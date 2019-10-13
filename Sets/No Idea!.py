n, m = map(int,input().split())
l = input().split(' ')
A = set(input().split(' '))
B = set(input().split(' '))
output = 0

for i in l:
    if i in A:
        output += 1
    if i in B:
        output -= 1
print(output)
