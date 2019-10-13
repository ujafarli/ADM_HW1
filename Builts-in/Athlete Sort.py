# Enter your code here. Read input from STDIN. Print output to STDOUT

# 2 input integer
a, b = map(int, input().split()) 

new_list = []
for _ in range(b):  # b time input new lists
    new_list.append( map(float, input().split()) ) 

#zip each list and from 1 to length of new_list find sum/len
for i in zip(*new_list): 
    print( sum(i)/len(i) )
