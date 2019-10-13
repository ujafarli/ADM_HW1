# Enter your code here. Read input from STDIN. Print output to STDOUT

# as a loop take input and print result line by line
for _ in range(int(input())):
    a = input()
    # first set A
    A = set(input().split())
    b = input()
    # second set B
    B = set(input().split())
    # check subset with set.issucset()
    print(A.issubset(B))
