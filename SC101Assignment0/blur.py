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
    :param img:
    :return:
    """
    pass


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
