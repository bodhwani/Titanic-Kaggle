#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 22:27:50 2017

@author: Vinit
"""

import numpy as np
import pandas as pd
from IPython.display import display # Allows the use of display() for DataFrames

# Import supplementary visualizations code visuals.py
import visuals as vs

# Pretty display for notebooks

# Load the dataset
in_file = 'test.csv'
full_data = pd.read_csv(in_file)
display(full_data)