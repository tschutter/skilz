#!/usr/bin/python
#
# Given an integer number (say, a 32 bit integer number), write code
# to count the number of bits set (1s) that comprise the number.  For
# instance: 87338 (decimal) = 10101010100101010 (binary) in which
# there are 8 bits set.  No twists this time and as before, there is
# no language restriction.
#

import sys

def main():
    number = int(sys.argv[1])
    if number < 0:
        number = -number
    #import gmpy
    #print gmpy.digits(number, 2)

    nsetbits = 0
    while number != 0:
        if number % 2 == 1:
            nsetbits += 1
        number = number // 2 # // is integer division

    print "Number of bits set = %i" % nsetbits

    return 0

if __name__ == '__main__':
    sys.exit(main())
