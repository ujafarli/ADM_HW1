import numpy

# first line float inputs as a list(not integer)
n = list(map(float,input().split()));

# second line one input m
m = input();

# print polyval from numpy library
print(numpy.polyval(n,int(m)));

