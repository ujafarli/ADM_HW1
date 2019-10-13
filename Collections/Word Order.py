# Enter your code here. Read input from STDIN. Print output to STDOUT

# library and create OrderedDict words
from collections import OrderedDict
n = int(input())
words = OrderedDict()

# Take inputs
for _ in range(n):
    word = input()
    words.setdefault(word, 0)
# count words
    words[word] += 1
   
# print number of all words and each word
print(len(words))
print(*words.values())
