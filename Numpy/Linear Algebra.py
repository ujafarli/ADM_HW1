import numpy

# first line take input m
m = int(input())

# second line take input array in a range of m
a=numpy.array([input().split() for _ in range(m)],float)

# Set print options
numpy.set_printoptions(legacy='1.13')

# Use numpy Linear Algebra function on array a
print(numpy.linalg.det(a))
