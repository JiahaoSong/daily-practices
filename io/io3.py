import sys

for line in sys.stdin.readlines():
    line = line.strip()
    if (line == "0 0"):
        break
    a, b = [int(x) for x in line.split()]
    print(a + b)