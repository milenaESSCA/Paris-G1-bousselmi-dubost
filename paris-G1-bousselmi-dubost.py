#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 16:37:41 2023

@author: milena
"""

print ("hello from milena") 
print ("hello my team from oumaima") 
print ("hello my team from chloe")

print ("test with branch")

2+2

print ("this code from my computer  - dubost")

# Read in the two files but call the data old and new and create columns to track
old = pd.read_excel('sample-address-1.xlsx', 'Sheet1', na_values=['NA'])
new = pd.read_excel('sample-address-2.xlsx', 'Sheet1', na_values=['NA'])
old['version'] = "old"
new['version'] = "new"
#check
old.head()
new.head()
