import pygame
import random
from snake import Snake
from astar import AStar
from node import Node
from apple import Apple

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
        self.score = 0
        self.game_over = False
        self.clock = pygame.time.Clock()
        self.astar = AStar()


    def create_graph(self):
        # Create nodes for each valid position
        nodes = {}
        for x in range(self.cols):
            for y in range(self.rows):
                if (x, y) not in self.snake.body[1:]:  # Exclude snake body except head
                    pos = (x, y)
                    # Use 0 as heuristic for pure Dijkstra behavior
                    nodes[pos] = Node(x, y, 0)  
    
        # Connect nodes to neighbors
        for pos, node in nodes.items():
            x, y = pos
            neighbors = [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]
            for nx, ny in neighbors:
                if (nx, ny) in nodes:
                    node.add_neighbor(nodes[(nx, ny)], 1)
    
        return nodes

    def run(self):
        while not self.game_over:
            print(self.score)
            self.handle_events()
            self.update_game_state()
            self.check_collisions()
            self.draw()
            self.clock.tick(1000)  # Control game speed
    
        pygame.quit()
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
    
    def update_game_state(self):
        nodes = self.create_graph()
        start_node = nodes.get(self.snake.get_head())
        goal_node = nodes.get(self.apple.position)
    
        if start_node and goal_node:
            path = self.astar.find_path(start_node, goal_node)
            if path and len(path) > 1:
                next_node = path[1]
                self.snake.move((next_node.x, next_node.y))
    
                if self.snake.get_head() == self.apple.position:
                    self.snake.grow()
                    self.score += 1
                    self.apple.position = self.apple.place_apple(self.snake.body)
    
    def check_collisions(self):
        head_x, head_y = self.snake.get_head()
        if (head_x < 0 or head_x >= self.cols or 
            head_y < 0 or head_y >= self.rows or 
            self.snake.collides_with_self()):
            self.game_over = True
    
    def draw(self):
            self.screen.fill((0, 0, 0))
            self.snake.draw(self.screen)
            self.apple.draw(self.screen)
            self.draw_score()
            pygame.display.flip()

    def draw_score(self):
        font = pygame.font.Font(None, 36)
        score_text = font.render(f'Score: {self.score}', True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))
    

if __name__ == "__main__":
    game = Game()
    game.run()