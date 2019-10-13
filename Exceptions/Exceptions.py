# Enter your code here. Read input from STDIN. Print output to STDOUT

test = int(input())

for i in range(test):
    x1,x2 = input().split()
        
    try:
        print (int(x1)//int(x2))
# division by zero can be 2 exception: ZeroDivisionError, ValueError
    except (ZeroDivisionError, ValueError) as e:
        print ("Error Code:", e)

