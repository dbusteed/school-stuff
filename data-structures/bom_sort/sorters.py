# Parameters in the following functions:
#   data: a list of tuples
#   index: the tuple index to sort by
#
# Consider the following example data:
#   data = [
#       ( 'homer', 'simpson', 50 ),
#       ( 'luke', 'skywalker', 87 ),
#       ( 'bilbo', 'baggins', 111 ),
#   ]
#
#   bubble_sort(data, 0) sorts on first name (a..z)
#   bubble_sort(data, 0, True) sorts on first name (z..a)
#   bubble_sort(data, 2) sorts on age (1..infinity)
#
# The data list is sorted in place (a new list is not created).
# You do NOT need to perform validation on input data
# (null data list, index out of bounds, etc.)
#

# i like to test this one
# q = [('a', 0), ('u', 3), ('q', 9), ('p', 10), ('e', 4), ('c', 2), ('b', 1)]

def bubble_sort(data, index, descending=False):
    '''Sorts using the bubble sort algorithm'''

    comp = (lambda x,y: x < y) if descending else (lambda x,y: x > y)

    for i in range(len(data)-1):
        for j in range(i+1, len(data)):
            if comp(data[i][index], data[j][index]):
                data[i], data[j] = data[j], data[i]


def insertion_sort(data, index, descending=False):
    '''Sorts using the insertion sort algorithm'''

    comp = (lambda x,y: x < y) if descending else (lambda x,y: x > y)

    for i in range(1,len(data)):
        
        hold = data[i]
        
        j = i-1
        while comp(data[j][index], hold[index]) and j >= 0:
            data[j+1] = data[j]
            j -= 1
        
        data[j+1] = hold


def selection_sort(data, index, descending=False):
    '''Sorts using the selection sort algorithm'''
    
    comp = (lambda x,y: x < y) if descending else (lambda x,y: x > y)

    for i in range(len(data)):

        ex = i
        for j in range(i, len(data)):
            ex = j if comp(data[ex][index], data[j][index]) else ex

        data[i], data[ex] = data[ex], data[i]