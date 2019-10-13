# Enter your code here. Read input from STDIN. Print output to STDOUT

# Take 2 input sets A and B
input()
A = set(map(int, input().split()))
input()
B = set(map(int, input().split()))

# Print difference by set.difference
print(len(A.difference(B)))
