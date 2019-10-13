# Take 2 input sets A and B
input()
A = set(map(int, input().split()))
input()
B = set(map(int, input().split()))

# Print difference by symmetric_difference
print(len(A.symmetric_difference(B)))
