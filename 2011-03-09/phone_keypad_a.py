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

import re, sys

digitToLettersMap = {
    "0": "e",
    "1": "jnq",
    "2": "rwx",
    "3": "dsy",
    "4": "ft",
    "5": "am",
    "6": "civ",
    "7": "bku",
    "8": "lop",
    "9": "ghz"
}

def buildPossibleWords(possibleWords, word, phoneNumber):
    if len(phoneNumber) == 0:
        possibleWords.append(word)
    else:
        digit = phoneNumber[0]
        phoneNumber = phoneNumber[1:]
        letters = digitToLettersMap[digit]
        for letter in letters:
            buildPossibleWords(possibleWords, word + letter, phoneNumber)

def main():
    # Process command line arguments.
    phoneNumber = sys.argv[1]
    dictionaryFilename = sys.argv[2]

    # Cleanup the phone number.
    phoneNumber = re.sub("[^0-9]", "", phoneNumber)

    # Read dictionary file into a frozenset.
    with open(dictionaryFilename) as file:
        words = file.read().split()
    dictionary = frozenset(words)

    # Build list of possible words.
    possibleWords = []
    buildPossibleWords(possibleWords, "", phoneNumber)

    # Print the possible words that exist in the dictionary.
    for word in possibleWords:
        if word in dictionary:
            print word

    return 0

if __name__ == '__main__':
    sys.exit(main())
