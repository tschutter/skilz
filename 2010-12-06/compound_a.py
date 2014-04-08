#!/usr/bin/python
#
# Find all the two-word compound words in a dictionary. A two-word
# compound word is a word in the dictionary that is the concatenation
# of exactly two other words in the dictionary. Assume input will be a
# number of lowercase words, one per line, in alphabetical order,
# numbering around, say, 100K. Generate output consisting of all the
# compound words, one per line, in alphabetical order.
#

import sys

def main():
    # Read the words into a list and sort the list.
    wordlist = [word.strip() for word in open(sys.argv[1]) if word != "\n"]
    nwords = len(wordlist)
    wordlist.sort()

    # Add the words to a dictionary.
    worddict = dict.fromkeys(wordlist)

    # Debug.
    maxscan = -1
    ncompound = 0

    # Loop through the words.
    for i, word in enumerate(wordlist):
        wordlen = len(word)

        # Find the following adjacent words that start with the same word.
        for j in xrange(i + 1, nwords):
            testword = wordlist[j]
            if not testword.startswith(word):
                if __debug__ and maxscan < j - i:
                    maxscan = j - i
                break

            # See if the remaining part of the word is in the dictionary.
            suffix = testword[wordlen:]
            if suffix in worddict:
                print "%s + %s = %s" % (word, suffix, testword)
                if __debug__:
                    ncompound += 1

    if __debug__:
        print "DEBUG: nwords = %s" % nwords
        print "DEBUG: ncompound = %s" % ncompound
        print "DEBUG: maxscan = %s" % maxscan

if __name__ == '__main__':
    main()
