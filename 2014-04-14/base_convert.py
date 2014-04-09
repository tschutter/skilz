#!/usr/bin/env python3

"""
Convert values from one base to another.

Changed from original spec to specify output base in the input stream
rather than the command line.  This makes demonstration easier.
"""

import argparse
import decimal
import re
import string
import sys

DEBUG = True

def baseString(base):
    """Return a printable version of a base."""
    (dig0, dig1) = divmod(base, 10)
    if dig0 == 0:
        printable = chr(0x2080 + base)
    else:
        printable = chr(0x2080 + dig0) + chr(0x2080 + dig1)
    return printable

DIGITS = string.digits + string.ascii_uppercase

def intBaseNToBase10(inputValue, inputBase):
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

# (?![-+]) allows E only if it is not followed by - or +
RE_FLOAT = re.compile(
    "^([-+]?[0-9A-Z]+)(?:\.([0-9A-Z](?![-+]))+)?(?:[eE]([-+][0-9A-Z]+))?$"
)

def floatBaseNToBase10(inputValue, inputBase):
    """Calculate a base10 decimal from an input value and an input base."""
    match = RE_FLOAT.match(inputValue.upper())
    whole = match.group(1)
    fraction = match.group(2)
    exponent = match.group(3)
    if exponent:
        exponent = intBaseNToBase10(exponent, inputBase)
    else:
        exponent = 0
    if fraction:
        if DEBUG and False:
            print("\nexponent = {}, fraction = {}".format(exponent, fraction))
        exponent -= len(fraction)
        value = whole + fraction
        if DEBUG and False:
            print("exponent = {}, value = {}".format(exponent, value))
    else:
        value = whole
    value = decimal.Decimal(intBaseNToBase10(value, inputBase))
    multiplier = decimal.Decimal(inputBase) ** decimal.Decimal(exponent)
    value = value * multiplier
    return value

def base10ToOutput(value, outputBase):
    print(value, outputBase)
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

        base10Value = floatBaseNToBase10(inputValue, inputBase)
        if DEBUG:
            print("{}{}".format(base10Value, baseString(10)), end=" = ")

        outputValue = base10ToOutput(base10Value, outputBase)
        print("{}{}".format(outputValue, baseString(outputBase)))
    return 0

if __name__ == "__main__":
    ret = main()
    sys.exit(ret)
