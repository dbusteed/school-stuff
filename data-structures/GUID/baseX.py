#!/usr/bin/env python3

import math

class BaseXConverter(object):
    '''
    Converts positive, base-10 numbers to base-X numbers using a custom alphabet.
    The base is given by the length of the alphabet specified in the constructor.
    The first character in the alphabet has a value of zero,
    the second character a value of one, and so forth.

    Examples:
        Base2:  BaseXConverter('01')
        Base2:  BaseXConverter('<>')     # custom alphabet: < is a zero value and > is a one value
        Base4:  BaseXConverter('0123')
        Base20: BaseXConverter('0123456789abcdefghij')

    See the unit tests at the bottom of the file for many examples.
    '''

    def __init__(self, alphabet):
        '''
        The base is taken from the number of characters in the alphabet.
        '''
        self.alphabet = list(alphabet)
        self.base = len(alphabet)

    def convert(self, val):
        '''
        Converts value from base 10 to base X.
        The return value is a baseX integer, wrapped as a string.
        '''

        if val > 0:

            out = []
            
            while val > 0:
                val, rem = divmod(val, self.base)
                out.append(self.alphabet[rem])

            out.reverse()

            bXval = ''.join(out)

        else:

            bXval = self.alphabet[0]

        return bXval

    def invert(self, bXval):
        '''
        Converts a value from base X to base 10.
        The bXval should be a baseX integer, wrapped as a string.
        Raises a ValueError if bXval contains any chars not in the alphabet.
        '''

        bXval = str(bXval)

        val = 0

        for i,char in enumerate(bXval):
            
            if char not in self.alphabet:
                raise ValueError("character not found in alphabet")

            val += ((self.base ** (len(bXval)-1-i)) * self.alphabet.index(char))

        return val
