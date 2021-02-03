import math

class BST:

    class Node:
        """
        Node

        val: stored value in the node
        left: left subtree
        right: right subtree
        """
        def __init__(self, val = None) -> None:
            self.val = val
            self.left = None
            self.right = None
            

    def __init__(self) -> None:
        self.root = None
        self.n = 0
    

    def empty(self):
        return self.root is None


    def size(self):
        return self.n


    def height(self):
        """
        Returns the height of the BST, also the height of the root node
        """
        def height_aux(node):
            if (node is None):
                return -1
            else:
                left_tree_height = height_aux(node.left)
                right_tree_height = height_aux(node.right)
                return max(left_tree_height, right_tree_height) + 1
        
        return height_aux(self.root)


    def search(self, x):
        def search_aux(node):
            if (node is None):
                return False
            elif (x < node.val):
                return search_aux(node.left)
            elif (x > node.val):
                return search_aux(node.right)
            else:
                return True
        
        return search_aux(self.root)


    def depth(self, target):
        """
        Returns the depth from the root node to the target node.
        The depth will be -1 if the target is not found.
        """
        def depth_aux(node):
            if (node is None):
                return -1
            elif (target == node.val):
                return 0
            elif (target < node.val):
                return depth_aux(node.left) + 1
            else:
                return depth_aux(node.right) + 1
        
        return depth_aux(self.root) if self.search(target) else -1
            
    def insert(self, x):
        def insert_aux(node) -> object:
            if (node is None):
                self.n += 1
                return self.Node(x)
            elif (x < node.val):
                node.left = insert_aux(node.left)
            elif (x > node.val):
                node.right = insert_aux(node.right)
            else:
                # Duplicate value found
                pass

            return node
        
        self.root = insert_aux(self.root)


    def delete(self, x):
        def swap(node_x, node_y):
            temp = node_x.val
            node_x.val = node_y.val
            node_y.val = temp

        def transplant(node, source_node) -> object:
            """
            Transplants the target (`node`) with the current node (`source_node`)
            while maintaining the BST property.
            """
            if (node.left is None):
                swap(node, source_node)
                return node.right # prune this node and switch to its right subtree
            else:
                node.left = transplant(node.left, source_node)
                return node
 
        def delete_aux(node) -> object:
            if (node is None):
                return None
            elif (x == node.val):
                # Target found, prepare to delete
                self.n -= 1

                if ((node.left is None) and (node.right is None)):
                    return None
                elif (node.left is None):
                    # Right subtree only, cut and paste 
                    return node.right
                elif(node.right is None):
                    # Left subtree only, cut and paste
                    return node.left
                else:
                    # Both of children exist
                    # Find the successor (candidate) in the right subtree
                    # (predecessor should do the same job) and
                    # do the transplantation
                    node.right = transplant(node.right, node)
                    return node
            elif (x < node.val):
                node.left = delete_aux(node.left)
            else:
                node.right = delete_aux(node.right)

            return node
        
        self.root = delete_aux(self.root)
        
            
    def print(self):
        """
        Prints out the traverse of this tree
        """
        pre_order_results = []
        in_order_results = []
        post_order_results = []

        def pre_order_traverse(node):
            if (node is None):
                return
            pre_order_results.append(node.val)
            pre_order_traverse(node.left)
            pre_order_traverse(node.right)

        def in_order_traverse(node):
            if (node is None):
                return
            else:
                in_order_traverse(node.left)
                in_order_results.append(node.val)
                in_order_traverse(node.right)
        
        def post_order_traverse(node):
            if (node is None):
                return
            post_order_traverse(node.left)
            post_order_traverse(node.right)
            post_order_results.append(node.val)

        pre_order_traverse(self.root)
        in_order_traverse(self.root)

        print("#Pre-order traverse (sorted) output is: {}".format(pre_order_results))
        print("#In-order traverse (sorted) output is: {}".format(in_order_results))
