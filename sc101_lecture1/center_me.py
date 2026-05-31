"""
File: center_me.py
Name:
--------------------------------
This program demonstrates how to center a GRect
within a window when both the width and height
of the rectangle are randomly generated.

By calculating the correct x and y positions,
the rectangle can be placed precisely at the
center of the window regardless of its size.
"""

from campy.graphics.gobjects import GRect
from campy.graphics.gwindow import GWindow


SIZE = 100       # Controls the width and height of the rect
WIDTH = 800      # Controls the width of the window
HEIGHT = 500     # Controls the height of the window


def main():
    """
    Center a magenta rect on the canvas
    where the width and height are SIZE
    """
    window = GWindow(width=WIDTH, height=HEIGHT, title='CenterMe')
    rect = GRect(SIZE, SIZE, x=(window.width-SIZE)/2, y=(window.height-SIZE)/2)
    rect.filled = True
    rect.fill_color = 'magenta'
    rect.color = 'magenta'
    window.add(rect)


if __name__ == '__main__':
    main()
