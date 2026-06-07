"""
File: mouse_tracker.py
Name:
------------------------
This program demonstrates how to use mouse events in the campy library to
track mouse movement and draw GOval objects on a GWindow.

By responding to mouse motion events,
the program continuously updates the position
of a circle to follow the mouse cursor.
"""

from campy.graphics.gobjects import GRect
from campy.graphics.gwindow import GWindow, pause
from campy.gui.events.mouse import onmousemoved

# This constant controls the size of the GRect
SIZE = 100

window = GWindow()
rect = GRect(SIZE, SIZE)

def main():
	window.add(rect)
	onmousemoved(move_handler)

def move_handler(e):
	rect.location = e.x - rect.width/2, e.y - rect.height/2

if __name__ == '__main__':
	main()
