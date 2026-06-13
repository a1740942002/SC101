from campy.graphics.gobjects import GOval


class Robot:
    def __init__(self, height, weight, color="green"):
        self.h = height
        self.w = weight
        self.c = color

    def give_me_a_ball(self, size):
        ball = GOval(size, size)
        ball.color = self.c
        ball.filled = True
        ball.fill_color = self.c
        return ball

    def self_intro(self):
        print(f"h: {self.h}/w={self.w}")

    def bmi(self):
        # weight(kg)/height(m)**2
        h_in_meter = self.h/100
        print("bmi:", self.w / h_in_meter ** 2)
