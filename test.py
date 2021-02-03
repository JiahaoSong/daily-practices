import math
import sys 

from algorithms.binary_search import binary_search, search_in_rotated_sorted_array
from algorithms.sort import sort
from data_structures.min_heap import MinHeap
from data_structures.bst import BST


def sorting_test():
    A = [-1, 0, 1, 2, 3, -100, 100]
    sort(A)
    print(A)


def binary_search_test():
    A = [-100, -1, 0, 1, 2, 3, 100]
    print("A: {}".format(A))
    print("-100 at [{}]".format(binary_search(A, -100)))
    print("10000 at [{}]".format(binary_search(A, 10000)))
    print("4 at [{}]".format(binary_search(A, 4)))
    print("0 at [{}]".format(binary_search(A, 0)))

def rotated_sorted_array_binary_search_test():
    A = [2, 3, 100, -100, -1, 0, 1]
    print("A: {}".format(A))
    print("-100 at [{}]".format(binary_search(A, -100)))
    print("10000 at [{}]".format(binary_search(A, 10000)))
    print("4 at [{}]".format(binary_search(A, 4)))
    print("0 at [{}]".format(binary_search(A, 0)))


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
    print("#Number of nodes: [{}]".format(bst_object.size()))
    print("#Height of this tree is [{}]".format(bst_object.height()))

    search_target = 5
    depth = bst_object.depth(search_target)
    print("#Depth from the {} to the {} is [{}]".format(bst_object.root.val, search_target, depth))

    # 2. Deletion sanity check (including three cases, that is, 0, 1, 2 children)
    for delete_target in my_numbers:
        print("!Delete [{}]".format(delete_target))
        bst_object.delete(delete_target)
        bst_object.print()
        print("#Number of nodes: [{}]".format(bst_object.size()))

        if (bst_object.empty()):
            break

        depth = bst_object.depth(search_target)
        print("#Depth from the {} to the {} is [{}]".format(bst_object.root.val, search_target, depth))