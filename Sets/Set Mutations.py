# Enter your code here. Read input from STDIN. Print output to STDOUT
# Take inputs
input()
X1 = set(map(int, input().split()))
N = int(input())

# according to the command make oparations
for i in range(N):
    command = (input().split())[0]
    X2 = set(map(int, input().split()))
    if(command == "intersection_update"):
        X1.intersection_update(X2)
    elif(command == "update"):
        X1.update(X2)
    elif(command == "symmetric_difference_update"):
        X1.symmetric_difference_update(X2)
    elif(command == "difference_update"):
        X1.difference_update(X2)

print(sum(X1))
