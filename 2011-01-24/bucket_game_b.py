#!/usr/bin/python
#
# You are one of two players in a game. Presented to both of you is a
# row of little buckets with a number of gold coins in each. The
# number of the coins in each bucket is known to both of
# you. Alternating turns, you get to choose a bucket from either end
# of the row and pocket the gold. However, you only can choose buckets
# at the ends and you always go first.
#
# Write a program that will maximize your take. Accept as input a file
# representing the bucket amounts in the form:
#    # # #
#
# As output, display the amount you were able to pocket.
#

import sys

def play(buckets):
    print str(buckets),
    myTake = 0
    myMove = True
    while len(buckets) > 0:
        if len(buckets) == 1:
            coins = buckets.pop(0)
            print "L",
        else:
            leftNetTake = buckets[0] - max(buckets[1], buckets[-1])
            rightNetTake = buckets[-1] - max(buckets[0], buckets[-2])

            if leftNetTake >= rightNetTake:
                coins = buckets.pop(0)
                print "L",
            else:
                coins = buckets.pop()
                print "R",

        if myMove:
            myTake += coins
        myMove = not myMove

    print str(myTake)

def main():
    with open(sys.argv[1]) as input:
        for line in input.readlines():
            buckets = map(int, line.split())
            play(buckets)

    return 0

if __name__ == '__main__':
    sys.exit(main())
