import pygame
from src.ui.button import Button

class MenuManager:
    def __init__(self, screen, width, height):
        self.screen = screen
        button_width, button_height = 200, 50
        center_x = width // 2 - button_width // 2
        
        self.menu_buttons = {
            'start': Button(center_x, 200, button_width, button_height, "Start", (0, 100, 0)),
            'options': Button(center_x, 300, button_width, button_height, "Options", (0, 100, 0)),
            'quit': Button(center_x, 400, button_width, button_height, "Quit", (100, 0, 0))
        }
        
        self.option_buttons = {
            'slow': Button(center_x, 200, button_width, button_height, "Slow", (0, 100, 50)),
            'medium': Button(center_x, 300, button_width, button_height, "Medium", (0, 100, 100)),
            'fast': Button(center_x, 400, button_width, button_height, "Fast", (0, 100, 200))
        }
        
        self.speeds = {'slow': 60, 'medium': 30, 'fast': 10}
        self.fps = self.speeds['medium']

    def draw_menu(self):
        self.screen.fill((0, 0, 0))
        for button in self.menu_buttons.values():
            button.draw(self.screen)
        pygame.display.flip()
        
    def draw_options(self):
        self.screen.fill((0, 0, 0))
        for button in self.option_buttons.values():
            button.draw(self.screen)
        pygame.display.flip()