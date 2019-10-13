import numpy as np

# input 2 input arrays
A =np.array([list(map(int,input().split()))])
B =np.array([list(map(int,input().split()))])

# find inner and outer product of array A and B
print(np.inner(A,B)[0][0], np.outer(A,B), sep='\n')
