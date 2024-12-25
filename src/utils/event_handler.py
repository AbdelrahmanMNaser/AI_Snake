import pygame

class EventHandler:
    def __init__(self, game):
        self.game = game

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.game_over = True
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse_click(pygame.mouse.get_pos())

    def handle_mouse_click(self, mouse_pos):
        if self.game.state == "MENU":
            if self.game.menu_manager.menu_buttons['start'].is_clicked(mouse_pos):
                self.game.state = "GAME"
            elif self.game.menu_manager.menu_buttons['options'].is_clicked(mouse_pos):
                self.game.state = "OPTIONS"
            elif self.game.menu_manager.menu_buttons['quit'].is_clicked(mouse_pos):
                self.game.game_over = True
                
        elif self.game.state == "OPTIONS":
            for speed, button in self.game.menu_manager.option_buttons.items():
                if button.is_clicked(mouse_pos):
                    self.game.menu_manager.fps = self.game.menu_manager.speeds[speed]
                    self.game.state = "MENU"