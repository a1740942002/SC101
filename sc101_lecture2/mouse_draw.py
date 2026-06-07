"""
File: mouse_draw.py
Name:
------------------------
This program demonstrates how to use mouse events
in the campy library to draw GOval objects on a GWindow.

By responding to mouse interactions,
the program allows the user to draw circles dynamically
at different positions on the window.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmousedragged

# This constant controls the size of the pen stroke
SIZE = 30

window = GWindow()


def main():
	onmousedragged(drag)

def drag(event):
	ink = GOval(SIZE, SIZE)
	ink.color = "blue"
	ink.filled = True
	ink.fill_color = "blue"
	window.add(ink, x=event.x - ink.width / 2, y=event.y - ink.height/2)


if __name__ == '__main__':
	main()
