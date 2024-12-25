import pygame

class Renderer:
    def __init__(self, screen):
        self.screen = screen

    def draw_game(self, snake, apple, score):
        self.screen.fill((0, 0, 0))
        snake.draw(self.screen)
        apple.draw(self.screen)
        self.draw_score(score)
        pygame.display.flip()

    def draw_score(self, score):
        font = pygame.font.Font(None, 36)
        score_text = font.render(f'Score: {score}', True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))