import webcolors as _webcolors


def color_to_rgb(color):
    return _webcolors.name_to_rgb(color)


def rgb_to_color(rgb):
    return _webcolors.rgb_to_name(rgb)


white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)