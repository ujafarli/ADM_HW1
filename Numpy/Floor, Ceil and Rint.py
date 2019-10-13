import numpy

numpy.set_printoptions(sign=' ')   # setting how to print
# take input array 
a = numpy.array(input().split(),float)

# print floor, ceil and rint
print(numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))

