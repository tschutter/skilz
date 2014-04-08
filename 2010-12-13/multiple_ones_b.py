#!/usr/bin/python
#
# Given any integer 0 <= n <= 10000 not [evenly] divisible by 2 or 5,
# find the number of digits in the smallest [integer] multiple of n
# that is a number which in decimal notation is a sequence of 1's.
#
# -9999 -> 0m1.611s
# -99999 -> 2m14.595s
#

import math, sys

def findNdigits(n):
    """Finds the number of digits in the smallest integer multiple of n.
       111 mod n = ((100 mod n) + (10 mod n) + (1 mod n)) mod n
       100 mod n = (10 * (10 mod n)) mod n
    """

    digmodulus = 1
    ndigits = 1
    modulus = 1 % n

    while modulus != 0:
      digmodulus = (digmodulus * 10) % n
      modulus = (modulus + digmodulus) % n
      ndigits += 1

    return ndigits

def main():
    n = int(sys.argv[1])
    if n % 2 == 0 or n % 5 == 0:
        print "ERROR: Invalid argument.  n must not be divisible by 2 or 5."
        sys.exit(1)

    if n < 0:
        maxdigits = 0
        for i in range(1, abs(n)):
            if i % 2 != 0 and i % 5 != 0:
                ndigits = findNdigits(i)
                print "%6d: %d" % (i, ndigits)
                if maxdigits < ndigits:
                    maxdigits = ndigits
                    maxdigitsi = i
        print "max ndigits = %d for n = %d" % (maxdigits, maxdigitsi)
    else:
        ndigits = findNdigits(n)
        print "%6d: %d" % (n, ndigits)

if __name__ == '__main__':
    main()
