class MinHeap:
    """
    <Min heap> invariant:
    parent < both of its children

    Data Structure:
    1. array -> more like a stack
    2. empty case -> use a sentinel node

    """
    def __init__(self):
        self.entries = [None]
        self.first = 0

    def _is_empty(self):
        return len(self.entries) == 1

    def _swap(self, x, y):
        if (x == y):
            return

        temp = self.entries[x]
        self.entries[x] = self.entries[y]
        self.entries[y] = temp
    
    def _min(self, *idxs):
        idx_val_pairs = [[idx, self.entries[idx]] 
                         for idx in idxs 
                         if (idx < len(self.entries))]
        return min(idx_val_pairs, key = lambda x: x[1])[0]

    def _parent(self, i):
        return int(i / 2)
    
    def _left_child(self, i):
        return 2 * i
    
    def _right_child(self, i):
        return 2 * i + 1

    def _swim_down(self):
        def aux(i):
            if (i >= len(self.entries)):
                return

            left_child_idx = self._left_child(i)
            right_child_idx = self._right_child(i)
            self._swap(i, self._min(i, left_child_idx, right_child_idx))
            
            aux(left_child_idx)
            aux(right_child_idx)

        return aux(1)
    
    def _swim_up(self):
        def aux(i):
            if (i == 1):
                return

            parent_idx = self._parent(i)
            self._swap(parent_idx, self._min(i, parent_idx))
            
            aux(parent_idx)
        
        return aux(len(self.entries) - 1)
            
    def push(self, x: int) -> None:
        if (self._is_empty()):
            self.first = 1
        
        self.entries.append(x)
        # Now the last element may break the invariant of min stack
        self._swim_up()

        # print("#Pushed: {}".format(self.entries))
        
    def pop(self) -> None:
        # Empty stack: do nothing
        if (self._is_empty()):
            return

        self._swap(self.first, -1)
        self.entries.pop()
        # Now the top element may break the invariant of min stack
        self._swim_down()

        if (self._is_empty()):
            self.first = 0
        
        # print("!Popped: {}".format(self.entries))
    
    def top(self) -> int:
        return self.entries[self.first]

    def get_min(self) -> int:
        return self.top()