def binary_search(arr, x):
    """
    A binary search function with O(logN) complexity
    """
    def aux(start, end):
        # Base case: target not found
        if (start > end):
            return -1

        mid = int((start + end) / 2)
        if (x < arr[mid]):
            return aux(start, mid - 1)
        elif (x > arr[mid]):
            return aux(mid + 1, end)
        else:
            # Value's been found
            return mid
    
    return aux(0, len(arr) - 1)