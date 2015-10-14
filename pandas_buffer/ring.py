#!/usr/bin/env python

import numpy as np
import pandas as pd
import warnings

class RingBuffer(object):
    def __init__(self, size_max, columns=['data']):
        """initialization"""
        self.clear(size_max, columns)

    def clear(self, size_max=None, columns=None):
        """clear ring"""
        if size_max is not None:
            self.size_max = size_max

        if columns is not None:
            self._columns = columns

        self._data = pd.DataFrame(columns=self._columns, index=np.arange(self.size_max))
        self._Ncols = len(self._data.columns)

        self.size = 0
        
        self.full = False
        self.append = self._append_not_full        

    def _append_not_full(self, *args, **kwargs):
        """append an element"""
        self._data = self._data.shift(1)

        self._put_data(*args, **kwargs)

        self.size += 1
                
        if self.size == self.size_max:
            self.full  = True
            self.append = self._append_full
            self.overflow(self)

    def _put_data(self, *args, **kwargs):
        if len(args)>0:
            if len(args)==self._Ncols:
                self._data.iloc[0] = args
            elif len(args)>self._Ncols:
                self._data.iloc[0] = args[0:self._Ncols]
                warnings.warn("Losing some data")
                warnings.warn(str(args[self._Ncols:]))
        else:
            if len(kwargs)>0:
                self._data.iloc[0] = kwargs
            else:
                raise NotImplementedError("Nothing to append")

    def _append_full(self, *args, **kwargs):
        """append an element when buffer is full"""
        self._data = self._data.shift(1)
        self._put_data(*args, **kwargs)

    @property
    def columns(self):
        """return a list of columns"""
        return self._data.columns

    @property
    def all(self):
        """return a list of elements from the oldest to the newest (len: size_max)"""
        return self._data
        
    @property
    def partial(self):
        """return a list of elements from the oldest to the newest (len: size)"""
        return self.all[0:self.size]

    #def view(self, *args, **kwargs):
    #    return self.partial[::-1].values.view(*args, **kwargs)
    
    def __len__(self):
        """return size (not size_max)"""
        return self.size

    def __getitem__(self, *args, **kwargs):
        """get element"""
        return self._data.__getitem__(*args, **kwargs)

    def __repr__(self):
        """return string representation"""
        s = """<%s
    all:
%s

    partial:
%s

    size/size_max: %d / %d
>""" % (self.__class__.__name__, 
    self.all.__repr__(), 
    self.partial.__repr__(),
    self.size, self.size_max
)
        return s

    def overflow(self, *args, **kwargs):
        return
