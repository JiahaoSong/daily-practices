def swap(arr, x, y):
    # arr[x], arr[y] = arr[y], arr[x] # this is super confusing, do not use it!
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp