#!/usr/bin/python
#
# The premise is that in the brave new world, a phone will be
# developed where the letters that appear on the keys are, well, just
# different:
#   e | j n q | r w x | d s y | f t | a m | c i v | b k u | l o p | g h z
#   0 |   1   |   2   |   3   |  4  |  5  |   6   |   7   |   8   |   9
# Additionally, the phone numbers can be all different lengths.
# Given a phone number and a dictionary, write a program to find all
# words in the dictionary that could be an encoding of the phone
# number. For a chance to gain even more prestige, find encodings of
# the number that encompass more than a single word (two smaller
# words).
#
# 454654
# 8888-03
#

import re, string, sys
from collections import defaultdict

def main():
    # Process command line arguments.
    phoneNumber = sys.argv[1]
    dictionaryFilename = sys.argv[2]

    # Cleanup the phone number.
    phoneNumber = re.sub("[^0-9]", "", phoneNumber)

    # Build a translation function to translate letters to digits.
    transTable = string.maketrans(
        "abcdefghijklmnopqrstuvwxyz",
        "57630499617851881234762239"
    )

    # Read dictionary file and create a dict.  The key is the word
    # where the letters have been translated to digits.  The value is
    # a list of words.
    dictionary = defaultdict(list)
    with open(dictionaryFilename) as file:
        for word in file.read().split():
            key = word.translate(transTable)
            dictionary[key].append(word)

    # Print the list of words that map to the digits.
    if phoneNumber in dictionary:
        for word in dictionary[phoneNumber]:
            print word

    # Try two words.
    for split in range(1, len(phoneNumber)):
        leftPhone = phoneNumber[:split]
        rightPhone = phoneNumber[split:]
        if leftPhone in dictionary and rightPhone in dictionary:
            for leftWord in dictionary[leftPhone]:
                for rightWord in dictionary[rightPhone]:
                    print leftWord + "+" + rightWord

    return 0

if __name__ == '__main__':
    sys.exit(main())
