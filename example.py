#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 15:58:35 2018

@author: amanrana
"""

import numpy as np

#dd = np.array([1, 2, 3, 4, -8, -10], float)
#print dd[::-1]

#dd = [1,2, 3, 4, 5, 6, 7, 8, 9]
#num_arr = np.array(dd)
#reshape_val = num_arr.reshape((3,3))
#print reshape_val

import sys,numpy
if sys.version_info[0]>=3:
    raw_input=input
n,m=map(int,raw_input().split())
print n 
print m
a=[]
for _ in range(n):
	a.append([int(e) for e in raw_input().split()])
a=numpy.array(a)
print(numpy.transpose(a))
print(a.flatten())
