#!/usr/bin/env python3

"""
Convert values from one base to another.

Changed from original spec to specify output base in the input stream
rather than the command line.  This makes demonstration easier.
"""

import string
import sys

DEBUG = True

def baseString(base):
    """Return a Unicode printable version of a base."""
    (dig0, dig1) = divmod(base, 10)
    if dig0 == 0:
        printable = chr(0x2080 + base)
    else:
        printable = chr(0x2080 + dig0) + chr(0x2080 + dig1)
    return printable

DIGITS = string.digits + string.ascii_uppercase

def baseNToBase10(inputValue, inputBase):
    """
    Given an input integer string and an input base, return a
    base10 integer.
    """
    inputValue = inputValue.upper()
    sign = 1
    result = 0
    for digit in inputValue:
        if digit == "-":
            sign = -1
        elif digit == "+":
            sign = 1
        else:
            result = result * inputBase + DIGITS.index(digit)
    return sign * result

def base10ToOutput(value, outputBase):
    """Given a base10 integer and an output base, return an output string."""
    if value < 0:
        return "-" + base10ToOutput(-value, outputBase)
    result = ""
    while value != 0:
        value, remainder = divmod(value, outputBase)
        result = DIGITS[remainder] + result
    return result

def main():
    """main"""
    for line in sys.stdin:
        if line.startswith("#"):
            continue
        (inputBase, inputValue, outputBase) = line.split()
        inputBase = int(inputBase)
        outputBase = int(outputBase)
        print("{}{}".format(inputValue, baseString(inputBase)), end=" = ")

        base10Value = baseNToBase10(inputValue, inputBase)
        if DEBUG:
            print("{}{}".format(base10Value, baseString(10)), end=" = ")

        outputValue = base10ToOutput(base10Value, outputBase)
        print("{}{}".format(outputValue, baseString(outputBase)))
    return 0

if __name__ == "__main__":
    ret = main()
    sys.exit(ret)
