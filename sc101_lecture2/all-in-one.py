from campy.graphics.gobjects import GRect
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmousedragged, onmouseclicked, onmousemoved


window = GWindow()

SIZE = 50

follower = GRect(SIZE, SIZE)
follower.filled = True
window.add(follower)


def main():
    onmouseclicked(create_ink)
    onmousedragged(create_ink)
    onmousemoved(follow_mouse)

def follow_mouse(e):
    follower.location = e.x - follower.width / 2, e.y - follower.height / 2

def create_ink(e):
    ink = GRect(SIZE, SIZE)
    ink.filled = True
    window.add(ink, x=e.x - ink.width/2, y=e.y - ink.height/2)

if __name__ == '__main__':
    main()
