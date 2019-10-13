#!/bin/python3

import math
import os
import random
import re
import sys


num = int(input())

# If input is odd, then Weird
if (num % 2 !=0) :
    print("Weird")
# If input is even and till 5, then Not Weird
elif (num >= 2 and num <= 5) :
    print("Not Weird")
# If input is even and between 5 and 20, then Weird
elif (num>=6 and num <=20):
    print("Weird")
#other cases
else:
    print("Not Weird")

