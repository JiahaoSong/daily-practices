from sys import stdin

for line in stdin.readlines():
    line = line.strip()
    a, b = [int(x) for x in line.split()]
    print(a + b)