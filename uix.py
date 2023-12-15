import pygame

pygame.init()


class Button:
    def __init__(self,
                 surface,
                 rect: tuple,
                 text="",
                 color=(180, 180, 180),
                 on_press_color=(50, 50, 50),
                 on_release_color=(150, 150, 150),
                 on_touch_color=(150, 150, 150),
                 text_color=(0, 0, 0),
                 on_press_action=...,
                 on_release_action=...,
                 on_touch_action=...,
                 button=1
                 ):
        self.surface = surface
        self.rect = pygame.Rect(rect[0], rect[1], rect[2], rect[3])

        self.color = color
        self.on_press_color = on_press_color
        self.on_release_color = on_release_color
        self.on_touch_color = on_touch_color
        self.text_color = text_color

        self.text = self._textForButton(text)

        self.leftButton = 1
        self.rightButton = 0

        self.on_press_action = on_press_action
        self.on_release_action = on_release_action
        self.on_touch_action = on_touch_action
        self.button = button

    def create(self):
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.surface, self.on_touch_color, self.rect)
            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if event.button == self.button:
                        pygame.draw.rect(self.surface, self.on_press_color, self.rect)
                        print(123)
        else:
            pygame.draw.rect(self.surface, self.color, self.rect)

    def _textForButton(self, text):
        font = pygame.font.SysFont('timesnewroman', 30)
        txt = font.render(text, True, self.text_color)
        return txt


class Input:
    pass
