import pygame
from src.core.snake import Snake
from src.core.apple import Apple
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from src.algorithm.astar import AStar
from src.utils.event_handler import EventHandler
from src.ui.menu_manager import MenuManager
from src.ui.renderer import Renderer
from src.core.game_state import GameState

class Game:
    def __init__(self, width=800, height=600):
        pygame.init()
        self.width = width
        self.height = height
        self.block_size = 20
        self.cols = width // self.block_size
        self.rows = height // self.block_size
        
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('AI Snake')
        
        self.snake = Snake(self.cols//2, self.rows//2, self.block_size)
        self.apple = Apple(self.cols, self.rows, self.block_size)
        self.astar = AStar()
        
        self.state = "MENU"
        self.game_over = False
        self.clock = pygame.time.Clock()
        
        self.menu_manager = MenuManager(self.screen, width, height)
        self.event_handler = EventHandler(self)
        self.game_state = GameState(self.snake, self.apple, self.cols, self.rows)
        self.renderer = Renderer(self.screen)

    def run(self):
        while not self.game_over:
            if self.state == "MENU":
                self.event_handler.handle_events()
                self.menu_manager.draw_menu()
            elif self.state == "OPTIONS":
                self.event_handler.handle_events()
                self.menu_manager.draw_options()
            elif self.state == "GAME":
                self.event_handler.handle_events()
                self.game_state.update(self.astar)
                if self.game_state.check_collisions():
                    self.game_over = True
                self.renderer.draw_game(self.snake, self.apple, self.game_state.score)
            
            self.clock.tick(self.fps_to_ticks(self.menu_manager.fps))
        
        pygame.quit()

    def fps_to_ticks(self, fps):
        if fps <= 0:
            return 1000
        return 1000 // fps

