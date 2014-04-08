#!/usr/bin/python
#

import sys

def useLargeArray(nrows, ncols):
    # Allocate a two dimensional array.
    grid = [ [ 0 ] * ncols for row in range(nrows)]

    # Define the initial box.
    startrow = 0
    endrow = nrows
    startcol = 0
    endcol = ncols
    val = 1

    while startrow < endrow and startcol < endcol:
        # Go right.
        for col in range(startcol, endcol):
            grid[startrow][col] = val
            val += 1
        if startrow + 1 == endrow:
            break

        # Go down.
        for row in range(startrow + 1, endrow):
            grid[row][endcol - 1] = val
            val += 1
        if startcol - 1 == endcol - 2:
            break

        # Go left.
        for col in range(endcol - 2, startcol - 1, -1):
            grid[endrow - 1][col] = val
            val += 1

        # Go up.
        for row in range(endrow - 2, startrow, -1):
            grid[row][startcol] = val
            val += 1

        # Shrink the box.
        startrow += 1
        endrow -= 1
        startcol += 1
        endcol -= 1

    # Print the array.
    width = len("{0}".format(nrows * ncols))
    print "      " + " ".join(["{0:{width}}".format(col, width=width) for col in range(ncols)])
    for rownum, row in enumerate(grid):
        print "{0:3}: ".format(rownum),
        print " ".join(["{0:{width}}".format(val, width=width) for val in row])

def rowvals(nrows, ncols, row):
    midcol = int(ncols / 2)
    delta = nrows * 2 + ncols * 2 - 3
    deltaorig = delta
    val = -row
    if row <= int((nrows - 1) / 2):
        # Top half.
        for col in range(0, min(row, midcol)):
            val += delta
            delta -= 8
            yield val
        for col in range(min(row, midcol), max(midcol, ncols - row)):
            val += 1
            yield val
        if row <= midcol:
            delta += 4
        else:
            if ncols % 2 == 0:
                val += (row - midcol) * 2
                delta += 4
            else:
                val += (row - midcol) * 2 + 8
                delta -= 4
        for col in range(max(midcol, ncols - row), ncols):
            val -= delta
            delta += 8
            yield val
    else:
        # Bottom half.
        for col in range(0, min(nrows - row, midcol)):
            val += delta
            delta -= 8
            yield val
        for col in range(min(nrows - row, midcol), max(midcol, ncols - (nrows - 1 - row))):
            val -= 1
            yield val
        # need work on 10 5
        if nrows - row == midcol:
            if ncols % 2 == 0:
                delta += 12
            else:
                delta += 12
        elif nrows - row < midcol:
            delta += 12
        # need work to here
        else:
            if ncols % 2 == 0:
                val += (row - midcol) * 2
                delta += 4
            else:
                val += (row - midcol) * 2 + 8
                delta -= 4
        for col in range(max(midcol, ncols - (nrows - 1 - row)), ncols):
            val -= delta
            delta += 8
            yield val

def useGenerator(nrows, ncols):
    width = len("{0}".format(nrows * ncols))

    print "      " + " ".join(["{0:{width}}".format(col, width=width) for col in range(ncols)])
    for row in range(nrows):
        print "{0:3}: ".format(row),
        for val in rowvals(nrows, ncols, row):
            print "{0:{width}}".format(val, width=width),
        print ""

def main():
    nrows = int(sys.argv[1])
    if len(sys.argv) > 2:
        ncols = int(sys.argv[2])
    else:
        ncols = nrows

    print "Fill and then print array:"
    useLargeArray(nrows, ncols)

    print "\nGenerate values on the fly:"
    useGenerator(nrows, ncols)

if __name__ == '__main__':
    sys.exit(main())
