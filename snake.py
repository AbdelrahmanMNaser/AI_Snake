import pygame
from node import Node

class Snake:
    def __init__(self, x, y, block_size):
        self.block_size = block_size
        self.body = [(x, y)]  # Head is at index 0
        self.direction = (1, 0)  # Start moving right
        self.length = 1

    def move(self, next_position):
        # Add new head position
        self.body.insert(0, next_position)
        # Remove tail if not growing
        if len(self.body) > self.length:
            self.body.pop()

    def grow(self):
        self.length += 1

    def get_head(self):
        return self.body[0]

    def collides_with_self(self):
        return self.get_head() in self.body[1:]

    def draw(self, screen):
        for i, segment in enumerate(self.body):
            x, y = segment
            color = (0, 255, 0) if i != 0 else (0, 255, 255)  # Green for body, Red for head
            pygame.draw.rect(screen, color, 
                             [x * self.block_size, y * self.block_size, 
                              self.block_size, self.block_size])