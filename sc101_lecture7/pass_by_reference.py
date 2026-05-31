"""
File: pass_by_reference.py
Name:
-------------------------------
This program demonstrates the concept of
pass-by-reference by showing how changing
the color of a GRect affects the original object.

Through this example, students can observe
that modifying an object inside a function
will also change it outside the function.
"""

from campy.graphics.gobjects import GRect
from campy.graphics.gwindow import GWindow

window = GWindow()


def main():
	rect = GRect(100, 100)
	rect.filled = True
	rect.fill_color = 'green'
	window.add(rect, 0, 0)
	change_color(rect)


def change_color(rect):
	rect.fill_color = 'magenta'


if __name__ == '__main__':
	main()
