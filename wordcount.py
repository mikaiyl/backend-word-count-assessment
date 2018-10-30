#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys
import operator

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

###

def read_file( file ):
    blob = []
    num_of_lines = 0
    num_of_chars = 0
    with open( file, 'r+' ) as file:
        for line in file:
            num_of_chars += len( line )
            num_of_lines += 1
            blob += line.split()
    # I know this is bad but I wanted to make a
    # option that acts like wc for fun and the other
    # way I know how to do this is with a global
    return [ blob, num_of_lines, num_of_chars ]

def get_word_count( words ):
    return len( words )

def print_words( file ):
    [ words, lnum, cnum ] = read_file( file )
    lower_words = sorted( map( lambda w: w.lower(), words ) )
    for word in words:
        print word + ": x" + str( lower_words.count( word.lower() ) )
    return words

def print_top( filename ):
    # get the words
    [ words, lnum, cnum ] = read_file( filename )
    # make sure they 
    words = map( lambda x: x.lower(), words )

    count_list = {}
    # Work through list one word at a time and find all instances
    # Record the word and num of instances in the above dict
    # 
    while len(words) > 0:
        word = words[0]
        count_list[ word ] = words.count( word )
        words = filter( lambda x: x != word, words )
    sort_array = sorted( count_list.items(), key=operator.itemgetter(1), reverse=True )[:20]

    for [ word, n ] in sort_array:
        print str(n).zfill(4) + '  ' + word
    return

# traditional wc function
# *numOfLines* *numOfWords* *numOfChars* *filename*
def word_count( file ):
    [ words, lnum, cnum ] = read_file( file )
    num_words = get_word_count( words )
    print '  ' + str(lnum) + '  ' + str(num_words) + ' ' + str(cnum) + ' ' + sys.argv[2]

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.


def main():
    if len(sys.argv) != 3:
        print 'usage: ./wordcount.py { --count | --topcount | --wc } file'
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    # this is new
    elif option == '--wc':
        word_count(filename)
    else:
        print 'unknown option: ' + option
        sys.exit(1)


if __name__ == '__main__':
    main()
