import pygame


class Button:
    def __init__(self,
                 surface,
                 rect: tuple,
                 mouse_pos: tuple,
                 event=...,
                 text="",
                 color=(180, 180, 180),
                 press_color=(100, 100, 100),
                 on_touch_color=(150, 150, 150),
                 text_color=(0, 0, 0)
                 ):
        self.surface = surface
        self.rect = pygame.Rect(rect[0], rect[1], rect[2], rect[3])
        self.mouse_pos = mouse_pos
        self.event = event
        self.text = self._textForButton(text)
        self.color = color
        self.press_color = press_color
        self.on_touch_color = on_touch_color
        self.text_color = text_color

    def create(self):
        pygame.draw.rect(self.surface, self.color)

    def on_touch(self, event) -> bool:
        self.event = event
        if self.rect.collidepoint(self.mouse_pos):
            return True
        else:
            return False

    def _textForButton(self, text):
        font = pygame.font.Font("times new roman", 15)
        txt = font.render(text, True, self.text_color)
        return txt

    def on_press(self, event, button) -> bool:
        """
        button variable contained 0 (for left button), 1 (for right button)
        :param self:
        :param event:
        :param button:
        :return:
        """
        self.event = event
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == button:
                if self.rect.collidepoint(self.mouse_pos):
                    return True
                else:
                    return False

    def on_release(self, event, button):
        """
        button variable contained 0 (for left button), 1 (for right button)
        :param event:
        :param button:
        :return:
        """
        self.event = event
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == button:
                if self.rect.collidepoint(self.mouse_pos):
                    return True
                else:
                    return False
