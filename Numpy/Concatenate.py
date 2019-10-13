import numpy

import numpy as np
a, b, c = map(int,input().split())

# a time input first array 
first_arr = np.array([input().split() for _ in range(a)],int)

# b time input second array
second_arr = np.array([input().split() for _ in range(b)],int)

# Use concatenate function
print(np.concatenate((first_arr, second_arr)))
