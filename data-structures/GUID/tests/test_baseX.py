from unittest import TestCase
from baseX import BaseXConverter
import base16, base58
from random import randint
from uid import generate, unpack, SHARD_ID
from time import sleep

# Run this from its parent directory:
#
#    python3 -m unittest tests.test_baseX
#

class BaseXTester(TestCase):

    def test_base2(self):
        conv = BaseXConverter('01')
        i = 1234567890
        self.assertEqual(conv.convert(i), '{:0b}'.format(i))    # test against python's builtin
        self.assertEqual(i, conv.invert(conv.convert(i)))

    def test_base16(self):
        num = randint(1,10000)
        encoded_num = base16.convert(num)
        decoded_num = base16.invert(encoded_num)
        self.assertEqual(num, decoded_num)        

    def test_base58(self):
        num = randint(1,10000)
        encoded_num = base58.convert(num)
        decoded_num = base58.invert(encoded_num)
        self.assertEqual(num, decoded_num)

    # check if 3 objects received from unpack
    def test_unpack_length(self):
        uid = generate()
        self.assertEqual(len(unpack(uid)), 3)

    # check if correct SHARD is returned
    def test_unpack_shard(self):
        uid = generate()
        unpacked_shard = unpack(uid)[2]
        self.assertEqual(unpacked_shard, SHARD_ID)

    # check if 2nd uid is created after the 1st
    def test_two_uids(self):
        u1 = generate()
        sleep(.01)
        u2 = generate()
        time1, time2 = unpack(u1)[0], unpack(u2)[0]
        self.assertLess(time1, time2)