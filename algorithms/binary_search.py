"""
Variants of binary search 
"""

def binary_search(nums, x):
    """
    Binary search.
    Time complexity: O(logN)
    """
    def aux(lo, hi):
        # Base case: target not found
        if (lo > hi):
            return -1

        mid = int((lo + hi) / 2)
        if (x < nums[mid]):
            return aux(lo, mid - 1)
        elif (x > nums[mid]):
            return aux(mid + 1, hi)
        else:
            # Value's been found
            return mid
    
    return aux(0, len(nums) - 1)

def search_in_rotated_sorted_array(nums, x):
    """
    Suppose nums contains distinct numbers.

    Time complexity: O(logN)
    Invariant: at least one side (of mid) will be in order.
    Notice that lo, hi and mid are all in the base cases.
    """
    def search_aux(lo, hi):
        if (lo > hi):
            return -1
        
        mid = (lo + hi) // 2
        if (x == nums[mid]):
            return mid
        elif (x == nums[lo]):
            return lo
        elif (x == nums[hi]):
            return hi
        else:
            if (nums[lo] < nums[mid]):
                if (nums[lo] < x and x < nums[hi]):
                    return search_aux(lo, mid - 1)
                else:
                    return search_aux(mid + 1, hi)
            else:
                if (nums[mid] < x and x < nums[hi]):
                    return search_aux(mid + 1, hi)
                else:
                    return search_aux(lo, mid - 1)
    
    return search_aux(0, len(nums) - 1)
