#!/usr/bin/python
#

import fileinput, sys

def rowCol2Quadkey(rowCol):
    row, col, nBits = rowCol
    quadkey = "".join(["0123"[(col & (1 << b) > 0) + (row & (1 << b) > 0) * 2] for b in xrange(nBits - 1, -1, -1)])
    return quadkey

def quadkey2RowCol(quadkey):
    row = int("".join([ "0011"[int(c)] for c in quadkey ]), 2)
    col = int("".join([ "0101"[int(c)] for c in quadkey ]), 2)
    nBits = len(quadkey)
    return (row, col, nBits)

def main():
    for line in fileinput.input():
        line = line.strip()
        if line.startswith("("):
            rowCol = eval(line)
            quadkey = rowCol2Quadkey(rowCol)
            rowCol2 = quadkey2RowCol(quadkey)
            print "%s -> %s -> %s" % (str(rowCol), quadkey, str(rowCol2))
        else:
            quadkey = line
            rowCol = quadkey2RowCol(quadkey)
            quadkey2 = rowCol2Quadkey(rowCol)
            print "%s -> %s -> %s" % (quadkey, str(rowCol), quadkey2)
    return 0

if __name__ == '__main__':
    sys.exit(main())
