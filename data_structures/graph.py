class Graph:
    """
    Implements a graph API with an adjacency list
    """
    
    def __init__(self, n_v) -> None:
        self.adj_list = [[] for _ in range(n_v)]
        self.n_v = n_v
        self.n_e = 0
    
    def __len__(self):
        return len(self.adj_list)
        
    def add_edge(self, u, v, w):
        self.adj_list[u].append((v, w))
        self.n_e += 1


    def neighbors(self, u):
        return self.adj_list[u]

    
    def vertex_size(self):
        return self.n_v


    def edge_size(self):
        return self.n_e