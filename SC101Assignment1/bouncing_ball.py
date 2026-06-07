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

# You Code Write Below
count = 0
MAX_COUNT = 3
is_ball_moving = False

def main():
    """
    This program simulates a bouncing ball that starts at
    the position (START_X, START_Y).
    The ball moves with an initial x velocity VX and an
    initial y velocity of 0. Each time the ball bounces,
    its y velocity is reduced by a factor defined as REDUCE.
    """
    setup_ball()
    onmouseclicked(on_click)

def on_click(e):
    global count, is_ball_moving

    # 超過指定次數，不可再進行
    if count >= MAX_COUNT: return
    # 球在彈跳過程中，不會受到使用者滑鼠點擊影響
    if is_ball_moving: return

    # 往下的初始速度為 0
    vy = 0
    maybe_ball = window.get_object_at(e.x, e.y)


    # 有點到 ball 的話
    if maybe_ball is not None:
        # Start Dropping
        is_ball_moving = True
        while is_ball_moving:
            is_hit_floor = maybe_ball.y + maybe_ball.height >= window.height
            is_off_wall = maybe_ball.x >= window.width

            # 每次反彈都會損失動能，並確保碰地後速度一定向上｀
            if is_hit_floor:
                vy = -abs(vy) * REDUCE

            # 球超出右邊邊界，Reset 並記錄使用次數
            if is_off_wall:
                maybe_ball.x = START_X
                maybe_ball.y = START_Y
                count += 1
                is_ball_moving = False
                return

            maybe_ball.move(VX, vy)

            vy = vy + GRAVITY
            pause(DELAY)


def setup_ball():
    ball = GOval(SIZE, SIZE)
    ball.filled = True
    ball.fill_color = "black"
    window.add(ball, x=START_X, y=START_Y)



if __name__ == "__main__":
    main()
