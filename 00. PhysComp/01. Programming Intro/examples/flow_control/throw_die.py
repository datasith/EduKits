#!/usr/bin/env python 
import random
x = random.randint(0,9)
x_str = str(x)+" "
if (x < 1):
    print(x_str + "is too small")
elif (x > 6):
    print(x_str + "is too big")
else:
    print(x_str + "is between 1 and 6")
