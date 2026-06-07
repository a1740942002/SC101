"""
File: hole_puncher.py
Name:
------------------------
This program demonstrates how to use mouse events
in the campy library to interact with a GWindow.

By responding to mouse clicks, the program creates circular holes
(GOval objects) at the clicked locations on the window.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# This constant controls the size of the hole
SIZE = 30


window = GWindow(500, 500)

def main():
	onmouseclicked(create_hole)

def create_hole(event):
	hole = GOval(SIZE, SIZE)
	hole.filled = True
	window.add(hole, x=event.x - SIZE/2, y=event.y - SIZE/2)


if __name__ == '__main__':
	main()
