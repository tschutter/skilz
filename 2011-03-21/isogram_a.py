#!/usr/bin/python
#
# An isogram (also known as a "nonpattern word") is a logological term
# for a word or phrase without a repeating letter. It is also used by
# some to mean a word or phrase in which each letter appears the same
# number of times, not necessarily just
# once. (http://en.wikipedia.org/wiki/Isogram)
# Examples:
#   'Wyoming' is an isogram, while 'Alabama' is not.
#   'Many' and 'few' are isograms, 'none' is not.
#   'Toto' is an isogram by the second definition, but not the first.
# Requirement: Given a word or phrase, report whether or not it's an
# isogram by the first definition above. Bonus: test for the second
# definition.
#
# Wyoming Alabama Many few none Toto Dermatoglyphics
#

import collections, fileinput, re, sys

def isIsogram(word):
    letterCounts = collections.defaultdict(int)
    for letter in word.lower():
        letterCounts[letter] += 1
    minCount = min(letterCounts.values())
    maxCount = max(letterCounts.values())
    if minCount != maxCount:
        return "no"
    elif minCount == 1:
        return "yes"
    else:
        return "alt"

def main():
    # Process command line arguments.
    if len(sys.argv) > 1 and re.match("(-s|--stats)", sys.argv[1]):
        sys.argv.remove("--stats")
        stats = collections.defaultdict(int)
    else:
        stats = None

    # Get an answer for each word.
    for line in fileinput.input():
        for word in line.split():
            answer = isIsogram(word)
            if stats != None:
                stats[answer] += 1
            else:
                print word, answer

    # Print statistics.
    if stats != None:
        for (answer, count) in stats.items():
            print answer, count

    return 0

if __name__ == '__main__':
    sys.exit(main())
