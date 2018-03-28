import unittest
from matrix import Matrix

# matrix by fisheye36

class MyTest(unittest.TestCase):

	def wrong_number_of_arguments(self):
		self.assertRaises(ValueError, Materix(1,2,4))

	def string_repr_test(self):
		matrix = Matrix(1,2,3,4)
		self.assertEqual("(1, 2, 3, 4)", str(matrix))

	def add_test(self):
		matrix1 = Matrix(1,2,3,4)
		matrix2 = Matrix(1,2,3,5)
		self.asserEquals("(2, 4, 6, 11)", str(matrix1.add(matrix2)))

	def throw_erro_when_add_with_bad_dimensions(self):
		matrix = Matrix(1,2,3,4)
		matrix2 = Matrix(1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7)
		self.assertRaises(ValueError, matrix.add(matrix2))
	def test_size(self):
		self.assertEquals(2, Matrix(1,2,3,4))
		self.assertEquals(4, Matrix(1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7))
