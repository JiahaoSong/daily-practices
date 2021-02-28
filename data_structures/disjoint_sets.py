class DisjointSets:
    def __init__(self, n):
        self.n = n 
        self.parents = [-1] * n 
    

    def _find(self, x):
        if (self.parents[x] < 0):
            return x 
        # Path compression
        self.parents[x] = self._find(self.parents[x])
        return self.parents[x]
    
    
    def size(self):
        return self.n


    def is_connected(self, v1, v2):
        return self._find(v1) == self._find(v2)
    

    def union(self, v1 ,v2):
        if (not (self.is_connected(v1, v2))):
            root1 = self._find(v1)
            root2 = self._find(v2)

            self.parents[root2] = root1
            self.n -= 1
    

        