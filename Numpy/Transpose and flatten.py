import numpy

a, b = map(int, input().split())
array = numpy.array([input().strip().split() for _ in range(a)], int)

# Here I call transpose and flatten function from numpy library
print (array.transpose())
print (array.flatten())


