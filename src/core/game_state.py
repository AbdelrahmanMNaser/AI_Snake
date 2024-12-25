from src.algorithm.node import Node

class GameState:
    def __init__(self, snake, apple, cols, rows):
        self.snake = snake
        self.apple = apple
        self.cols = cols
        self.rows = rows
        self.score = 0

    def create_graph(self):
        nodes = {}
        for x in range(self.cols):
            for y in range(self.rows):
                if (x, y) not in self.snake.body[1:]:
                    pos = (x, y)
                    nodes[pos] = Node(x, y, 0)
        
        for pos, node in nodes.items():
            x, y = pos
            neighbors = [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]
            for nx, ny in neighbors:
                if (nx, ny) in nodes:
                    node.add_neighbor(nodes[(nx, ny)], 1)
        
        return nodes

    def update(self, astar):
        nodes = self.create_graph()
        start_node = nodes.get(self.snake.get_head())
        goal_node = nodes.get(self.apple.position)
    
        if start_node and goal_node:
            path = astar.find_path(start_node, goal_node)
            if path and len(path) > 1:
                next_node = path[1]
                self.snake.move((next_node.x, next_node.y))
    
                if self.snake.get_head() == self.apple.position:
                    self.snake.grow()
                    self.score += 1
                    self.apple.position = self.apple.place_apple(self.snake.body)

    def check_collisions(self):
        head_x, head_y = self.snake.get_head()
        return (head_x < 0 or head_x >= self.cols or 
                head_y < 0 or head_y >= self.rows or 
                self.snake.collides_with_self())