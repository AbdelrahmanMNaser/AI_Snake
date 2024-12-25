from queue import PriorityQueue

class AStar:
    def find_path(self, start_node, goal_node):
        """Implement A* search algorithm using priority queue"""
        open_set = PriorityQueue()
        open_set.put((0, start_node))
        open_set_hash = {start_node} 
        
        closed_set = set()
        g_scores = {start_node: 0}
        parents = {}
        f_scores = {start_node: start_node.get_heuristic()}
        
        while not open_set.empty():
            current = open_set.get()[1]  # Get node with minimum f_score
            open_set_hash.remove(current)
            
            if current == goal_node:
                return self._reconstruct_path(parents, current)
            
            closed_set.add(current)
            
            for neighbor, edge in current.get_neighbor_data():
                if neighbor in closed_set:
                    continue
                    
                tentative_g = g_scores[current] + edge.cost
                
                if neighbor not in open_set_hash:
                    open_set_hash.add(neighbor)
                    # Add to priority queue with f_score as priority
                    f_score = tentative_g + neighbor.get_heuristic()
                    open_set.put((f_score, neighbor))
                elif tentative_g >= g_scores.get(neighbor, float('inf')):
                    continue
                
                parents[neighbor] = current
                g_scores[neighbor] = tentative_g
                f_scores[neighbor] = tentative_g + neighbor.get_heuristic()
        
        return None
    
    def calculate_total_cost(self, start_node, goal_node):
        """Calculate total cost (f-score) from start to goal node"""
        path = self.find_path(start_node, goal_node)
        if not path:
            return float('inf')
        
        # Calculate g-score (actual path cost)
        g_score = 0
        for i in range(len(path) - 1):
            current = path[i]
            next_node = path[i + 1]
            
            # Find edge cost between current and next node
            for neighbor, edge in current.get_neighbor_data():
                if neighbor == next_node:
                    g_score += edge.cost
                    break
        
        # Add h-score (heuristic of goal node)
        h_score = goal_node.get_heuristic()
        
        return g_score + h_score


    def _reconstruct_path(self, parents, current):
        """Reconstruct path from parents dictionary"""
        path = [current]
        while current in parents:
            current = parents[current]
            path.append(current)
        return path[::-1]  # Reverse path to get start->goal