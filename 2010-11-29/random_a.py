#!/usr/bin/python
#
# Write a program in any language that takes a integer parameter n and
# outputs each number from 0 to n in random order where each number
# appears only once.
#
# In this version I have randomly chosen the sorted order.
#

import random, sys
n = int(sys.argv[1]) + 1
print range(n)
