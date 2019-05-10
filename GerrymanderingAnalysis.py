#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 06:32:11 2018
@author: Abishek Varadarajan
"""

# Multiple Linear Regression
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('IS733_GerryMandering multiple reg.csv')
X = dataset.iloc[:, [0,1,2,3,4,5]].values
y = dataset.iloc[:, [-1,-2]].values
