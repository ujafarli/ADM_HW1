# Enter your code here. Read input from STDIN. Print output to STDOUT

n = input()
s = set()

# Add to the set
for i in range(int(n)):
    s.add(input())

# print the lenght
print (len(s))
