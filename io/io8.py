import sys 

n = int(sys.stdin.readline())
s = sys.stdin.readline()

strs = s.strip().split()
print(" ".join(sorted(strs)))
