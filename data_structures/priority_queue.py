
class PriorityQueue:
    
    def __init__(self):
        self.pq = [(0, 0)]
        # Adapting methods `change_priority` and `contains` 
        self.idx_finder = {} # O(1) access using item as the key
        self.n = 0

    def _swap(self, x, y):
        if (x != y):
            tmp = self.pq[x]
            self.pq[x] = self.pq[y]
            self.pq[y] = tmp
            
            x_item = self.pq[x][1]
            y_item = self.pq[y][1]
            self.idx_finder[x_item] = x
            self.idx_finder[y_item] = y
    

    def _greater(self, x, y):
        # Thanks to the code from Sedgewick
        # src: https://algs4.cs.princeton.edu/24pq/MinPQ.java.html
        if (y <= self.n):
            return self.pq[x][0] > self.pq[y][0]
        else:
            return False

    
    def _parent(self, i):
        return i // 2


    def _left(self, i):
        return 2 * i


    def _right(self, i):
        return 2 * i + 1


    def _swim(self, i):
        if (i <= 1):
            return

        parent = self._parent(i)
        if (self.pq[i][0] < self.pq[parent][0]):
            self._swap(i, parent)
            self._swim(parent)


    def _sink(self, i):
        if (i <= self.n):
            l = self._left(i)
            r = self._right(i)
            candidate = i 

            if (self._greater(i, l)):
                if (self._greater(l, r)):
                    candidate = r 
                else:
                    candidate = l 
            elif (self._greater(i, r)):
                candidate = r
                
            if (candidate != i):
                self._swap(candidate, i)
                self._sink(candidate)


    def is_empty(self):
        return self.n == 0
    
    
    def size(self):
        return self.n


    def push(self, priority, item):
        self.pq.append((priority, item))
        self.n += 1
        self.idx_finder[item] = self.n
        self._swim(self.n)
        

    def pop(self):
        self._swap(1, self.n)
        priority, item = self.pq.pop()
        self.n -= 1
        self._sink(1)
        del self.idx_finder[item]

        return priority, item
    

    def contains(self, item):
        return (item in self.idx_finder)

    
    def change_priority(self, new_priority, item : object):
        if (self.contains(item)):
            idx = self.idx_finder[item]
            priority, _ = self.pq[idx]
            self.pq[idx] = (new_priority, item)
            if (priority > new_priority):
                self._swim(idx)
            elif (priority < new_priority):
                self._sink(idx)

