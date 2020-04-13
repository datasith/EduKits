#!/usr/bin/env python
from Encoder import Encoder
import time

encoder = Encoder(38, 40) 
t = time.time()
while True:
    cycles, dir_flag = encoder.get_cycles()
    if dir_flag:
        t = time.time()
        print "Wheel changed directions!"
        continue
    if cycles != 0:
        dt = time.time()-t
        t = time.time()
        print "Completed cycle in %f seconds" % dt
