"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')


def main():
    """
    This program simulates a bouncing ball that starts at
    the position (START_X, START_Y).
    The ball moves with an initial x velocity VX and an
    initial y velocity of 0. Each time the ball bounces,
    its y velocity is reduced by a factor defined as REDUCE.
    """
    pass


if __name__ == "__main__":
    main()
