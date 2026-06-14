from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect
from campy.gui.events.mouse import onmouseclicked
from random import randint

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
ZONE_WIDTH = 100
ZONE_HEIGHT = 100
BALL_RADIUS = 15
MAX_SPEED = 6
MIN_Y_SPEED = 2


class ZoneGraphics:

    def __init__(self, window_width=WINDOW_WIDTH, window_height=WINDOW_HEIGHT,
                 zone_width=ZONE_WIDTH, zone_height=ZONE_HEIGHT, ball_size=BALL_RADIUS*2,ball_radius=BALL_RADIUS):
        # Create window
        window = GWindow(window_width, window_height)

        # Create zone
        zone = GRect(zone_width, zone_height)
        zone.color="red"

        # Create ball and initialize velocity/position
        ball = GOval(ball_size, ball_size)
        ball.filed = True
        ball.fill_color="black"

        # Initialize mouse listeners
        onmouseclicked(self.hanldemouseclicked)

        self._window = window
        self._zone = zone
        self._ball = ball

        window.add(ball)
        window.add(zone, x=window_width/2 - zone_width/2, y=window_height/2 - zone_height/2)
        self.random_ball_position()

    def hanldemouseclicked(self):
        self._ball.move()

    def random_ball_position(self):
        self._ball.x =randint(0, self._window.width - self._ball.width)
        self._ball.y =randint(0, self._window.height - self._ball.height)

    @property
    def ball(self):
        return self._ball

    @property
    def window(self):
        return self._window
