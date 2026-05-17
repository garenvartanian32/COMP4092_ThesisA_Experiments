class Graph:

    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges

    def find_shortest_path(self, start, end, heuristic=None):
        """find shortest path using A* algorithm"""
        open_set = {start}
        came_from = {}
        g_score = {node: float('inf') for node in self.nodes}
        g_score[start] = 0
        f_score = {node: float('inf') for node in self.nodes}
        f_score[start] = self.apply_heuristic(start, end, heuristic)
        while open_set:
            current = min(open_set, key=lambda x: f_score[x])
            if current == end:
                return self.reconstruct_path(came_from, current)
            open_set.remove(current)
            for neighbor in self.get_neighbors(current):
                tentative_g_score = g_score[current] + self.distance(current, neighbor)
                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self.apply_heuristic(neighbor, end, heuristic)
                    if neighbor not in open_set:
                        open_set.add(neighbor)
        return None

    def get_neighbors(self, node):
        """get neighbors of a node"""
        return [edge[1] for edge in self.edges if edge[0] == node]

    def distance(self, node_a, node_b):
        """calculate distance between two nodes"""
        for edge in self.edges:
            if (edge[0], edge[1]) == (node_a, node_b):
                return edge[2]
        return float('inf')

    def reconstruct_path(self, came_from, current):
        """reconstruct path from start to end"""
        total_path = [current]
        while current in came_from:
            current = came_from[current]
            total_path.insert(0, current)
        return total_path