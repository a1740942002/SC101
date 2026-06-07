"""
File: whack_a_mole.py
Name: 
---------------------------
This program implements a game called "Whack-a-Mole".

In this game, moles randomly pop up on the screen,
and the player clicks on them to earn points.
The program tracks the player's interactions and
updates the score accordingly.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLabel
from campy.graphics.gimage import GImage
from campy.gui.events.mouse import onmouseclicked
from campy.gui.events.timer import pause
import random

# Constants control the diameter of the window
WINDOW_WIDTH = 850
WINDOW_HEIGHT = 550

# Constant controls the pause time of the animation
DELAY = 700

# Global variables
score = 0
window = GWindow(WINDOW_WIDTH, WINDOW_HEIGHT, title="WhackAMole")
label = GLabel(f"Score: {score}")
label.font ="-60"
label.color="red"
window.add(label, x=0, y=label.height)

def main():
    onmouseclicked(remove_mole)

    while score < 10:
        mole = GImage("./mole.png")
        window.add(mole, x=random.randint(0,window.width - mole.width), y=random.randint(0, window.height - mole.height))
        pause(DELAY)

def remove_mole(e):
    # 因為下面有 score += 1（重新賦值），
    # 沒宣告 global 的話 Python 會把 score 當成 local 變數而出錯。
    global score
    maybe_mole = window.get_object_at(e.x, e.y)

    # 如果打到地鼠
    if maybe_mole is not None and maybe_mole is not label:
        window.remove(maybe_mole)
        score += 1
        label.text = f"Score: {score}"



if __name__ == '__main__':
    main()
