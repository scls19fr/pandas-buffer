#!/usr/bin/env python

from pandas_buffer import RingBuffer
import numpy as np

N = 5

ring = RingBuffer(N, 
    columns=['sensor01', 'sensor02', 'sensor03'], 
)

print(ring)

ring.append(1.01, 1.02, 1.03)
print(ring)

ring.append(2.01, 2.02, 2.03, 2.04, 2.05, 2.06) # should warn about losing (2.04, 2.05, 2.06)
print(ring)

ring.append(sensor01=3.01, sensor02=3.02, sensor03=3.03)
print(ring)

ring.append(sensor01=4.01, sensor02=4.02, sensor03=4.03, sensor04=4.04) # ToDo: should warn about losing (4.04)
print(ring)

ring.append(sensor01=5.01, sensor02=5.02, sensor03=5.03)
print(ring)

ring.append(sensor01=6.01, sensor02=6.02, sensor03=7.03)
print(ring)
