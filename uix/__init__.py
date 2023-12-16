import pygame

pygame.init()


class Button:
    def __init__(self,
                 surface,
                 rect: tuple,
                 text="Button",
                 color=(180, 180, 180),
                 on_press_color=(50, 50, 50),
                 on_release_color=(150, 150, 150),
                 on_touch_color=(150, 150, 150),
                 text_color=(0, 0, 0),
                 on_press_action=...,
                 on_release_action=...,
                 on_touch_action=...,
                 button=1,
                 alignment="center",
                 ):
        self.surface = surface
        self.rect = pygame.Rect(rect[0], rect[1], rect[2], rect[3])

        self.color = color
        self.on_press_color = on_press_color
        self.on_release_color = on_release_color
        self.on_touch_color = on_touch_color
        self.text_color = text_color

        self.text = self._textForButton(text)

        self.on_press_action = on_press_action
        self.on_release_action = on_release_action
        self.on_touch_action = on_touch_action

        self.button = button

        self.alignment = alignment

    def create(self):
        mouse_pos = pygame.mouse.get_pos()

        x, y = self._alignment(self.alignment)

        if self.rect.collidepoint(mouse_pos):
            if self.button == 1:
                if pygame.mouse.get_pressed()[0]:
                    pygame.draw.rect(self.surface, self.on_press_color, self.rect)
                else:
                    pygame.draw.rect(self.surface, self.on_touch_color, self.rect)
            elif self.button == 0:
                if pygame.mouse.get_pressed()[1]:
                    pygame.draw.rect(self.surface, self.on_press_color, self.rect)
                else:
                    pygame.draw.rect(self.surface, self.on_touch_color, self.rect)
        else:
            pygame.draw.rect(self.surface, self.color, self.rect)

        self.surface.blit(self.text, (x, y))

    def _alignment(self, alignment):
        if alignment == "center":
            x = self.rect.x + (self.rect.width - self.text.get_width()) / 2
            y = self.rect.y + (self.rect.height - self.text.get_height()) / 2
        elif alignment == "left":
            x = self.rect.x
            y = self.rect.y + (self.rect.height - self.text.get_height()) / 2
        elif alignment == "right":
            x = self.rect.x + self.rect.width - self.text.get_width()
            y = self.rect.y + (self.rect.height - self.text.get_height()) / 2
        elif alignment == "top":
            x = self.rect.x + (self.rect.width - self.text.get_width()) / 2
            y = self.rect.y
        elif alignment == "bottom":
            x = self.rect.x + (self.rect.width - self.text.get_width()) / 2
            y = self.rect.y + self.rect.height - self.text.get_height()
        elif alignment == "top-left":
            x = self.rect.x
            y = self.rect.y
        elif alignment == "top-right":
            x = self.rect.x + self.rect.width - self.text.get_width()
            y = self.rect.y
        elif alignment == "bottom-left":
            x = self.rect.x
            y = self.rect.y + self.rect.height - self.text.get_height()
        elif alignment == "bottom-right":
            x = self.rect.x + self.rect.width - self.text.get_width()
            y = self.rect.y + self.rect.height - self.text.get_height()
        else:
            x = 0
            y = 0
        return x, y

    def _textForButton(self, text):
        font = pygame.font.SysFont('timesnewroman', 30)
        txt = font.render(text, True, self.text_color)
        return txt


class Input:
    pass
