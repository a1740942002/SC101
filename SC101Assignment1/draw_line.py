"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

window = GWindow(title="Draw Line")
count = 0
start_x = 0
start_y = 0
cursor = None

POINTER_SIZE = 25

def main():
    """
    This program creates line objects on a GWindow.
    A circle is displayed to indicate the user's first mouse click.
    When the user clicks on the canvas for the second time, the circle
    disappears and a line is drawn between the two clicked positions.
    """
    onmouseclicked(on_click)

def on_click(e):
    global count
    global start_x
    global start_y
    global cursor

    count += 1

    # 奇數
    if count % 2 == 1:
        start_x = e.x
        start_y = e.y
        cursor = GOval(POINTER_SIZE, POINTER_SIZE)
        window.add(cursor, x=e.x - cursor.width/2, y=e.y - cursor.height / 2)

    # 偶數
    else:
        line = GLine(start_x, start_y, e.x, e.y)
        window.add(line)
        if cursor is not None:
            window.remove(cursor)


if __name__ == "__main__":
    main()
