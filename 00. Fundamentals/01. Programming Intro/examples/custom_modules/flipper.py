#!/usr/bin/env python 
import random
num_to_string = ["Heads","Tails"]
def flip(times):
    for i in range(times):
        x = random.randint(0,1)
        print("Coin flip is "+num_to_string[x])
