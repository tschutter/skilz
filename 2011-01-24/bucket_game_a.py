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

Left = False
Right = True

def movesToStr(moves):
    result = ""
    for move in moves:
        if move == Left:
            result += "L "
        else:
            result += "R "
    return result

def determineMyTake(buckets, moves):
    myTake = 0
    leftIndex = 0
    rightIndex = len(buckets) - 1
    myMove = True
    for move in moves:
        if leftIndex > rightIndex:
            break
        if move == Left:
            coins = buckets[leftIndex]
            leftIndex += 1
        else:
            coins = buckets[rightIndex]
            rightIndex -= 1
        if myMove:
            myTake += coins
        myMove = not myMove

    return myTake

def play(buckets):
    nBuckets = len(buckets)
    nTries = 1
    for bucket in range(nBuckets - 1):
        nTries *= 2

    maxTake = -1
    maxMoves = []
    maxTryNum = -1

    for tryNum in range(nTries):
        # Build moves array.
        moves = []
        tryBits = tryNum
        for moveNum in range(nBuckets):
            moves.append(tryBits % 2 == 1)
            tryBits = tryBits // 2 # // is integer division

        # Try this set of moves
        myTake = determineMyTake(buckets, moves)
        if maxTake < myTake:
            maxTake = myTake
            maxMoves = moves
            maxTryNum = tryNum
        print str(buckets) + " " + movesToStr(moves) + str(myTake) + " it=" + str(tryNum)

    print str(buckets) + " " + movesToStr(maxMoves) + str(maxTake) + " maxit=" + str(maxTryNum)

def main():
    with open(sys.argv[1]) as input:
        for line in input.readlines():
            buckets = map(int, line.split())
            play(buckets)

    return 0

if __name__ == '__main__':
    sys.exit(main())
