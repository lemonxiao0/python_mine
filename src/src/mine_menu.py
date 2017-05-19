import pygame
from pygame.locals import *

class menu_title(object):
    def __init__(self, screen, bkGround, screen_size, font_size, interval_size, font_clocr = (145, 145, 145), font_select_color = (73, 140, 252)):
        self.screen          = screen
        self.bkGround        = bkGround
        self.screen_size     = screen_size
        self.title_text      = []
        self.title_text_pos  = []
        self.font_size       = font_size
        self.interval_size   = interval_size
        self.current_select  = -1
        self.font            = pygame.font.Font("FEASFBRG.TTF", font_size)
        self.font_select     = pygame.font.Font("FEASFBRG.TTF", font_size+15)
        self.font_color      = font_clocr
        self.font_select_color = font_select_color
        self.is_running      = True
        
    def add_text(self, title_str):
        if title_str == "": return
        self.title_text.append(title_str)
    
    def calculate_pos(self):
        text_count = len(self.title_text)
        height_interval = (self.screen_size[1] - text_count * self.font_size - (text_count-1) * self.interval_size)/2
                
        for index  in range(text_count):
            width_interval = ( self.screen_size[0] )/2
            pos = (width_interval, height_interval + index*(self.font_size + self.interval_size))
            self.title_text_pos.append([pos, len(self.title_text[index])])
#        print(self.title_text_pos)  
    
    def show_running_come(self):
        loop = True
        time_clock = pygame.time.Clock()
        speed_x, x_increase = 400, 0
        
        title_pos_temp  = []
        title_pos_state = [0 for index in range(len(self.title_text_pos))]

        for index in range(len(self.title_text_pos)):
            index_item = self.title_text_pos[index]
            if index % 2 ==0:
                title_pos_temp.append([(index_item[0][0] * -1, index_item[0][1]), index_item[1]])
            else:
                title_pos_temp.append([(index_item[0][0] + self.screen.get_width(), index_item[0][1]), index_item[1]])

        while loop:
            self.screen.blit(self.bkGround , (0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
            
            time_pass = time_clock.tick(30)        
            x_increase +=speed_x * time_pass/500
            is_run_over = 0
            for index in range(len(title_pos_temp)):
#                print("%s---%s---%s--%s" % (title_pos_temp[index][0], title_pos_state[index], self.title_text_pos[index][0], x_increase))
                index_item = title_pos_temp[index]
                font_running = self.font.render(self.title_text[index], True, self.font_color)
                if index % 2 == 0:
                    if title_pos_temp[index][0][0] + x_increase >= self.title_text_pos[index][0][0]:
                        self.screen.blit(font_running, self.title_text_pos[index][0])
                        if title_pos_state[index] == False: 
                            title_pos_state[index] = True
                            is_run_over += 1
                    else:
                        self.screen.blit(font_running, (title_pos_temp[index][0][0] + x_increase, title_pos_temp[index][0][1]))
                        is_run_over += 1
                elif index % 2 == 1:
                    if  title_pos_temp[index][0][0] - x_increase <= self.title_text_pos[index][0][0]:
                        self.screen.blit(font_running, self.title_text_pos[index][0])
                        if title_pos_state[index] == False: 
                            title_pos_state[index] = True
                            is_run_over += 1
                    else:
                        self.screen.blit(font_running, (title_pos_temp[index][0][0] - x_increase, title_pos_temp[index][0][1]))
                        is_run_over += 1 
            if is_run_over == 0: loop = False
            pygame.display.update()
            
    def show_running_leave(self):
        loop = True
        time_clock = pygame.time.Clock()
        speed_x, x_decrease = 400, 0
        
        title_pos_temp  = []
        title_pos_state = [0 for index in range(len(self.title_text_pos))]

        for index in range(len(self.title_text_pos)):
            index_item = self.title_text_pos[index]
            if index % 2 ==0:
                title_pos_temp.append([(index_item[0][0] * -1, index_item[0][1]), index_item[1]])
            else:
                title_pos_temp.append([(index_item[0][0] + self.screen.get_width(), index_item[0][1]), index_item[1]])

        while loop:
            self.screen.blit(self.bkGround , (0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
            
            time_pass = time_clock.tick(30)        
            x_decrease +=speed_x * time_pass/500
            is_run_over = 0
            for index in range(len(title_pos_temp)):
#                print("%s---%s---%s--%s" % (title_pos_temp[index][0], title_pos_state[index], self.title_text_pos[index][0], x_decrease))
                index_item = title_pos_temp[index]
                font_running = self.font.render(self.title_text[index], True, self.font_color)
                if index % 2 == 0:
                    if title_pos_temp[index][0][0] > (self.title_text_pos[index][0][0] - x_decrease):
                        pass
                    else:
                        self.screen.blit(font_running, (self.title_text_pos[index][0][0] - x_decrease, self.title_text_pos[index][0][1]))
                        is_run_over += 1
                elif index % 2 == 1:
                    if  title_pos_temp[index][0][0]  <= (self.title_text_pos[index][0][0] + x_decrease):
                        pass
                    else:
                        self.screen.blit(font_running, (self.title_text_pos[index][0][0] + x_decrease, self.title_text_pos[index][0][1]))
                        is_run_over += 1

            if is_run_over == 0: loop = False
            pygame.display.update()
        
                       
    def show_text(self):
        text_count = len(self.title_text)
        b_select = False
        for index  in range(text_count):
            mouse_pos = pygame.mouse.get_pos()
            rect_temp = (self.title_text_pos[index][0], (self.title_text_pos[index][1]*self.font_size/2, self.font_size))
            if rect_temp[0][0] <= mouse_pos[0] and (rect_temp[0][0] + rect_temp[1][0]) >= mouse_pos[0] \
                and rect_temp[0][1] <= mouse_pos[1] and (rect_temp[0][1] + rect_temp[1][1]) >= mouse_pos[1]:
                font_surface = self.font_select.render(self.title_text[index], True, self.font_select_color)
                self.screen.blit(font_surface, (self.title_text_pos[index][0][0] -15, self.title_text_pos[index][0][1] - 15))
                self.current_select = index
                b_select = True
            else:
                font_surface = self.font.render(self.title_text[index], True, self.font_color)
                self.screen.blit(font_surface, self.title_text_pos[index][0])
        if b_select == False: self.current_select = -1
        
    def run_loop(self):
        self.show_running_come()
        select_return = -1
        loop = True
        time_clock = pygame.time.Clock()
        while loop:
            time_clock.tick(30)
            self.screen.blit(self.bkGround , (0, 0))
            self.show_text()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_press = pygame.mouse.get_pressed()
                    if mouse_press[0] == 1:
                        select_return = self.current_select
                        self.current_select = -1
                        loop = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        loop = False

            pygame.display.update()
        self.show_running_leave()
        return select_return
