#!/bin/sh
#
# Given an integer number (say, a 32 bit integer number), write code
# to count the number of bits set (1s) that comprise the number.  For
# instance: 87338 (decimal) = 10101010100101010 (binary) in which
# there are 8 bits set.  No twists this time and as before, there is
# no language restriction.
#

# First argument is a decimal number.
NUMBER=$1

# Use "bc" to convert the decimal number to binary.  Setting
# BC_LINE_LENGTH to 0 prevents bc from wrapping at 70 characters.
BINARY=`echo "obase=2;${NUMBER}" | BC_LINE_LENGTH=0 bc`

# Strip out the zeros (and the minus sign if it is there).
ONES=`echo "${BINARY}" | tr --delete '0-'`

# Count the number of ones.  The count will include an implicit
# newline.
NSETBITS=`echo "${ONES}" | wc --chars`

# Subtract one for the implicit newline.
NSETBITS=`expr ${NSETBITS} "-" 1`

echo "Number of bits set = ${NSETBITS}"
