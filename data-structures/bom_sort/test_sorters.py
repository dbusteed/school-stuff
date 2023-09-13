from unittest import TestCase
from pprint import pprint
import random

#
# Run with:
#   python -m unittest test_sorters

class SortTestCase(TestCase):
    '''Unit tests for the three sort functions'''
    LETTERS = 'abcdefghijklmnopqrstuvwxyz'

    def setUp(self):
        '''Set up the test: called before *each* test function'''
        # we generate list of tuples of random data to be used.
        self.data = []
        for i in range(10):
            self.data.append((
                ''.join(( random.choice(self.LETTERS) for i in range(10) )), # 10 random letters
                random.randint(0, 100),                                      # an integer
                round(random.uniform(0.0, 100.0), 1),                        # a float
            ))


    def debugPrint(self):
        '''Helper method during debugging the tests'''
        pprint(self.data)
        print('')


    def iterPairs(self):
        '''
        Iterates the data list, yielding each sequential pair or rows:
            ( self.data[0], self.data[1] ),
            ( self.data[1], self.data[2] ),
            ...
        '''
        last = None
        for item in self.data:
            if last is not None:
                yield (last, item)
            last = item


    def test_bubble_sort_ascending(self):
        from sorters import bubble_sort
        idxes = [0,1,2]

        for idx in idxes:
            bubble_sort(self.data, idx)

            # self.debugPrint()                   # remove this line - only used while creating the test
            for a, b in self.iterPairs():
                # print('{} < {}'.format(a, b))   # remove this line - only used while creating the test
                self.assertLessEqual(a[idx], b[idx],
                    msg='previous {} should be less than current {} at index {}'.format(a, b, idx))


    # add at least 5 more methods to the class


    def test_bubble_sort_descending(self):
        from sorters import bubble_sort
        idxes = [0,1,2]

        for idx in idxes:
            bubble_sort(self.data, idx, True)

            for a, b in self.iterPairs():
                self.assertGreaterEqual(a[idx], b[idx],
                    msg='previous {} should be less than current {} at index {}'.format(a, b, idx))


    def test_insertion_sort_ascending(self):
        from sorters import insertion_sort
        idxes = [0,1,2]

        for idx in idxes:
            insertion_sort(self.data, idx)

            for a, b in self.iterPairs():
                self.assertLessEqual(a[idx], b[idx],
                    msg='previous {} should be less than current {} at index {}'.format(a, b, idx))


    def test_insertion_sort_descending(self):
        from sorters import insertion_sort
        idxes = [0,1,2]

        for idx in idxes:
            insertion_sort(self.data, idx, True)

            for a, b in self.iterPairs():
                self.assertGreaterEqual(a[idx], b[idx],
                    msg='previous {} should be less than current {} at index {}'.format(a, b, idx))


    def test_selection_sort_ascending(self):
        from sorters import selection_sort
        idxes = [0,1,2]

        for idx in idxes:
            selection_sort(self.data, idx)

            for a, b in self.iterPairs():
                self.assertLessEqual(a[idx], b[idx],
                    msg='previous {} should be less than current {} at index {}'.format(a, b, idx))


    def test_selection_sort_descending(self):
        from sorters import selection_sort
        idxes = [0,1,2]

        for idx in idxes:
            selection_sort(self.data, idx, True)

            for a, b in self.iterPairs():
                self.assertGreaterEqual(a[idx], b[idx],
                    msg='previous {} should be less than current {} at index {}'.format(a, b, idx))


    # do the sorting methods give the same results?
    # if the above tests passed, this is kinda redundant but i'm having fun
    def test_bubble_insertion(self):
        from sorters import bubble_sort, insertion_sort
        idxes = [0,1,2]

        for idx in idxes:
            data_copy1, data_copy2 = self.data[:], self.data[:]

            bubble_sort(data_copy1, idx)
            insertion_sort(data_copy2, idx)

            for i in range(len(data_copy1)):
                self.assertEqual(data_copy1[i][idx], data_copy2[i][idx])


    def test_bubble_selection(self):
        from sorters import bubble_sort, selection_sort
        idxes = [0,1,2]

        for idx in idxes:
            data_copy1, data_copy2 = self.data[:], self.data[:]

            bubble_sort(data_copy1, idx)
            selection_sort(data_copy2, idx)

            for i in range(len(data_copy1)):
                self.assertEqual(data_copy1[i][idx], data_copy2[i][idx])


    def test_insertion_selection(self):
        from sorters import insertion_sort, selection_sort
        idxes = [0,1,2]

        for idx in idxes:
            data_copy1, data_copy2 = self.data[:], self.data[:]

            insertion_sort(data_copy1, idx)
            selection_sort(data_copy2, idx)

            for i in range(len(data_copy1)):
                self.assertEqual(data_copy1[i][idx], data_copy2[i][idx])
