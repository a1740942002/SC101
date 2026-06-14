from campy.gui.events.timer import pause
from zonegraphics import ZoneGraphics

FRAME_RATE = 1000 / 120 # 120 frames per second.
NUM_LIVES = 3


def main():
    """
    This program plays a Python game called "Zone".
    A ball continuously bounces around the GWindow. The player
    must defend the zone indicated by a black line at the center
    of the window by clicking on the bouncing ball.
    """
    graphics = ZoneGraphics()
    ball = graphics.ball
    window = graphics.window

    vx = 5
    vy = 3

    while True:
        # update
        ball.move(vx, vy)

        # check
        if ball.x <= 0 or ball.x + ball.width >= window.width:
            vx = -vx

        if ball.y <= 0 or ball.y + ball.height >= window.height:
            vy = -vy

        # pause
        pause(FRAME_RATE)




if __name__ == '__main__':
    main()
