import numpy

# input n and m first
# then take input list in a range of x1
x1, x2 = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(x2)]

# returns the prod sum of array elements over a given axis
print(numpy.prod(numpy.sum(arr,axis=0)))
