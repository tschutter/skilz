#!/usr/bin/env python3

"""
Convert values from one base to another.

TODO:
  regexp: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?$
  strip out ., adjusting shift
  convert mantissa
"""

import argparse
import string
import sys

DIGITS = string.digits + string.ascii_uppercase

def baseString(base):
    """Return a printable version of a base."""
    (dig0, dig1) = divmod(base, 10)
    if dig0 == 0:
        printable = chr(0x2080 + base)
    else:
        printable = chr(0x2080 + dig0) + chr(0x2080 + dig1)
    return printable

def inputToBase10(string, inputBase):
    """Given an input string and an input base, return a base10 integer."""
    string = string.upper()
    sign = 1
    result = 0
    for digit in string:
        if digit == "-":
            sign = -1
        elif digit == ".":
            result = result
        else:
            result = result * inputBase + DIGITS.index(digit)
    return sign * result

def inputToBase10v2(string, inputBase):
    """Given an input string and an input base, return a base10 integer and decimal shift."""
    string = string.upper()
    if string[0] == "-":
        string = string[1:]
        sign = -1
    else:
        sign = 1
    result = 0
    shift = 0
    for (i, digit) in enumerate(string):
        if digit == "." and shift == 0:
            shift = len(string) - 1 - i
        else:
            result = result * inputBase + DIGITS.index(digit)
    return (sign * result, shift)

def base10ToOutput(value, outputBase):
    """Given a base10 integer and an output base, return an output string."""
    if value < 0:
        return "-" + base10ToOutput(-value, outputBase)
    result = ""
    while value != 0:
        value, remainder = divmod(value, outputBase)
        result = DIGITS[remainder] + result
    return result

def base10ToOutputv2(value, shift, outputBase):
    """Given a base10 integer, a decimal shift, and an output base, return an output string."""
    if value < 0:
        return "-" + base10ToOutput(-value, outputBase)
    result = ""
    while value != 0:
        if shift != 0 and len(result) == shift:
            result = "." + result
        value, remainder = divmod(value, outputBase)
        result = DIGITS[remainder] + result
    return result

def main():
    """main"""
    parser = argparse.ArgumentParser(
        description="Convert values from one base to another."
    )
    parser.add_argument(
        "base",
        type=int,
        choices=range(2, 37),
        metavar="BASE",
        help="output base"
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        default=False,
        help="print itermediate values"
    )
    args = parser.parse_args()
    outputBase = args.base

    for line in sys.stdin:
        (inputBase, inputValue) = line.split()
        inputBase = int(inputBase)
        print("{}{}".format(inputValue, baseString(inputBase)), end=" = ")

        (base10Value, shift) = inputToBase10v2(inputValue, inputBase)
        if args.debug:
            print("{}{}s{}".format(base10Value, baseString(10), shift), end=" = ")

        base10Value = inputToBase10(inputValue, inputBase)
        if args.debug:
            print("{}{}".format(base10Value, baseString(10)), end=" = ")

        outputValue = base10ToOutput(base10Value, outputBase)
        print("{}{}".format(outputValue, baseString(outputBase)))
    return 0

if __name__ == "__main__":
    ret = main()
    sys.exit(ret)
