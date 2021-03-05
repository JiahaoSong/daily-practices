import sys 

for line in sys.stdin.readlines():
    line = line.strip()
    arr = [int(x) for x in line.split()]

    print(sum(arr))