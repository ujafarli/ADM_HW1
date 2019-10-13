# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

d = OrderedDict()

# take inputs and for each item + item_price
for _ in range(int(input())):
    item_name, item_extra, item_price = input().rpartition(' ')
    d[item_name] = d.get(item_name, 0) + int(item_price)

# then print each item with price
for item_name, item_price in d.items():
    print(item_name, item_price)
