"""
File:
Name:
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GArc, GPolygon
from campy.graphics.gwindow import GWindow

window = GWindow(500, 400)

def main():
    """
    Title: 史努比

    左臉被蜜蜂叮到腫起來的史努比
    """

    # 臉
    top_face = create_oval(100,100)
    window.add(top_face, x=205, y=110)

    left_face = create_oval(100, 100)
    window.add(left_face, x=160, y=130)

    mid_face = create_rect(100,77, color="white", fill_color="white")
    window.add(mid_face, x=200, y=152)

    # 耳朵
    ear = create_oval(50, 100)
    window.add(ear, x=265, y=140)

    inner_eye = create_oval(35,70, color="black", fill_color="black")
    window.add(inner_eye, x=275, y=165)

    # 身體
    upper_body = GPolygon()
    # 左頂點
    upper_body.add_vertex((220, 260))
    # 右頂點
    upper_body.add_vertex((280, 260))
    # 中頂點
    upper_body.add_vertex((250, 205))
    upper_body.filled = True
    upper_body.fill_color = "white"
    upper_body.color="white"
    window.add(upper_body)

    # 眼睛
    left_eye = create_oval(5,10, color="black", fill_color="black")
    window.add(left_eye, x=220, y=150)

    right_eye = create_oval(5,10, color="black", fill_color="black")
    window.add(right_eye, x=240, y=150)

    # 眉毛
    left_eyebrow = GArc(30,30, 0, 90)
    window.add(left_eyebrow, x=210, y=115)

    right_eyebrow = GArc(30,30, 0, 90)
    window.add(right_eyebrow, x=230, y=115)

    # 鼻子
    nose = create_oval(15,10, color="black", fill_color="black")
    window.add(nose, x=190, y=170)

    # 嘴巴
    mouth = GArc(65,40, 160, 180)
    window.add(mouth, x=200, y=190)

    # 項圈
    necklace = create_rect(38,4, fill_color="red", color="red")
    window.add(necklace, x=231, y=235)


def create_oval(width, height, color="white", fill_color="white"):
    oval = GOval(width, height)
    oval.filled = True
    oval.color = color
    oval.fill_color = fill_color
    return oval

def create_rect(width, height, color="white", fill_color="white"):
    rect = GRect(width, height)
    rect.filled = True
    rect.color = color
    rect.fill_color = fill_color
    return rect


if __name__ == '__main__':
    main()
