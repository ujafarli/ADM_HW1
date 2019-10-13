import numpy

# I have tried to read input first but it shows error because of split() function
# This is the only way I could make it run(looked on internet)
print(str(numpy.eye(*map(int,input().split()))).replace('1',' 1').replace('0',' 0'))
