#!/usr/bin/env python 
import random
x = random.randint(0,9)
x_str = str(x)+" "
if ((x%2) == 0):
    print(x_str + "is even")
else:
    print(x_str + "is odd")
