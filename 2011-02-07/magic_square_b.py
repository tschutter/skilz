#!/usr/bin/python
#
# A magic square is a an n x n array of numbers consist of the
# integers 1, 2, ..., n^2 arranged so that the sum of the numbers in
# every row, column and main diagonals is the same. For example, in a
# 4 x 4 square the numbers are 1, 2, ..., 16 and could be arranged
# thusly to create the sum 34:
#
# 16  3  2 13
#  5 10 11  8
#  9  6  7 12
#  4 15 14  1
#
# For the first part, write a program that can produce magic squares
# with values of n from 4 to, say, 28 (inclusively).
#

# One method I learnt was to start with '1' in the centre of the bottom line and go 1 step diagonally down and right, unless that space was filled, in which case go up one.
#
# 1. Start by filling the magic square with the numbers in order, starting in the upper left corner with one, going across to the right, and beginning a new row when you reach the end.
# 2. Change the order of the numbers in the two diagonals. Thats it !!
# For eg:
# For a 4*4 grid, Switch the numbers on the diagonals--1 and 16, 11 and 6 on one diagonal; 7 and 10, 4 and 13 on the other. That's it!

import math, sys

def rowSlice(values, order, row):
    return values[row * order : (row + 1) * order]

def colSlice(values, order, col):
    return values[col : : order]

def foreDiagSlice(values, order):
    return values[order - 1 : order * order - 1 : order - 1]

def backDiagSlice(values, order):
    return values[ : : order + 1]

def rowSum(values, order, row):
    return sum(rowSlice(values, order, row))

def colSum(values, order, col):
    return sum(colSlice(values, order, col))

def foreDiagSum(values, order):
    return sum(foreDiagSlice(values, order))

def backDiagSum(values, order):
    return sum(backDiagSlice(values, order))

def toStrWithSums(values, order):
    magicSum = order * (order * order + 1) / 2
    valueWidth = int(math.ceil(math.log10(magicSum)))
    valueFormat = "%" + str(valueWidth) + "i"

    result = " " * (valueWidth * order + order) + "| " + str(foreDiagSum(values, order)) + "\n"
    result += "-" * ((valueWidth + 1) * (order + 1) + 1) + "\n"
    for row in range(order):
        result += " ".join(valueFormat % v for v in rowSlice(values, order, row)) + " | " + str(rowSum(values, order, row)) + "\n"
    result += "-" * ((valueWidth + 1) * (order + 1) + 1) + "\n"
    result += " ".join(valueFormat % colSum(values, order, col) for col in range(order)) + " | " + str(backDiagSum(values, order)) + "\n"
    return result

def main():
    order = int(sys.argv[1])
    length = order * order

    # http://www.curiousmath.com/index.php?name=News&file=article&sid=64
    # up 2 over 1 only works for odd order
    values = [0 for i in range(length)]
    idx = length - 1 - order / 2
    for i in range(length):
        values[idx] = i + 1
        newidx = (idx - order - order + 1) % length
        if newidx % order == 0:
            newidx = (newidx - order) % length
        if values[newidx] == 0:
            idx = newidx
        else:
            idx = (idx - order) % length
    print toStrWithSums(values, order)

    # http://www.curiousmath.com/index.php?name=News&file=article&sid=64
    # swapping diagonals only works for order == 4
    values = [i + 1 for i in range(length)]
    for i in range(order / 2):
        offset = i * (order + 1)
        tmp = values[offset]
        values[offset] = values[length - 1 - offset]
        values[length - 1 - offset] = tmp
        offset = (i + 1) * (order - 1)
        tmp = values[offset]
        values[offset] = values[length - 1 - offset]
        values[length - 1 - offset] = tmp
    print toStrWithSums(values, order)

#    values = [ ]
#    print toStrWithSums(values, order)
    return 0

#    def __init__(values, order, values=None):
#        genetic.Individual.__init__(values, order, values)
#        targetSum = order * (order * order + 1) / 2
#        valueWidth = int(math.ceil(math.log10(targetSum)))
#        valueFormat = "%" + str(valueWidth) + "i"

    return 0

if __name__ == '__main__':
    sys.exit(main())
