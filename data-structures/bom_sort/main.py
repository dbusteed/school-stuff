#!/usr/bin/env python3
from sorters import bubble_sort, insertion_sort, selection_sort
from collections import namedtuple, Counter
import re


# data for a single word
WordData = namedtuple("WordData", [ 'word', 'count', 'percent' ])

def get_data():
    '''Returns the list of WordData objects'''
    # Read `bom.txt` into a string.
    bom = open('bom.txt', 'r').read()

    # Convert the entire string to lowercase.
    bom = bom.lower()

    # Split the string by any non-alpha character. Regular expressions are your friend here.
    # A simple regular expression with `re.split(...)` will do this for you.
    tokens = re.split(r'[^a-z0-9]', bom)

    # Using a list comprehension with a conditional (if), create a new list that contains only
    # those words that are 5+ alpha characters in length. All of the following will be
    # skipped: "am", "", "i", "are".
    tokens = [t for t in tokens if len(t) >= 5]
    
    # only filtered? or all ???
    num_of_tokens = len(tokens)

    # Count the frequency of each word in the list, creating a WordData object for each
    # unique word.  Round all percentages to three decimal places: 3.141592 => 3.142.
    # See the `collections.Counter` module is your friend here.  The percent for a given
    # word is calculated as `count / length of list`, rounded to one decimal place.

    data = []
    counts = Counter(tokens)

    for word, count in counts.items():
        data.append(WordData(word, count, round( (count/num_of_tokens) * 100, 3) ))

    # return the list of WordData objects, which contains
    # a single object for each unique word
    return data



#######################
###   Main loop

def main():
    '''Main program'''
    # get the WordData list

    # Sort the list of WordData objects by highest percent using your Bubble Sort
    # function. Sort the list in place (don't create a new list). Print the first 50
    # WordData objects in the list.
    print()
    print('BY PERCENT:')
    data = get_data()
    bubble_sort(data, 2, descending=True)
    for wd in data[:50]:
        print(wd)

    # Sort the list of WordData objects by highest count using your Insertion Sort
    # function. Sort the list in place (don't create a new list). Print the first 50
    # WordData objects in the list.
    print()
    print('BY COUNT:')
    data = get_data()
    insertion_sort(data, 1, descending=True)
    for wd in data[:50]:
        print(wd)

    # Sort the list of WordData objects by alpha order (a-z) using your Selection Sort
    # function. Sort the list in place (don't create a new list). Print the first 50
    # WordData objects in the list.
    print()
    print('BY WORD:')
    data = get_data()
    selection_sort(data, 0)
    for wd in data[:50]:
        print(wd)


if __name__ == '__main__':
    main()
