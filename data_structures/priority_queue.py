class PriorityQueue:
    """
    A priority queue. Note that items are ensured to be unique.
    ---
    Min-heap invariant:
    parent < both of its children
    ---
    Data Structure:
    1. Array storing [priority, item]
    2. Dict of item to index (for O(1) access to an item in the heap)
    """

    def __init__(self):
        self.heap = []
        self.item_index_map = {}
    
    
    def __contains__(self, key):
        return key in self.item_index_map


    def __len__(self):
        return len(self.heap)

    
    def __str__(self):
        return "Heap:\n{}\nItem to index mapping:\n{}\n".format(
            self.heap.__str__(),
            self.item_index_map.__str__()
        )


    def __setitem__(self, key, value):
        if (key in self):
            self.replace(key, value)
        else:
            self.push(key, value)


    def __getitem__(self, key):
        if (key not in self):
            raise LookupError("Item doesn't exist!")
        return self.item_index_map[key]


    def _swap(self, x, y):
        if (x != y):
            item_x = self.heap[x][1]
            item_y = self.heap[y][1]
            self.heap[x], self.heap[y] = self.heap[y], self.heap[x]
            # Index of x and y has been swapped
            self.item_index_map[item_x] = y 
            self.item_index_map[item_y] = x


    def _less(self, x, y):
        return self.heap[x][0] < self.heap[y][0]
    

    def _greater(self, x, y):
        return self._less(y, x)


    def _findsmallest(self, index):
        smallest = index 
        left_child = index * 2 + 1
        right_child = index * 2 + 2
        if (right_child >= len(self)):
            if (left_child < len(self) and
                self._less(left_child, smallest)):
                smallest = left_child
        else:
            if (self._less(left_child, smallest)):
                smallest = left_child
            if (self._less(right_child, smallest)):
                smallest = right_child
        return smallest


    def _siftup(self, index):
        if (index <= 0):
            return
        parent = (index - 1) // 2
        if (self._less(index, parent)):
            self._swap(parent, index)
            self._siftup(parent)

    
    def _siftdown(self, index):
        if (index >= len(self)):
            return
        smallest = self._findsmallest(index)
        if (smallest != index):
            self._swap(index, smallest)
            self._siftdown(smallest)


    def push(self, item, priority):
        if (item in self):
            raise LookupError("Item already exists in the heap!")

        self.heap.append([priority, item])
        self.item_index_map[item] = len(self) - 1
        self._siftup(len(self) - 1)


    def pop(self):
        """
        Extract the item with minimum priority in the heap
        """
        if (not self):
            raise RuntimeError("Heap is empty!")
            
        self._swap(0, len(self) - 1)
        top = self.heap.pop()
        del self.item_index_map[top[1]]
        if (self):
            self._siftdown(0)
        return top


    def replace(self, item, priority):
        if (item not in self):
            raise LookupError("Item doesn't exist!")

        item_index = self.item_index_map[item]
        old_priority = self.heap[item_index][0]
        if (old_priority != priority):
            self.heap[item_index][0] = priority
            if (old_priority > priority):
                self._siftup(item_index)
            else:
                self._siftdown(item_index)
