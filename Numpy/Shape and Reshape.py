import numpy

import numpy as np

# Take input as list of integers
lis = list(map(int,input().split()))

# Using numpy array functions, shape it 3x3 matrix
arr = np.array(lis)
arr.shape=(3,3)
print(arr)


