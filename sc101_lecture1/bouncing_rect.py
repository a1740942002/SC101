"""
File: bouncing_rect.py
Name: 
------------------------
This program demonstrates how to create a simple animation
using the campy library.

By repeatedly updating the position of a rectangle, the
program shows how animation can be achieved through
continuous movement and screen refresh.
"""

from campy.graphics.gobjects import GOval, GRect
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause

# This controls the width and height of the rect
SIZE = 30

# This controls the pause time (in millisecond) for the animation
DELAY = 10


def main():
	window = GWindow(500, 500)

	rect1 = setup_rect()
	rect1.location =  (window.width - SIZE) / 2, (window.height - SIZE) / 2

	rect2 = setup_rect()
	rect2.location =  (window.width - SIZE) / 2, (window.height - SIZE) / 2

	window.add(rect1)
	window.add(rect2)

	vx = 5
	vy = 3

	while True:
		# Update
		rect1.move(vx, 0)
		rect2.move(0, vy)
		# Check
		if rect1.x <=0 or rect1.x + rect1.width >= window.width :
			vx = -vx
		if rect2.y <= 0 or rect2.y +rect2.height >= window.height:
			vy = -vy
		# Pause
		pause(DELAY)

def setup_rect():
	rect = GRect(SIZE, SIZE)
	rect.filled = True
	rect.fill_color = "pink"
	return rect

if __name__ == '__main__':
	main()
