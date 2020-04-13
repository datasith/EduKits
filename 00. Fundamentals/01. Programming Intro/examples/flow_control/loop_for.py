#!/usr/bin/env python 
import random
x = 1
seq = [0,1,2,3,4,5,6,7,8,9]
for i in seq:
    x = random.randint(0,1)
    x_str = str(x)
    print("x_str" + " is " + x_str)
print("Done!")
