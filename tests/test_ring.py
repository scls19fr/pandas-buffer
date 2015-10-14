#!/usr/bin/env python

from pandas_buffer import RingBuffer
import pandas as pd

def test_ring():
    N = 10
    #ring = RingBuffer(size_max=N, default_value=0.0, dtype=float, overflow=print_overflow)
    assert False