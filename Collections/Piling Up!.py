# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import deque

t = int(input())
for i in range(t):
    input()
    d = deque(list(map(int, input().split())))
    ls = []
    Y = 1
    while len(d) !=0:
        actual = d[0]
        what = 1
        if d[-1] > actual:
            what = 0
        if what == 1:
            d.pop()
        else:
            d.popleft()
        if ls  == []:
            ls.append(actual)
        else:
            if ls[-1] < actual:
                Y = 0
                break
            else:
                ls.append(actual)
    
    if Y == 1:
        print("Yes")
    else:
        print("No")
            
