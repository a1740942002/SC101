"""
File: score_book.py
Name: 
----------------------
This program demonstrates how to use a
Python dictionary by implementing a
simple score book.

Scores are stored and managed using
key-value pairs, allowing data to be
organized and accessed efficiently.
"""

# This controls when to break the loop for user inputs
QUIT = ''


def main():
	"""
	This main function contains 3 functions that
	constructing a score book. d is passed by reference
	"""
	d = {}
	get_scores(d)
	check_score(d)
	print_scores(d)
	

def get_scores(d):
	"""
	: param d: (dict) an empty python dict 
	--------------------------------------
	This function adds key-value pairs to the dictionary d.
	"""
	print("Let's input some data!")


def check_score(d):
	"""
	: param d: (dict) a python dict contains name->score
	--------------------------------------
	This function checks whether a specific key exists in the dictionary d.
	"""
	print("Let's check the score!")
	

def print_scores(d):
	"""
	: param d: (dict) a python dict contains name->score
	--------------------------------------
	This function checks whether a specific key exists in the dictionary d.
	"""
	print('-----------------------')
	

if __name__ == '__main__':
	main()
