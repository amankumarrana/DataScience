#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 11:43:15 2018

@author: amanrana
"""

import numpy as np
import pandas as pd

data = pd.read_excel('Data/GLM_data/Table 2.8 Waist loss.xls')
print data[-5:] 
print data.tail(5)
