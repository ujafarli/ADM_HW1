# Enter your code here. Read input from STDIN. Print output to STDOUT

# Call library
from collections import defaultdict
d = defaultdict(list)

# input n and m
n, m = map(int,input().split())

# append input n's to collection d
for i in range(1, n + 1):
    d[input()].append(i) 

# append input m's to collection d
for j in range(m):
    index = input()  
    if d[index] == []:
        print(-1)
    else:
        print (*d[index])
