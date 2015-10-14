#!/usr/bin/env python

from pandas_buffer import RingBuffer
import numpy as np

N = 5

ring = RingBuffer(N, 
    columns=['dt', 'sensor01', 'sensor02', 'sensor03'], 
)

print(ring)

ring.append(1.00, 1.01, 1.02, 1.03)
print(ring)

ring.append(2.00, 2.01, 2.02, 2.03, 2.04, 2.05, 2.06) # should warn about losing (2.04, 2.05, 2.06)
print(ring)

ring.append(dt=3.00, sensor01=3.01, sensor02=3.02, sensor03=3.03)
print(ring)

ring.append(dt=4.00, sensor01=4.01, sensor02=4.02, sensor03=4.03, sensor04=4.04) # ToDo: should warn about losing (4.04)
print(ring)

ring.append(dt=5.00, sensor01=5.01, sensor02=5.02, sensor03=5.03)
print(ring)

ring.append(dt=6.00, sensor01=6.01, sensor02=6.02, sensor03=6.03)
print(ring)


#print(ring['sensor01'][::-1])

"""
<RingBuffer
    all:
  dt sensor01 sensor02 sensor03
0  6     6.01     6.02     7.03
1  5     5.01     5.02     5.03
2  4     4.01     4.02     4.03
3  3     3.01     3.02     3.03
4  2     2.01     2.02     2.03

    partial:
  dt sensor01 sensor02 sensor03
0  6     6.01     6.02     7.03
1  5     5.01     5.02     5.03
2  4     4.01     4.02     4.03
3  3     3.01     3.02     3.03
4  2     2.01     2.02     2.03

    size/size_max: 5 / 5
>


A ResampledRingBuffer need also to be created
resample with mean value or with OHLCV

we need to define a timeframe (int or timedelta or Pandas offset ?)

For each sensor we can get a dataframe with OHLCV or mean&V
V=Volume being the number of acquisition in a timeframe


A Panel might be an appropriate data structure.


"""