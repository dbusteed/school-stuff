#!/usr/bin/env python3
import os, os.path, binascii
from collections import namedtuple
from io import StringIO


# a named tuple to hold an individual key and value
# this Node "object" is never seen outside this class
# (e.g. get() returns the value, not the full Node)
Node = namedtuple("Node", ( 'key', 'value' ))

# This is super small because we want to test the loading and print for debugging easier
NUM_BUCKETS = 10


class Hashtable(object):
    '''
    An abstract hashtable superclass.
    '''
    def __init__(self):
        self.buckets = []

        # --> [ [], [], [], ... ]
        for i in range(NUM_BUCKETS):
            self.buckets.append([])


    def set(self, key, value):
        '''
        Adds the given key=value pair to the hashtable.
        '''
        idx = self.get_bucket_index(key)
        self.buckets[idx].append( Node(key, value) )


    def get(self, key):
        '''
        Retrieves the value under the given key.
        Returns None if the key does not exist.
        '''
        idx = self.get_bucket_index(key)
        
        if self.buckets[idx]:
            for node in self.buckets[idx]:
                if key == node.key:
                    return node.value

        # return none if the bucket empty
        else:
            return None


    def remove(self, key):
        '''
        Removes the given key from the hashtable.
        Returns silently if the key does not exist.
        '''
        idx = self.get_bucket_index(key)
        
        if self.buckets[idx]:
            for node in self.buckets[idx]:
                if key == node.key:
                    self.buckets[idx].remove(node)

        # return silently if the bucket empty
        else:
            return ''


    def get_bucket_index(self, key):
        '''
        Returns the bucket index number for the given key.
        The number will be in the range of the number of buckets.
        '''
        # leave this method as is - write your code in the subclasses
        raise NotImplementedError('This method is abstract!  The subclass must define it.')


    ##################################################
    ###   Helper methods

    def __repr__(self):
        '''Returns a representation of the hash table'''
        buf = StringIO()
        for i, bkt in enumerate(self.buckets):
            for j, node in enumerate(bkt):
                buf.write('{:>5}  {}\n'.format(
                    '[{}]'.format(i) if j == 0 else '',
                    node.key,
                ))
        return buf.getvalue()



######################################################
###   String hash table

class StringHashtable(Hashtable):
    '''A hashtable that takes string keys'''

    def get_bucket_index(self, key):
        '''
        Returns the bucket index number for the given key.
        The number will be in the range of the number of buckets.
        '''      
        count = 0
        for char in key:
            count += ord(char)

        return count % len(self.buckets)



######################################################
###   Guid hash table

COUNTER_CHARS = ( 16, 24 )

class GuidHashtable(Hashtable):
    '''A hashtable that takes GUID keys'''

    def get_bucket_index(self, key):
        '''
        Returns the bucket index number for the given key.
        The number will be in the range of the number of buckets.
        '''
        counter = key[COUNTER_CHARS[0]:COUNTER_CHARS[1]]
        return int(counter, 16) % len(self.buckets)



######################################################
###   Image hash table

NUM_CHUNKS = 8
START_IDX = 2760

class ImageHashtable(Hashtable):
    '''A hashtable that takes image name keys and creates the hash from (some of) the bytes of the file.'''

    def get_bucket_index(self, key):
        '''
        Returns the bucket index number for the given key.
        The number will be in the range of the number of buckets.
        '''
        img_bytes = open(os.path.join('images', key), 'rb').read()[START_IDX:(START_IDX+NUM_CHUNKS)]
        return int(binascii.b2a_hex(img_bytes), 16) % len(self.buckets)