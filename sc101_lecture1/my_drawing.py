"""
File: my_drawing.py
Name:
----------------------
This program uses the campy module to
draw graphical objects on a GWindow.

By creating and placing different shapes,
the program demonstrates how drawing can
be done in a graphical window using campy.
"""

from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.graphics.gwindow import GWindow


def main():
    window = GWindow(800, 500, "MyFace")

    face = GOval(200, 250)
    face.filled = True
    face.fill_color = "pink"

    l_eye = GOval(50, 50)
    l_eye.filled = True

    r_eye = GOval(50, 50)
    r_eye.filled = True

    mouth = GRect(120, 40)
    mouth.filled = True
    mouth.fill_color = "sage"

    label = GLabel("Hello World")
    label.color = "red"
    label.font = "-80"

    window.add(face, x=350, y=200)
    window.add(l_eye, x=390, y=230)
    window.add(r_eye, x=450, y=230)
    window.add(mouth, x=390, y=360)
    window.add(label, x=0, y=label.height)


if __name__ == "__main__":
    main()
