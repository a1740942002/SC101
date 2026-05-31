"""
File: blur.py
Name:
-------------------------------
This program first displays the original image,
smiley-face.png, and then compares it with a
blurred version of the image.

The blur effect is created by replacing each
pixel with the average RGB values of its
nearest neighboring pixels.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: SimpleImage, the original image.
    :return: SimpleImage, blurred version image.
    """
    blank = SimpleImage.blank(img.width, img.height)

    for x in range(img.width):
        for y in range(img.height):
            total_red = 0
            total_green = 0
            total_blue = 0
            count = 0

            # 掃過自己 + 周圍 8 格 (3x3)。
            # offset_x, offset_y = 相對於目前 pixel 的位移量:
            #   -1 = 往左/往上一格, 0 = 不動, +1 = 往右/往下一格。
            # 兩層迴圈把 {-1, 0, 1} 兩兩組合, 剛好湊出全部 9 個位置。
            for offset_x in [-1, 0, 1]:
                for offset_y in [-1, 0, 1]:
                    # nx, ny = 鄰居在圖片上的實際座標
                    nx = x + offset_x
                    ny = y + offset_y
                    # 只算還在圖片範圍內的鄰居
                    # (例如在最左邊時, x - 1 會變 -1, 那就超出圖片了)
                    if 0 <= nx < img.width and 0 <= ny < img.height:
                        neighbor = img.get_pixel(nx, ny)
                        total_red += neighbor.red
                        total_green += neighbor.green
                        total_blue += neighbor.blue
                        count += 1

            blank_pixel = blank.get_pixel(x, y)
            blank_pixel.red = total_red // count
            blank_pixel.green = total_green // count
            blank_pixel.blue = total_blue // count

    return blank


def main():
    """
    TODO:
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
