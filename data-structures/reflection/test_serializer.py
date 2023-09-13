from unittest import TestCase
from serialize import to_json_int, to_json_float, to_json_bool, to_json_nonetype

#
# Run with:
#   python -m unittest test_serializer

class TestSerializer(TestCase):

	def test_json_int(self):
		x = 5
		self.assertEqual("5", to_json_int(x))

	def test_json_float(self):
		x = 5.1
		self.assertEqual("5.1", to_json_int(x))

	def test_json_bool(self):
		x,y = True, False
		self.assertEqual("true", to_json_bool(x))
		self.assertEqual("false", to_json_bool(y))

	def test_json_none(self):
		x = None
		self.assertEqual("null", to_json_nonetype(x))