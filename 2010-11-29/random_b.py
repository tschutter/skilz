#!/usr/bin/python
#
# Write a program in any language that takes a integer parameter n and
# outputs each number from 0 to n in random order where each number
# appears only once.
#

import random, sys
n = int(sys.argv[1]) + 1
a = range(n)
random.shuffle(a)
print a
if n > 2080:
    print "WARNING: Not all permutations are possible."
    print "WARNING: %s! > 2**19937-1 (MersenneTwister period)" % n
