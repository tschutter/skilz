#!/usr/bin/python
#
# Find all the two-word compound words in a dictionary. A two-word
# compound word is a word in the dictionary that is the concatenation
# of exactly two other words in the dictionary. Assume input will be a
# number of lowercase words, one per line, in alphabetical order,
# numbering around, say, 100K. Generate output consisting of all the
# compound words, one per line, in alphabetical order.
#

import multiprocessing
import sys

def findwords(wordlist, worddict, start, stop):
    nwords = len(wordlist)
    result = []

    for i in xrange(start, stop):
        word = wordlist[i]
        wordlen = len(word)

        # Find the following adjacent words that start with the same word.
        for j in xrange(i + 1, nwords):
            testword = wordlist[j]
            if not testword.startswith(word):
                break

            # See if the remaining part of the word is in the dictionary.
            suffix = testword[wordlen:]
            if suffix in worddict:
                result.append((word, suffix, testword))

    return result

def main():
    # Read the words into a list and sort the list.
    filename = sys.argv[1]
    wordlist = [word.strip() for word in open(filename) if word != "\n"]
    nwords = len(wordlist)
    wordlist.sort()

    # Add the words to a dictionary.
    worddict = dict.fromkeys(wordlist)

    # Loop through the words.
    print "cpu_count = %i" % multiprocessing.cpu_count()
    manager = multiprocessing.Manager()
    wordlist = multiprocessing.Array('s', wordlist)
    worddict = manager.dict(worddict)
    pool = multiprocessing.Pool(processes = 8)
    asyncResults = []
    njobs = 64
    jobsize = max(1, nwords / 128)
    for start in range(0, nwords, jobsize):
        stop = min(start + jobsize, nwords)
        if start < stop:
            asyncResults.append(pool.apply_async(findwords, (wordlist, worddict, start, stop)))
    results = []
    for asyncResult in asyncResults:
        results.extend(asyncResult.get())

    # Print the results.
    #for word, suffix, testword in results:
    #    print "%s + %s = %s" % (word, suffix, testword)
    print "nresults = %i" % len(results)

if __name__ == '__main__':
    main()
