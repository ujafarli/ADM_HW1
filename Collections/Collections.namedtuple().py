from collections import namedtuple

# input int n and collection of input
(n, m) = (int(input()), input().split())

Grade = namedtuple('Grade', m)
marks = [int(Grade._make(input().split()).MARKS) for _ in range(n)]

# print avarage
print((sum(marks) / len(marks)))
