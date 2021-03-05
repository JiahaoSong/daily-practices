import sys 

for line in sys.stdin.readlines():
    line = line.strip()
    raw_nums = [int(x) for x in line.split()]
    n = raw_nums[0]
    arr = raw_nums[1:]

    print(sum(arr))