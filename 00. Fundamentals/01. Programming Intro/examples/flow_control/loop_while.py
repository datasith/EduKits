#!/usr/bin/env python 
import random
x = 1
while (x != 0):
    x_str = str(x) + " "
    print(x_str + "is not 0")
    x = random.randint(0,3)
print("is " + x_str + "== 0?")
