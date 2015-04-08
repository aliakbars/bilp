import cleaner
import unittest

class Test(unittest.TestCase):
	def setUp(self):
		self.kamus = cleaner.fillKamus('singkatan-lib.csv')
		self.case1 = '...demi menjadi presiden wiranto rela jd buruh kasar d pasar klewer,Solo'
		self.tokens1 = ['demi', 'menjadi', 'presiden', 'wiranto', 'rela', 'jd', 'buruh', 'kasar', 'd', 'pasar', 'klewer', 'solo']

	def tearDown(self):
		pass

	def test_tokenize(self):
		self.assertEqual(cleaner.tokenize(self.case1), self.tokens1)

	def test_translate(self):
		self.assertEqual(cleaner.translate(self.case1, self.kamus), 'demi menjadi presiden wiranto rela jadi buruh kasar di pasar klewer solo')