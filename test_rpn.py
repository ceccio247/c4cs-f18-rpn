import unittest
import rpn

class TestBasics(unittest.TestCase):
	def test_add(self):
		result = rpn.calculate("1 1 +")
		self.assertEqual(2, result)
	def test_sub(self):
		result = rpn.calculate("4 3 -")
		self.assertEqual(1, result)
	def test_div(self):
		result = rpn.calculate("4 2 /")
		self.assertEqual(2, result)
	def test_mult(self):
		result = rpn.calculate("3 5 *")
		self.assertEqual(15, result)
	def test_exp(self):
		result = rpn.calculate("3 2 ^")
		self.assertEqual(9, result)
