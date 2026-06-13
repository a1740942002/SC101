from campy.graphics.gwindow import GWindow
from robot import Robot

window = GWindow()

def main():
    r1 = Robot(190,110, color="blue")
    r1.self_intro()
    r1.bmi()
    ball_1 = r1.give_me_a_ball(300)

    r2 = Robot(80, 100, color="orange")
    r2.self_intro()
    r2.bmi()
    ball_2 = r2.give_me_a_ball(200)

    window.add(ball_1)
    window.add(ball_2)



if __name__ == "__main__":
    main()