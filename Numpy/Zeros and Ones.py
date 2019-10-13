import numpy

# Take input as a list of numbers
nums = list(map(int, input().split()))

# print zeros and print ones
print (numpy.zeros(nums, dtype = numpy.int))
print (numpy.ones(nums, dtype = numpy.int))


