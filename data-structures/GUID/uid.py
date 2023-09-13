#!/usr/bin/env python3

import base2, base16, base58
import base64_ as base64
from time import time, sleep

##############################################################################################################################################################################
#  A uid class based on time, counter, and shard id.                                                                                                                         #
#                                                                                                                                                                            #
# |                | Time Component                 | Time Component                            | Space Component                                                            |
# |----------------|--------------------------------|-------------------------------------------|----------------------------------------------------------------------------|
# | Number of Bits | 42 bits                        | 13 bits                                   | 8 bits                                                                     |
# | Description    | Milliseconds since Jan, 1970   | Counter (allows more than one UID per ms) | Shard ID (assigned explicitly to a server, process, or database)           |
# | Maximum Value  | 4,398,046,511,104 (May, 2109)  | 8,192 per ms                              | 256 unique locations                                                       |


# range is 0-255
SHARD_ID = 13

# sizes
MILLIS_BITS = 42
COUNTER_BITS = 13
SHARD_BITS = 8

# the masks
MILLIS_MASK = 4398046511103 #42 ones
COUNTER_MASK = 8191 # 13 ones
SHARD_MASK = 255 # 8 ones

LAST_MILLIS = 0
COUNTER = 0

MAX_COUNTER = 8191

# map each base to the respective module
CONV = {
    2: base2,
    16: base16,
    58: base58,
    64: base64,
}

def generate(base=10):
    '''Generates a uid with the given base'''
    global LAST_MILLIS
    global COUNTER

    # get the millisecond, waiting if needed if we've hit the max counter
    if COUNTER >= MAX_COUNTER:
        sleep(.01)
    
    millis = round(time() * 1000)

    if millis == LAST_MILLIS:
        COUNTER += 1

    # reset the counter if we are in a new millisecond
    if millis > LAST_MILLIS:
        COUNTER = 0
    
    LAST_MILLIS = millis
    
    # pack it up into base10
    uid = pack(millis, COUNTER, SHARD_ID)

    # convert base

    if base in CONV:
        uid = CONV[base].convert(uid)
    else:
        # use base 10
        uid = str(uid)

    return uid


def pack(millis, counter, shard):
    '''Combines the three items into a single uid number'''

    # ??? necessary
    uid = base2.convert(millis).rjust(42, '0') \
            + base2.convert(counter).rjust(13, '0') \
            + base2.convert(shard).rjust(8, '0')

    # needs to go to base10 ???
    uid = int(uid, 2)

    return uid  

# can i change function signature?
def unpack(uid, base=10):
    '''Separates the uid into its three parts'''
    
    if base in CONV:
        uid10 = CONV[base].invert(uid)
    else:
        # use base 10
        uid10 = int(uid)

    millis = (uid10 >> (COUNTER_BITS + SHARD_BITS)) & MILLIS_MASK
    counter = (uid10 >> SHARD_BITS) & COUNTER_MASK
    shard = (uid10) & SHARD_MASK
    
    return (millis, counter, shard)
