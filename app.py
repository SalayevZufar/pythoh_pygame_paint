import pygame,sys
from pygame.locals import *
import pygame_gui

from pygame_gui.core import ObjectID
from pygame_gui.elements import UIButton



pygame.init()

pygame.display.set_caption("Paint")
clock = pygame.time.Clock()

class Brush():
    def __init__(self):
        self.radius = 5
        self.width = 5
        self.color = (0,0,0,0)
        self.raser = (255,255,255)
    
    def draw(self,canvas):
        
        if pygame.mouse.get_pressed()[0]:
            position = pygame.mouse.get_pos()
            if position[0] > 50:
                
                pygame.draw.circle(canvas, self.color, position, self.radius, self.width)
              
    
    
        elif pygame.mouse.get_pressed()[2]:
            position = pygame.mouse.get_pos()
            pygame.draw.circle(canvas, self.raser, position, self.radius, self.width)
    def change_color(self,event):      
        if event.ui_element == red_button:
            self.color = (255, 0, 0)
        elif event.ui_element == yellow_button:
            self.color = (255, 255, 0)
        elif event.ui_element == green_button:
            self.color = (0,128,0)
        elif event.ui_element == blue_button:
            self.color = (0,0,255) 
        elif event.ui_element == purple_button:
            self.color = (160,32,240) 
        elif event.ui_element == pink_button:
            self.color = (255,192,203) 
        elif event.ui_element == brown_button:
            self.color = (150,75,0) 
        elif event.ui_element == orange_button:
            self.color = (255,165,0) 
        elif event.ui_element == cyan_button:
            self.color = (0,255,255)
        elif event.ui_element == teal_button:
            self.color = (0,125,125) 
        elif event.ui_element == olive_button:
            self.color = (128,128,0) 
        elif event.ui_element == tan_button:
            self.color = (210,180,140) 
        elif event.ui_element == violet_button:
            self.color = (207, 159, 255)
        elif event.ui_element == indigo_button:
            self.color = (75,0,130)  
        elif event.ui_element == black_button:
            self.color = (0,0,0)
        elif event.ui_element == gray_button:
            self.color = (128,128,128)    
canvas = pygame.display.set_mode((700,500))


manager = pygame_gui.UIManager((700,500), theme_path="button.json")
canvas.fill((255,255,255))
options_list = [f"{x}" for x in range(20)]
small_brush = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0,0), (50,50)), text="", manager=manager)
medium_brush = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0,50), (50,50)), text="", manager=manager)
large_brush = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0,100), (50,50)), text="", manager=manager)


button_3 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0,450), (50,50)), text="Clear", manager=manager)



red_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0,150), (25,25)), text="", manager=manager,object_id=ObjectID(class_id='@red_btn'))
yellow_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((25,150), (25,25)), text="", manager=manager,object_id=ObjectID(class_id='@yellow_btn'))
green_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0,175), (25,25)), text="", manager=manager,object_id=ObjectID(class_id='@green_btn'))
blue_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((25,175), (25,25)), text="", manager=manager,object_id=ObjectID(class_id='@blue_btn'))
purple_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0,200), (25,25)), text="", manager=manager,object_id=ObjectID(class_id='@purple_btn'))
pink_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((25,200), (25,25)), text="", manager=manager,object_id=ObjectID(class_id='@pink_btn'))
brown_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0,225), (25,25)), text="", manager=manager,object_id=ObjectID(class_id='@brown_btn'))
orange_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((25,225), (25,25)), text="", manager=manager,object_id=ObjectID(class_id='@orange_btn'))
cyan_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0,250), (25,25)), text="", manager=manager,object_id=ObjectID(class_id='@cyan_btn'))
teal_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((25,250), (25,25)), text="", manager=manager,object_id=ObjectID(class_id='@teal_btn'))
olive_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0,275), (25,25)), text="", manager=manager,object_id=ObjectID(class_id='@olive_btn'))
tan_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((25,275), (25,25)), text="", manager=manager,object_id=ObjectID(class_id='@tan_btn'))
violet_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0,300), (25,25)), text="", manager=manager,object_id=ObjectID(class_id='@violet_btn'))
indigo_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((25,300), (25,25)), text="", manager=manager,object_id=ObjectID(class_id='@indigo_btn'))
black_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0,325), (25,25)), text="", manager=manager,object_id=ObjectID(class_id='@black_btn'))
gray_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((25,325), (25,25)), text="", manager=manager,object_id=ObjectID(class_id='@gray_btn'))




pygame.mouse.set_cursor(pygame.cursors.broken_x)
brush = Brush()

while True:
    time_delta = clock.tick(1000)
    pygame.draw.rect(canvas,(148, 166, 155), pygame.Rect(0, 0, 50, 500))
    for event in pygame.event.get():
        if(event.type == QUIT):
            pygame.quit()
            sys.exit(1)
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            
            
            if event.ui_element == large_brush:
                brush.radius = 10
                brush.width = 10
                
            elif event.ui_element == small_brush:
                brush.radius = 5
                brush.width = 5
            elif event.ui_element == medium_brush:
                brush.radius = 7
                brush.width = 7
            elif event.ui_element == button_3:
                canvas.fill((255,255,255))
            brush.change_color(event)
        manager.process_events(event)
    clock.tick(1000)
    brush.draw(canvas)
    
    manager.update(time_delta)
    manager.draw_ui(canvas)
    pygame.draw.circle(canvas, brush.color, (25,25), 5, 5)
    pygame.draw.circle(canvas, brush.color, (25,75), 7, 7)
    pygame.draw.circle(canvas, brush.color, (25,125), 10, 10)
    
    pygame.display.update()