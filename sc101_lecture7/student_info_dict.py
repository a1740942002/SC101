"""
File: student_info_dict.py
------------------------------
This program reads data from a text file and
organizes it into a nested data structure.

Each student's name is used as a key in the
outer dictionary, and the corresponding value
is another dictionary that stores detailed
information about the student.
"""


# The file name of our target text file
FILE = 'students_info.txt'


def main():
	all_d = {}
	######################







	######################
	print_out_d(all_d)


def print_out_d(d):
	"""
	: param d: (dict) key of type str is the name of student
				value of type dict is the info of the student
	---------------------------------------------------------------
	This function prints the entire nested data structure to the console.
	"""
	pass




if __name__ == '__main__':
	main()