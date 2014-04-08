#!/usr/bin/python
#
# Write a simple mail merge program that accepts a document and a data
# file.  The document will contain variable text identified as $n
# where n is the zero-based data field number in the data file.  The
# data file will be a tab delimited file containing no header line.
# Merge and write the merged document(s) to the screen.
#
# ./mail_merge.py mail_merge_doc.txt mail_merge_data.txt | fold -w 40 -s | less
#

import csv, re, sys

def main():
    # Read the document file.
    with open(sys.argv[1]) as docfile:
        doc = docfile.read()

    # Quote curly braces.
    doc = doc.replace("{", "{{").replace("}", "}}")

    # Convert "$n" to "{0[n]}".
    doc = re.sub(r"\$([0-9]+)", r"{0[\1]}", doc)

    # Read the data file.
    with open(sys.argv[2]) as datafile:
        for data in csv.reader(datafile, delimiter = "\t"):
            # Merge the data into the document.
            print doc.format(data),
            print "==================================\n\f",

if __name__ == '__main__':
    sys.exit(main())
