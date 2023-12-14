import pygame


class Button:
    def __init__(self,
                 surface,
                 rect: tuple,
                 mouse_pos: tuple,
                 event,
                 text="",
                 color=(180, 180, 180),
                 press_color=(100, 100, 100),
                 on_touch_color=(150, 150, 150),
                 ):
        self.surface = surface
        self.rect = pygame.Rect(rect[0], rect[1], rect[2], rect[3])
        self.mouse_pos = mouse_pos
        self.event = event
        self.text = text
        self.color = color
        self.press_color = press_color
        self.on_touch_color = on_touch_color

    def on_touch(self): pass

    def on_press(self): pass

    def on_release(self): pass
