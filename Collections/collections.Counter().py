# Enter your code here. Read input from STDIN. Print output to STDOUT

import collections
# import collections lib to store input elements

numofShoes = int(input())   # first input number of shoes
shoes = collections.Counter(map(int, input().split()))  # possible sizes
n = int(input())  # how many size and price

sumofshoes = 0

for i in range(n):
    size, price = map(int, input().split()) #n shoe
    if shoes[size]: 
        sumofshoes += price  # add prices
        shoes[size] -= 1     # do not add if added already

print (sumofshoes)
