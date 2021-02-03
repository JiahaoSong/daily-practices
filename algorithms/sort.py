from random import randint

from algorithms.utils import swap

SORTING_THRESH = 100

def insertion_sort(arr):
    """
    O(N^2)
    """
    for i in range(len(arr)):
        for j in range(i, 0, -1):
            if (arr[j - 1] > arr[j]):
                swap(arr, j - 1, j)
    
def quicksort(arr):
    """
    Divide and conquer, E(T(N)) = O(NlogN) 
    
    Divide: the partition method
    Conquer: do nothing since they are sorted as a whole
    """
    def partition(start, end):
        """
        Invariant:
        for all pos < i, arr[pos] <= arr[i]
        for all pos > i, arr[pos] > arr[i]
        """
        # 1. Randomly choose a pivot, swap it with the first item
        rand_choice = randint(start, end)
        swap(arr, end, rand_choice)

        # 2. Scan the array, swap them if *the invariant breaks*
        i = start # position where the invariant should hold
        for j in range(start, end):
            if (arr[j] <= arr[end]):
                swap(arr, i, j)
                i += 1

        # 3. Swap the last item with the i-th item
        swap(arr, i, end)

        return i
    
    def aux(start, end):
        if (start < end):
            pivot = partition(start, end)
            aux(start, pivot - 1)
            aux(pivot + 1, end)
    
    return aux(0, len(arr) - 1)


def sort(arr):
    if (len(arr) <= SORTING_THRESH):
        insertion_sort(arr)
    else:
        quicksort(arr)

        

        