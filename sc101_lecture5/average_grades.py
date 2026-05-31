"""
File: average_grades.py
Name: 
-------------------------
This program stores a collection of scores in a Python list
and calculates the average value of all the elements.

By iterating through the list and summing the scores, the
program demonstrates how lists can be used to manage and
process multiple data values.
"""

# Constant
EXIT = -1  # Controls when to break the loop of score input


def main():
	"""
	This program asks inputs from users 
	"""
	print(f"This program averages the input(s), or {EXIT} to exit")
	
	lst = []
	# TODO: Add values to lst 
	
	print('The average:', average_by_index(lst))
	print('The average:', average_by_for_each(lst))


def average_by_index(scores):
	"""
	:param scores: (list) Containing all the scores input by user
	:return : (float) The average of the elements in scores
	----------------------------------------------
	This function calculates the average score by iterating
	through the list using indices in a for loop.
	"""
	pass


def average_by_for_each(scores):
	"""
	:param scores: (list) Containing all the scores input by user
	:return : (float) The average of the elements in scores
	----------------------------------------------
	This function calculates the average score by iterating
	through the list using a for-each loop.
	"""
	pass


if __name__ == '__main__':
	main()
