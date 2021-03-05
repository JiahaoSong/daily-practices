import sys

for line in sys.stdin.readlines():
    line = line.strip()
    raw_nums = [int(x) for x in line.split()]

    n = raw_nums[0]

    if (n > 0):
        print(sum(raw_nums[1:]))