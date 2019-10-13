# Enter your code here. Read input from STDIN. Print output to STDOUT

# read library and create deque d
from collections import deque
d = deque()

# Take an input deque
for _ in range(int(input())):
    method_name, *inputs = input().split()
    getattr(d, method_name)(*inputs)

print(*d)
