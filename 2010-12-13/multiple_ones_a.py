#!/usr/bin/python
#
# Given any integer 0 <= n <= 10000 not [evenly] divisible by 2 or 5,
# find the number of digits in the smallest [integer] multiple of n
# that is a number which in decimal notation is a sequence of 1's.
#

import sys

# Build array [ 0, 1, 11, 111, 1111, etc. ]
maxdigits = 10000 # known a-priori, not directly related to range of n
answer = 0
answers = [ 0 ]
for ndigits in range(1, maxdigits):
    answer = answer * 10 + 1
    answers.append(answer)

def findNdigits(n):
    """Finds the number of digits in the smallest integer multiple of n."""
    for ndigits in range(1, maxdigits):
        if answers[ndigits] >= n and answers[ndigits] % n == 0:
            return ndigits
    print "ERROR: maxdigits too small."
    sys.exit(1)

def main():
    n = long(sys.argv[1])
    if n % 2 == 0 or n % 5 == 0:
        print "ERROR: Invalid argument.  n must not be divisible by 2 or 5."
        sys.exit(1)

    if n < 0:
        maxdigits = 0
        for i in range(1, abs(n)):
            if i % 2 != 0 and i % 5 != 0:
                ndigits = findNdigits(i)
                print "%+6d: %d" % (i, ndigits)
                if maxdigits < ndigits:
                    maxdigits = ndigits
                    maxdigitsi = i
        print "max ndigits = %d for n = %d" % (maxdigits, maxdigitsi)
    else:
        ndigits = findNdigits(n)
        print "%+6s: %d" % (n, ndigits)

if __name__ == '__main__':
    main()
