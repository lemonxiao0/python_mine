'''
python my first game

'''
import pygame
import mine_menu
from pygame.locals import *
from random import randint, choice
from gameobjects.vector2 import Vector2

pygame.init()
screen_size = (560, 560)
screen = pygame.display.set_mode(screen_size, HWSURFACE | SRCALPHA, 32)

back_ground = pygame.image.load('image/aloucs.jpg').convert()

start_x, start_y = 40, 40
end_x, end_y = start_x + 480, start_y + 480

g_mouse_first = True
mine_row, mine_col = 14, 16
mine_count = 35
remain_banners = mine_count

#mine place is 16x16
mine_state = [[0 for row in range(mine_col)] for col in range(mine_row)]
mine_show  = [[0 for row in range(mine_col)] for col in range(mine_row)]
#surface mine
image_state = [0 for image in range(15)]

image_state[0] = pygame.image.load('image/button.png').convert_alpha()
image_state[1] = pygame.image.load('image/mark.png').convert_alpha()
image_state[2] = pygame.image.load('image/lei_ed.png').convert_alpha()
image_state[3] = pygame.image.load('image/lei_bad.png').convert_alpha()
image_state[4] = pygame.image.load('image/lei.png').convert_alpha()
image_state[5] = pygame.image.load('image/blank_9.png').convert_alpha() #9
image_state[6] = pygame.image.load('image/blank_8.png').convert_alpha() #8
image_state[7] = pygame.image.load('image/blank_7.png').convert_alpha() #7
image_state[8] = pygame.image.load('image/blank_6.png').convert_alpha() #6
image_state[9] = pygame.image.load('image/blank_5.png').convert_alpha() #5
image_state[10] = pygame.image.load('image/blank_4.png').convert_alpha() #4
image_state[11] = pygame.image.load('image/blank_3.png').convert_alpha() #3
image_state[12] = pygame.image.load('image/blank_2.png').convert_alpha() #2
image_state[13] = pygame.image.load('image/blank_1.png').convert_alpha() #1
image_state[14] = pygame.image.load('image/button_ed.png').convert_alpha() #butten down

face_image_state = [0 for face_image in range(6)]
face_image_state[0] = pygame.image.load('image/common.png').convert_alpha()
face_image_state[1] = pygame.image.load('image/common_ed.png').convert_alpha()
face_image_state[2] = pygame.image.load('image/success.png').convert_alpha()
face_image_state[3] = pygame.image.load('image/success_ed.png').convert_alpha()
face_image_state[4] = pygame.image.load('image/fail.png').convert_alpha()
face_image_state[5] = pygame.image.load('image/fail_ed.png').convert_alpha()

face_image_mode = {'common':0, 'common_ed':1, 'success':2, 'success_ed':3, 'fail':4, 'fail_ed':5}


class azeal_mine(object):
    #install mine
    def __init__(self, row_nums, col_nums, mine_nums, screen_font, screen_face):
        global start_x, start_y
        self.redraw = False
        self.set_mine_row_col(row_nums, col_nums, mine_nums)
        self.screen_font = screen_font
        self.screen_face = screen_face
        self.mine_fail_or_success = 0
        self.init_data()
    
    def set_mine_row_col(self, row, col, mine_nums):
        self.self_mine_count = mine_nums
        self.self_mine_row = row
        self.self_mine_col = col
        if self.self_mine_col >16:
            self.self_mine_col = 16
        if self.self_mine_row >16:
            self.self_mine_row = 16
        if self.self_mine_count > int(0.9 * self.self_mine_col * self.self_mine_col):
            self.self_mine_count = int(0.9 * self.self_mine_col * self.self_mine_col)
        self.start_x = (screen_size[0] - self.self_mine_col * 30)/2
        self.start_y = (screen_size[1] - self.self_mine_row * 30)/2 
        
    
    def set_fail_or_success(self, state):
        self.mine_fail_or_success = state
    
    def get_fail_or_success(self):
        return self.mine_fail_or_success 
    
    def init_data(self):
        self.mine_fail_or_success = 0
        self.remain_no_turn_over = self.self_mine_col * self.self_mine_row
    
    def reduce_no_turn_over(self):
        self.remain_no_turn_over -= 1
    
    def set_redraw(self, bDraw):
        self.redraw = bDraw
    
    def get_redraw(self):
        return self.redraw
    
    
    def get_count(self):
        return self.self_mine_count
    
    def mine_restart(self):
        global mine_state
        global mine_show
        global g_mouse_first
        
        
        for row_index in range(self.self_mine_row):
            for col_index in range(self.self_mine_col):
                mine_state[row_index][col_index] = 0
                mine_show[row_index][col_index] = 0
        self.install_mine()
        g_mouse_first = True
        self.init_data()
        self.screen_font.restart()
        self.screen_face.set_face_mode('common', 'common_ed')
        self.screen_face.set_foucs(False)
        
    def install_mine(self):
       for row_index in range(self.self_mine_row):
           for col_index in range(self.self_mine_col):
               mine_state[row_index][col_index] = 0
       mine_count_temp = self.self_mine_count
       while mine_count_temp != 0:
            rand_row = randint(0, self.self_mine_row -1)
            rand_col = randint(0, self.self_mine_col -1)
            if mine_state[rand_row][rand_col] == 4:
                pass
            else:
                mine_state[rand_row][rand_col] = 4
                mine_count_temp -= 1
       for row_index in range(self.self_mine_row):
           for col_index in range(self.self_mine_col):    
               round_mine_count = 0
               if mine_state[row_index][col_index] != 4:
                   if (row_index - 1)>=0 and (col_index - 1)>=0 :
                       if mine_state[row_index - 1][col_index -1] == 4:
                           round_mine_count += 1
                         
                   if (row_index - 1)>=0 and (col_index    )>=0 :
                       if mine_state[row_index - 1][col_index] == 4:
                           round_mine_count += 1
                        
                   if (row_index - 1)>=0 and (col_index + 1)<self.self_mine_col :
                       if mine_state[row_index - 1][col_index + 1] == 4:
                           round_mine_count += 1
                        
                   if (row_index    )>=0 and (col_index - 1)>=0 :
                       if mine_state[row_index][col_index -1] == 4:
                           round_mine_count += 1
                        
                   if (row_index    )>=0 and (col_index + 1)<self.self_mine_col :
                       if mine_state[row_index][col_index + 1] == 4:
                           round_mine_count += 1
                        
                   if (row_index + 1)<self.self_mine_row and (col_index -1)>=0 :
                       if mine_state[row_index + 1][col_index -1] == 4:
                           round_mine_count += 1
                        
                   if (row_index + 1)<self.self_mine_row and (col_index)>=0 :
                       if mine_state[row_index + 1][col_index] == 4:
                           round_mine_count += 1
                        
                   if (row_index + 1)<self.self_mine_row and (col_index +1)<self.self_mine_col:
                       if mine_state[row_index + 1][col_index +1] == 4:
                           round_mine_count += 1
                   
                   mine_state[row_index][col_index] = 14 - round_mine_count
        
      
    def open_mine(self, row_index, col_index, mouse_first):
        global g_mouse_first
        global mine_state
        global mine_show
        
        if row_index < 0 or row_index >= self.self_mine_row or col_index < 0 or col_index>= self.self_mine_col:
            return
        
        if mine_show[row_index][col_index] != 0:
            return

        if mouse_first == True:
            if mine_state[row_index][col_index] == 4:
                self.install_mine()
                self.open_mine(row_index, col_index, mouse_first)
            g_mouse_first = False
#we should open round place when click place is '0'==>mine_state[row_index][col_index] = 14
        if mine_state[row_index][col_index] == 14 and mine_show[row_index][col_index] == 0:
            mine_show[row_index][col_index] = mine_state[row_index][col_index]
            self.reduce_no_turn_over()
            if ((row_index - 1)>=0 and (col_index - 1)>=0) and mine_show[row_index-1][col_index-1] == 0:
                if mine_state[row_index - 1][col_index - 1] == 14:
                    self.open_mine(row_index - 1, col_index - 1, g_mouse_first)
                else:
                    mine_show[row_index - 1][col_index - 1] = mine_state[row_index - 1][col_index - 1]
                    self.reduce_no_turn_over()
            
            if ((row_index - 1)>=0 and (col_index)>=0) and mine_show[row_index-1][col_index] == 0:
                if mine_state[row_index - 1][col_index] == 14:
                    self.open_mine(row_index - 1, col_index, g_mouse_first)
                else:
                    mine_show[row_index - 1][col_index] = mine_state[row_index - 1][col_index]
                    self.reduce_no_turn_over()

            if ((row_index - 1)>=0 and (col_index + 1)<self.self_mine_col) and mine_show[row_index - 1][col_index + 1] == 0:
                if mine_state[row_index - 1][col_index + 1] == 14:
                    self.open_mine(row_index - 1, col_index + 1, g_mouse_first)
                else:
                    mine_show[row_index - 1][col_index + 1] = mine_state[row_index - 1][col_index + 1]
                    self.reduce_no_turn_over()
            
            if ((row_index)>=0 and (col_index - 1)>=0) and mine_show[row_index][col_index-1] == 0:
                if mine_state[row_index][col_index - 1] == 14:
                    self.open_mine(row_index, col_index - 1, g_mouse_first)
                else:
                    mine_show[row_index][col_index - 1] = mine_state[row_index][col_index - 1]
                    self.reduce_no_turn_over()
                
            if ((row_index)>=0 and (col_index + 1)<self.self_mine_col) and mine_show[row_index][col_index+1] == 0:
                if mine_state[row_index][col_index + 1] == 14:
                    self.open_mine(row_index, col_index + 1, g_mouse_first)
                else:
                    mine_show[row_index][col_index + 1] = mine_state[row_index][col_index + 1]
                    self.reduce_no_turn_over()

            if ((row_index + 1)<self.self_mine_row and (col_index - 1)>=0) and mine_show[row_index+1][col_index-1] == 0:
                if mine_state[row_index + 1][col_index - 1] == 14:
                    self.open_mine(row_index + 1, col_index - 1, g_mouse_first)
                else:
                    mine_show[row_index + 1][col_index - 1] = mine_state[row_index + 1][col_index - 1]
                    self.reduce_no_turn_over()

            if ((row_index + 1)<self.self_mine_row and (col_index)>=0) and mine_show[row_index+1][col_index] == 0:
                if mine_state[row_index + 1][col_index] == 14:
                    self.open_mine(row_index + 1, col_index, g_mouse_first)
                else:
                    mine_show[row_index + 1][col_index] = mine_state[row_index + 1][col_index]
                    self.reduce_no_turn_over()

            if ((row_index + 1)<self.self_mine_row and (col_index + 1)<self.self_mine_col) and mine_show[row_index+1][col_index+1] == 0:
                if mine_state[row_index + 1][col_index + 1] == 14:
                    self.open_mine(row_index + 1, col_index + 1, g_mouse_first)
                else:
                    mine_show[row_index + 1][col_index + 1] = mine_state[row_index + 1][col_index + 1]
                    self.reduce_no_turn_over()
            
        else:
           mine_show[row_index][col_index] = mine_state[row_index][col_index]
           self.reduce_no_turn_over()
        
        if mine_show[row_index][col_index] == 4:
           mine_show[row_index][col_index] = 2
           self.screen_face.set_face_mode('fail', 'fail_ed')
           self.screen_face.set_foucs(False)
           self.mine_fail_or_success = -1
           for row_index in range(self.self_mine_row):
               for col_index in range(self.self_mine_col):
                   if mine_state[row_index][col_index] == 4 and mine_show[row_index][col_index] == 0:
                      mine_show[row_index][col_index] = 4
                   elif mine_state[row_index][col_index] != 4 and mine_show[row_index][col_index] == 1:
                      mine_show[row_index][col_index] = 3  
           return
    
        if self.screen_font.get_remain_banners_count() >= 0 and  self.screen_font.get_banners_count() == (self.screen_font.get_remain_banners_count() + self.remain_no_turn_over):
            self.screen_face.set_face_mode('success', 'success_ed')
            self.screen_face.set_foucs(False)
            self.mine_fail_or_success = 1
        
    def process_mouse_left_and_right_down(self, row_index, col_index):
        global mine_state, mine_show
        if mine_show[row_index][col_index] == 0:
            return
        if mine_state[row_index][col_index] < 5 and mine_state[row_index][col_index] >13:
            return
        the_place_num = 14 - mine_state[row_index][col_index] #how mang mine count round the place
        #so judge whether haved imput the_num banners rount the place
        the_place_nums_banners = 0
        for row_index_temp in [row_index-1, row_index, row_index+1]:
            for col_index_temp in [col_index-1,col_index, col_index+1]:
                if row_index_temp >=0 and col_index_temp >=0 \
                    and row_index_temp < self.self_mine_row and col_index_temp < self.self_mine_col \
                    and (row_index_temp !=row_index or col_index_temp != col_index ):
                    if mine_show[row_index_temp][col_index_temp] == 1:
                       the_place_nums_banners += 1
        
        if the_place_num != the_place_nums_banners:
            return
        
        for row_index_temp in [row_index-1, row_index, row_index+1]:
            for col_index_temp in [col_index-1,col_index, col_index+1]:
                if row_index_temp >=0 and col_index_temp >=0 \
                    and row_index_temp < self.self_mine_row and col_index_temp < self.self_mine_col \
                    and (row_index_temp !=row_index or col_index_temp != col_index ):
                    self.open_mine(row_index_temp, col_index_temp, g_mouse_first)
                    if mine_show[row_index_temp][col_index_temp] == 4:
                        mine_show[row_index_temp][col_index_temp] = 2
        
        
              
        
    def process_banner(self, row_index, col_index):
        global mine_show, remain_banners
        if row_index < 0 or row_index >= self.self_mine_row or col_index < 0 or col_index>= self.self_mine_col:
          return

        if mine_show[row_index][col_index] == 1:
            mine_show[row_index][col_index] = 0
            self.screen_font.increase()
        elif mine_show[row_index][col_index] == 0:
            mine_show[row_index][col_index] = 1
            self.screen_font.decrease()
        else:
            pass
#        print("%s--%s--%s" % (self.screen_font.get_remain_banners_count(), self.screen_font.get_banners_count(), self.remain_no_turn_over))

        if self.screen_font.get_remain_banners_count() >= 0 and self.screen_font.get_banners_count() == (self.screen_font.get_remain_banners_count() + self.remain_no_turn_over):
            self.screen_face.set_face_mode('success', 'success_ed')
            self.screen_face.set_foucs(False)
            self.mine_fail_or_success = 1
            

class ScreenFace(object):

    def __init__(self, screen_width, screen_height, surface):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.show_position = (int((screen_width - 45)/2), 0)
        self.face_mode = 'common'
        self.face_foucs_mode = 'common_ed'
        self.screen = surface
        self.foucs = False
        
    def set_face_mode(self, mode, foucs_mode):
        self.face_mode = mode
        self.face_foucs_mode = foucs_mode
    
    def set_foucs(self, bFoucs):
        self.foucs = bFoucs
        
    def show_face(self):
        global face_image_mode, face_image_state
        if self.foucs == False:
            self.screen.blit(face_image_state[face_image_mode[self.face_mode]], self.show_position)
        else:
            self.screen.blit(face_image_state[face_image_mode[self.face_foucs_mode]], self.show_position)
            
    def mousepos_is_here(self, pos):
        if self.show_position[0] <= pos[0] and (self.show_position[0] + 45) >= pos[0] \
            and self.show_position[1] <= pos[1] and (self.show_position[1] + 45) >= pos[1]:
            return True
        return False
      
    def mouse_up_exit_mode(self, pos):
        if self.mousepos_is_here( pos) == False:
            self.set_foucs(False)
        
class ScreenFont(object):
    def __init__(self, surface, banners_all):
       self.font = pygame.font.SysFont("arial_black", 16)
       self.font_tps = pygame.font.SysFont("arial", 16)
       self.screen = surface 
       self.remain_banners_count = banners_all
       self.banners_all = banners_all
    
    def restart(self):
       self.remain_banners_count = self.banners_all 
    
    def increase(self):
       self.remain_banners_count += 1
    
    def decrease(self):
        self.remain_banners_count -= 1 

    def get_remain_banners_count(self):
        return self.remain_banners_count
    
    def get_banners_count(self):
        return self.banners_all
    

    def set_remain_banners_count(self, remain_banners_count, banners_all):
       self.remain_banners_count = remain_banners_count
       self.banners_all = banners_all
    
    def show(self, pos):
        text = "remain_banners: " + str(self.remain_banners_count)
        font_surface = self.font.render(text, True, (47, 77, 247))
        self.screen.blit(font_surface, pos)
        font_surface_tip = self.font_tps.render("Precss ESC Setting", True, (255, 0, 0))
        self.screen.blit(font_surface_tip, (pos[0], pos[1]+18))
  
def run():
    global mine_row, mine_col
    screen.blit(back_ground, (0, 0))
    font = ScreenFont(screen, remain_banners)
    face = ScreenFace(screen_size[0], screen_size[1], screen)
    mine = azeal_mine(mine_row, mine_col, mine_count, font, face)
    menu = mine_menu.menu_title(screen, back_ground, screen_size, 22, 10, (145, 145, 145), (73, 140, 252))
    menu.add_text("Primary")
    menu.add_text("middle-level")
    menu.add_text("high level")
    menu.add_text("Cancel")
    menu.calculate_pos()
    
    mine.install_mine()
    pygame.display.set_caption('python_pygame_mine_Azeal')
    
    loop = True
    time_clock = pygame.time.Clock()
    while loop:
        time_clock.tick(30)
        for event in pygame.event.get():
            if event.type == QUIT:
                loop = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                prew_mouse_press = pygame.mouse.get_pressed()
                if prew_mouse_press[0] == 1:
                    if face.mousepos_is_here(pygame.mouse.get_pos()) == True:
                        face.set_foucs(True)
            if event.type == pygame.MOUSEBUTTONUP:
                if prew_mouse_press == ():
                    continue
                if prew_mouse_press[0] == 1 and prew_mouse_press[2] == 1:
                    prew_mouse_press = ()
                    mouse_pos = pygame.mouse.get_pos()
                    if mine.get_fail_or_success() == 0:
                        mine.process_mouse_left_and_right_down((mouse_pos[1] - mine.start_y)/30, (mouse_pos[0] - mine.start_x)/30)
                
                elif prew_mouse_press[0] == 1:
                    if face.mousepos_is_here(pygame.mouse.get_pos()) == True:
                        mine.mine_restart()
                        prew_mouse_press = ()
                    else:                                               
                        prew_mouse_press = ()
                        mouse_pos = pygame.mouse.get_pos()
                        face.mouse_up_exit_mode(mouse_pos) 
                        if mine.get_fail_or_success() == 0:
                           mine.open_mine((mouse_pos[1] - mine.start_y)/30, (mouse_pos[0] - mine.start_x)/30, g_mouse_first)
                        
                elif prew_mouse_press[2] == 1:
                    prew_mouse_press = ()
                    mouse_pos = pygame.mouse.get_pos()
                    if mine.get_fail_or_success() == 0:
                       mine.process_banner((mouse_pos[1] - mine.start_y)/30, (mouse_pos[0] - mine.start_x)/30)
            
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    select_return = menu.run_loop()
                    if select_return == 0:
                        mine.set_mine_row_col(6, 6, 6)
                        mine.screen_font.set_remain_banners_count(6, 6)
                        mine.mine_restart()
                        prew_mouse_press = ()
                    elif select_return == 1:
                        mine.set_mine_row_col(10, 11, 12)
                        mine.screen_font.set_remain_banners_count(12, 12)
                        mine.mine_restart()
                        prew_mouse_press = ()
                    elif select_return == 2:
                       mine.set_mine_row_col(14, 16, 35)
                       mine.screen_font.set_remain_banners_count(35, 35)
                       mine.mine_restart()
                       prew_mouse_press = ()
                                                                                                                
        screen.blit(back_ground, (0, 0))
        font.show((0, 17))
        face.show_face()
        
        for row in range(mine.self_mine_row):
            for col in range(mine.self_mine_col):
                draw_point = (col * 30 + mine.start_x, row * 30 + mine.start_y)
                screen.blit(image_state[mine_show[row][col]], draw_point)

        
        pygame.display.update()

if __name__ == "__main__":
    run()
    pygame.display.quit()
    


