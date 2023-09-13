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
# The data list is sorted in place (anew list is not created).
# You do NOT need to perform validation on input data
# (null data list, index out of bounds, etc.)
#
# q = [('a', 5), ('v', 9), ('z', 1), ('q', 7), ('m', -4), ('t', 12), ('c', 2)]

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


def quick_sort(data, index, descending=False):
    '''Sorts using the quick sort algorithm'''
    
    comp = (lambda x,y: x <= y) if descending else (lambda x,y: x >= y)

    def partition(array, start, end):
        pivot = array[start]
        low = start + 1
        high = end

        while True:

            while low <= high and comp(array[high][index], pivot[index]):
                high = high - 1

            while low <= high and (not comp(array[low][index], pivot[index])):
                low = low + 1   

            if low <= high:
                array[low], array[high] = array[high], array[low]                
            else:                
                break

        array[start], array[high] = array[high], array[start]

        return high


    def recursive_sort(array, start, end):
        if start >= end:
            return

        p = partition(array, start, end)
        recursive_sort(array, start, p-1)
        recursive_sort(array, p+1, end)

    recursive_sort(data, 0, len(data)-1)    


def python_sort(data, index, descending=False):
    '''Sorts using the native Python sort algorithm (Timsort)'''
    # LEAVE this function as is - it will allow you to see your sorts against the python one
    data.sort(key=lambda t: t[index], reverse=descending)
