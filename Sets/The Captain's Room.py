# Enter your code here. Read input from STDIN. Print output to STDOUT

# Take input integer n and set of integers s
n = int(input())
s = list(map(int, input().split()))
lists = set(s)

# have n-1*captains left so divide
total = sum(lists) * n - sum(s)
print(total // (n-1))
