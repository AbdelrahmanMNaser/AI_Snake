from edge import Edge

class Node:
    def __init__(self, x=0, y=0, heuristic=0):
        self.x = x
        self.y = y
        self.heuristic = heuristic
        self.neighbors = []
        self.edges = []

    def add_neighbor(self, neighbor, edge_cost):
        edge = Edge(edge_cost)
        self.neighbors.append(neighbor)
        self.edges.append(edge)

    def get_heuristic(self):
        return self.heuristic

    def get_neighbor_data(self):
        return list(zip(self.neighbors, self.edges))

    def __lt__(self, other):
        # Required for PriorityQueue comparison
        return False

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return self.x == other.x and self.y == other.y
        
    def __hash__(self):
        # Hash based on x,y coordinates
        return hash((self.x, self.y))