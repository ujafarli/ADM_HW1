import numpy as np

np.set_printoptions(legacy='1.13')
# take input array 
x1, x2 = map(int, input().split())
a = np.array([input().split() for _ in range(x1)], int)

# Print Variance, mean and standart deviation by calculating numpy
print(np.mean(a, axis = 1))
print(np.var(a, axis = 0))
print(np.std(a))
