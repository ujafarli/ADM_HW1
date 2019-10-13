import numpy

# input integer and 2 input arrays
a=int(input())
array1=numpy.array([list(map(int,input().split())) for _ in range(a)])
array2=numpy.array([list(map(int,input().split())) for _ in range(a)])

# find matrix multiplication with numpy.dot
print(numpy.dot(array1,array2))

