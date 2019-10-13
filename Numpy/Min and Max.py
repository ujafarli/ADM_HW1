import numpy as np

# Standart process of reading input as in the other problems
x1, x2 = map(int, input().split())
a = np.array([input().split() for _ in range(x1)], int)

# compute min and then print max
print(a.min(axis=1).max())


