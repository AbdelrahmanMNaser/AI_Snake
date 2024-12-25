import pygame
import random

class Apple:
    def __init__(self, cols, rows, block_size):
        self.cols = cols
        self.rows = rows
        self.block_size = block_size
        self.position = self.place_apple([])

    def place_apple(self, snake_body):
        while True:
            x = random.randint(0, self.cols-1)
            y = random.randint(0, self.rows-1)
            if (x, y) not in snake_body:
                return (x, y)

    def draw(self, screen):
        apple_x, apple_y = self.position
        pygame.draw.rect(screen, (255, 0, 0), 
                         [apple_x * self.block_size, apple_y * self.block_size, 
                          self.block_size, self.block_size])