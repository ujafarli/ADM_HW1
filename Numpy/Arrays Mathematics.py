import numpy as np

x1, x2 = map(int, input().split())

# get input array
a, b = (np.array([input().split() for _ in range(x1)], dtype=int) for _ in range(2))

# print arithmetic operations on array
print(a+b, a-b, a*b, a//b, a%b, a**b, sep='\n')
