#!/usr/bin/python
#
# Write a program in any language that takes a integer parameter n and
# outputs each number from 0 to n in random order where each number
# appears only once.
#
# timeit version
#

import random, sys, timeit
n = int(sys.argv[1]) + 1
a = range(n)
num = 1000000 / n
t = timeit.timeit(
    setup = "import random; from __main__ import a",
    stmt = "random.shuffle(a)",
    number = num,
)
print str(t / num) + " seconds to shuffle"
