import math
import sys 

from algorithms.binary_search import binary_search, search_in_rotated_sorted_array
from algorithms.knapsack import knapsack
from algorithms.shortest_path import my_dijkstra, generate_path, built_in_dijkstra
from algorithms.sort import sort

from data_structures.bst import BST
from data_structures.disjoint_sets import DisjointSets
from data_structures.graph import Graph
from data_structures.linked_list import LinkedList
from data_structures.min_heap import MinHeap
from data_structures.priority_queue import PriorityQueue

def built_in_dijkstra_test():
    g = Graph(7)
    g.add_edge(0, 1, 2);
    g.add_edge(0, 2, 1);

    g.add_edge(1, 2, 5);
    g.add_edge(1, 3, 11);
    g.add_edge(1, 4, 3);

    g.add_edge(2, 5, 15);

    g.add_edge(3, 4, 2);

    g.add_edge(4, 2, 1);
    g.add_edge(4, 5, 4);
    g.add_edge(4, 6, 5);

    g.add_edge(6, 3, 1);
    g.add_edge(6, 5, 1);

    print("#Vertices: {}\n#Edges: {}".format(
          g.vertex_size(),
          g.edge_size()
    ))

    start = 0;
    goal = 6;
    dist_to, edge_to = built_in_dijkstra(g, start)

    # This should be 10
    print("The shortest path from 0 to 6 is {}".format(
          dist_to[goal]))
    print(dist_to)
    # This should be 0, 1, 4, 6
    print("The path is {}".format(
          generate_path(edge_to, start, goal)
    ))


def my_dijkstra_test():
    g = Graph(7)
    g.add_edge(0, 1, 2);
    g.add_edge(0, 2, 1);

    g.add_edge(1, 2, 5);
    g.add_edge(1, 3, 11);
    g.add_edge(1, 4, 3);

    g.add_edge(2, 5, 15);

    g.add_edge(3, 4, 2);

    g.add_edge(4, 2, 1);
    g.add_edge(4, 5, 4);
    g.add_edge(4, 6, 5);

    g.add_edge(6, 3, 1);
    g.add_edge(6, 5, 1);

    print("#Vertices: {}\n#Edges: {}".format(
          g.vertex_size(),
          g.edge_size()
    ))

    start = 0;
    goal = 6;
    dist_to, edge_to = my_dijkstra(g, start)

    # This should be 10
    print("The shortest path from 0 to 6 is {}".format(
          dist_to[goal]))
    print(dist_to)
    # This should be 0, 1, 4, 6
    print("The path is {}".format(
          generate_path(edge_to, start, goal)
    ))
    

def priority_queue_test():
    pq = PriorityQueue()
    A = [(1000, "a big nubmer"), 
         (30, "has"), (15, "a"), (90, "priority"), 
         (100, "queue"), (30, "same priority as 'has'")]

    for p, item in A:
        print("!Pushing ({}, {})...".format(p, item))
        pq.push(p, item)
    print("#Current size of the PQ: {}".format(pq.size()))

    for i in range(1, pq.size() + 1):
        print(pq.pq[i])

    print("!Changing the priority of 'has' from 30 to 45...")
    pq.change_priority(45, "has")
    print("!Changing the priority of 'priority' from 90 to 0...")
    pq.change_priority(0, "priority")

    for _ in range(len(A)):
        print(pq.pop())


def knapsack_test():
    w = 50
    ws = [10, 20, 30]
    vs = [60, 100, 120]

    print("Maximum value is {}.".format(knapsack(w, ws, vs)))
    
def disjoint_sets_test():
    ds = DisjointSets(1000000)
    ds.union(1, 3)
    ds.union(1, 5)
    ds.union(5, 7)
    ds.union(3, 5)

    print("({}) 1 connected to 7.".format(ds.is_connected(1, 7)))
    print("#sets = {}".format(ds.size()))

def linkedlist_test():
    A = [-1, 0, 1, 2, 3, -100, 100]
    l = LinkedList()
    
    for x in A:
        l.insert(x)

    print("#Printed linkedlist:")
    l.print()

    print("!Deleting {}...".format(100))
    l.delete(100)
    print("!Deleting {}...".format(-111))
    l.delete(-111)
    print("#Printed linkedlist:")
    l.print()

    print("!Reversing the whole list...")
    l.reverse()
    print("#Printed linkedlist:")
    l.print()

    print("!Reversing the list by 2...")
    l.reverse_k(2)
    print("#Printed linkedlist:")
    l.print()

    print("!Reversing the list by 1... (should be itself)")
    l.reverse_k(1)
    print("#Printed linkedlist:")
    l.print()

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