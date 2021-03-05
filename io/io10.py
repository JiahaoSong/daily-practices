from sys import stdin

for line in stdin.readlines():
    strs = line.strip().split(",")
    print(",".join(sorted(strs)))
