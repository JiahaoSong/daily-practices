import sys 

for line in sys.stdin.readlines():
    line = line.strip()
    a, b = [int(x) for x in line.split()]
    print(a + b)