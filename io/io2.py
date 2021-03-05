import sys 

n = int(sys.stdin.readline().strip())

for _ in range(n):
    line = sys.stdin.readline().strip()
    a, b = [int(x) for x in line.split()]
    print(a + b)