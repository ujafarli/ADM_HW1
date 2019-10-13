# input integer n and set s
n = int(input())
sets = set(map(int, input().split())) # len is n
 
# new input x and x time input commands
for i in range(int(input())):
    eval('sets.{0}({1})'.format(*input().split()+['']))

# print the sum of elements in the final set
print(sum(sets))
