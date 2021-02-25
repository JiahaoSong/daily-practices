class LinkedList:
    
    class Node:
        def __init__(self, x, next_node=None):
            self.val = x
            self.next = next_node

    def __init__(self) -> None:
        self.dummy = self.Node(0)

    def empty(self):
        return self.dummy is None
    
    def insert(self, x):
        def insert_aux(node):
            if (node is None):
                return self.Node(x)
            else:
                node.next = insert_aux(node.next)
                return node

        self.dummy.next = insert_aux(self.dummy.next)
    
    def delete(self, x):
        def delete_aux(node):
            if (node is None):
                return node
            elif (node.val == x):
                return node.next
            else:
                node.next = delete_aux(node.next)
                return node
        
        self.dummy.next = delete_aux(self.dummy.next)
    
    def reverse(self):
        """
        Reverse the whole linked list
        """
        def reverse_aux(node):
            next_node = node.next

            if (next_node is None):
                return node
            else:
                new_head = reverse_aux(next_node)
                next_node.next = node
                node.next = None

                return new_head
        
        self.dummy.next = reverse_aux(self.dummy.next)

    def reverse_k(self, k):
        """
        Reverse the sublist after k steps
        
        Note: If steps < k and reaches the end, do nothing.
        """
        def reverse_aux(node, count):
            pre_node = None
            cur_node = node
            next_node = None

            while (count > 0):
                next_node = cur_node.next
                cur_node.next = pre_node
                pre_node = cur_node
                cur_node = next_node

                count -= 1
            
            return pre_node
        
        if (k <= 1):
            return

        pre = self.dummy
        cur = pre.next
        count = 0

        while (cur is not None):
            first = cur
            while (count < k and cur is not None):
                cur = cur.next
                count += 1
            
            if (count < k):
                return
            else:
                pre.next = reverse_aux(first, count)
                first.next = cur
                pre = first

            count = 0

    def print(self):
        arr = []
        p = self.dummy.next
        while (p is not None):
            arr.append(p.val)
            p = p.next

        print(arr)
            




    

