import sys 

from algorithms.sort import sort
from data_structures.min_heap import MinHeap
from data_structures.bst import BST


def sorting_test():
    A = [-1, 0, 1, 2, 3, -100, 100]
    sort(A)
    print(A)


def min_heap_test():
    min_heap = MinHeap()
    my_numbers = [-2, 0, -3, 100, -100]
    for number in my_numbers:
        print("!Push {}".format(number))
        min_heap.push(number)
        print("#Current min heap: {}".format(min_heap.entries))
    
    print("#Current min is {}".format(min_heap.get_min()))

    pop_times = 3
    for _ in range(pop_times):
        print("!Pop")
        min_heap.pop()
        print("#Current min heap: {}".format(min_heap.entries))
    
    print("#Top element: {}".format(min_heap.top()))
    print("#Current min is {}".format(min_heap.get_min()))

def bst_test():
    bst_object = BST()
    my_numbers = [7, 9, 8, 4, 5, 5, 10, 2]
    """
                7
        4               9
    2       5       8      10
                    
    """
    print("#Original numbers are {}".format(my_numbers))
    
    # 1. Insertion sanity check (with duplicate values)
    for number in my_numbers:
        print("!Insert [{}]".format(number))
        bst_object.insert(number)
    
    bst_object.print()
    print("#Height of this tree is [{}]".format(bst_object.height()))

    search_target = 5
    depth = bst_object.depth(search_target)
    print("#Depth from the {} to the {} is [{}]".format(bst_object.root.val, search_target, depth))

    # 2. Deletion sanity check (including three cases, that is, 0, 1, 2 children)
    for delete_target in my_numbers:
        print("!Delete [{}]".format(delete_target))
        bst_object.delete(delete_target)
        bst_object.print()

        if (bst_object.empty()):
            break

        depth = bst_object.depth(search_target)
        print("#Depth from the {} to the {} is [{}]".format(bst_object.root.val, search_target, depth))
        

def main():
    # sorting_test()
    # min_heap_test()
    bst_test()

if (__name__ == "__main__"):
    main()