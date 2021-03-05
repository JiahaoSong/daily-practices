import sys

groups = int(sys.stdin.readline().strip())

for _ in range(groups):
    line = sys.stdin.readline().strip()
    raw_nums = [int(x) for x in line.split()]

    n = raw_nums[0]

    if (n > 0):
        print(sum(raw_nums[1:]))