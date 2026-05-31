"""
File: pass_by_value.py
Name:
--------------------------
This program demonstrates the concept of
pass-by-value in computer memory.

Through this example, students can observe
that changing a value inside a function
does not affect the original value outside
the function.
"""


def main():
	print('--------------')
	a = 0
	plus_one(a)
	print(a)
	print('--------------')


def plus_one(a):
	"""
	: param a: int, the number passed from main()
	"""
	a += 1


if __name__ == '__main__':
	main()