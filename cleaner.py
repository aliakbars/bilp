import csv
import re
import unittest

def fillKamus(filename):
	file_data = open(filename)
	kamus = {}
	file_data.readline()
	for key in file_data:
	    key = key.replace('"', '').strip()
	    k = key.split(",")
	    kamus['%s' % k[0]] = '%s' % k[1]
	return kamus

def writeFile(file_in, column, file_out, kamus):
	"File must be in csv format"
	with open(file_in) as fi:
		f = csv.reader(fi)
		out = open(file_out, 'w')
		for row in f:
			line = translate(row[column], kamus)
			out.write('"%s"\n' % line)

def tokenize(line):
	return filter(lambda x: x != '', re.split('[^\w]', line.lower()))

def translate(line, kamus):
	tokens = tokenize(line)
	for key, word in enumerate(tokens):
		if word in kamus:
			tokens[key] = kamus[word]
	return ' '.join(tokens)

if __name__ == '__main__':
	kamus = fillKamus('singkatan-lib.csv')
	writeFile('sample/capres2014-2.1.csv', 2, 'sample/output.csv', kamus)