import pygame as _pygame
import pygame.image
from pygame.sprite import Sprite as _Sprite
import os

_pygame.init()

FPS = 60

class Widget:
    def __init__(self, surface, rect):
        self.surface = surface
        self.rect = _pygame.Rect(rect)

    def update(self, events):
        pass

    def create(self):
        pass


class GroupWidget:
    def __init__(self,
                 widgets=None):
        if widgets is None:
            widgets = []
        self.widgets = widgets

    def update(self, events):
        for widget in self.widgets:
            try:
                widget.update(events)
            except Exception as bug:
                print(bug)
                print("There is no widget or your widget is not recognize as Widget")

    def create_widget(self):
        for widget in self.widgets:
            try:
                widget.create()
            except Exception as bug:
                print(bug)
                print("There is no widget or your widget is not recognize as Widget")


class Text(Widget):
    def __init__(self,
                 surface,
                 rect,
                 text="text",
                 size = 32,
                 color=(0,0,0)
                 ):
        super().__init__(surface, rect)
        self.text = text
        self.color = color
        self.size = size

    def create(self,text):
        self.text = text
        self._txt = self.font()
        self.surface.blit(self._txt, self.rect)

    def font(self):
        self._font = _pygame.font.Font(None, self.size)
        self._txt = self._font.render(self.text, True, self.color)
        return self._txt


class Button(Widget):
    def __init__(self,
                 surface,
                 rect: tuple,
                 text="Button",
                 color=(180, 180, 180),
                 on_touch_color=(150, 150, 150),
                 bottom_rect_color=(0,0,0),
                 text_color=(255, 255, 255),
                 on_press_action=...,
                 on_touch_action=...,
                 button=1,
                 alignment="center",
                 text_size=30,
                 elevation = 6,
                 border_radius = 10
                 ):
        super().__init__(surface, rect)

        self.original_color = color
        self.color = color
        self.on_touch_color = on_touch_color
        self.text_color = text_color

        self.text_size = text_size

        self.text = self.textForButton(text)

        self.on_press_action = on_press_action
        self.on_touch_action = on_touch_action

        self.button = button

        self.alignment = alignment

        #Make the elevation for button
        self.elevation = elevation
        self.border_radius = border_radius

        #The bottom rectangle under the top rectangle
        self.bottom_rect = pygame.Rect(rect)
        self.bottom_rect_color = bottom_rect_color

        self.access = False

    def create(self):
        mouse_pos = _pygame.mouse.get_pos()
        start_time,time = 110,0
        timing = pygame.time.get_ticks()

        x, y = self._alignment(self.alignment)

        self.bottom_rect.center = self.rect.center
        self.bottom_rect.y = self.rect.y + self.elevation + 2

        if self.rect.collidepoint(mouse_pos):
            if _pygame.mouse.get_pressed()[0]:
                #
                self.rect.y += self.elevation

                y += 3
                _pygame.draw.rect(self.surface, self.bottom_rect_color, self.bottom_rect,border_radius=self.border_radius)
                _pygame.draw.rect(self.surface, self.color,self.rect,border_radius=self.border_radius)

                if timing - time > start_time:
                    time = timing
                    self.rect.y -= self.elevation


            else:
                _pygame.draw.rect(self.surface, self.bottom_rect_color, self.bottom_rect, border_radius=self.border_radius)
                _pygame.draw.rect(self.surface, self.color, self.rect,border_radius=self.border_radius)

        else:
            _pygame.draw.rect(self.surface, self.bottom_rect_color, self.bottom_rect, border_radius=self.border_radius)
            _pygame.draw.rect(self.surface, self.color, self.rect,border_radius=self.border_radius)

            try:
                self.on_touch_action()
            except: pass

        self.surface.blit(self.text, (x, y))

    def update(self, events):
        mouse_pos = _pygame.mouse.get_pos()

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == self.button:
                    if self.rect.collidepoint(mouse_pos):
                        if pygame.mouse.get_pressed()[0]:
                            self.on_press_action()


        

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

    def textForButton(self, text):
        font = _pygame.font.SysFont('timesnewroman', self.text_size)
        txt = font.render(text, True, self.text_color)

        return txt


class InputBox(Widget):

    def __init__(self,
                 surface,
                 rect,
                 text='',
                 action=None
                 ):
        super().__init__(surface, rect)

        self._COLOR_INACTIVE = _pygame.Color('lightskyblue3')
        self._COLOR_ACTIVE = _pygame.Color('dodgerblue2')
        self._FONT = _pygame.font.Font(None, self.rect.height-20)

        self.color = self._COLOR_INACTIVE

        self.text = text
        self.txt_surface = self._FONT.render(text, True, self.color)

        self.active = False

        self.action = action

    def _update(self):
        # Resize the box if the text is too long.
        width = max(300, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def update(self, events):
        for event in events:
            if event.type == _pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if self.rect.collidepoint(event.pos):
                    # Toggle the active variable.
                    self.active = not self.active
                else:
                    self.active = False

                # Change the current color of the input box.
                self.color = self._COLOR_ACTIVE if self.active else self._COLOR_INACTIVE
            if event.type == _pygame.KEYDOWN:
                if self.active:
                    if event.key == _pygame.K_RETURN:
                        self.text = ''
                        try:
                            self.action()
                        except: pass
                    elif event.key == _pygame.K_BACKSPACE:
                        self.text = self.text[:-1]
                    else:
                        self.text += event.unicode
                    # Re-render the text.
                    self.txt_surface = self._FONT.render(self.text, True, self.color)

    def create(self):
        # Update input box's width
        self._update()

        # Blit the text.
        self.surface.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))

        # Blit the rect.
        _pygame.draw.rect(self.surface, self.color, self.rect, 2)

    def reset_text(self):
        self.text = self.text[:-1]


class Image(Widget):
    def __init__(self,
                 surface,
                 path,
                 pos: tuple,
                 view=None,
                 animation=None
                 ):
        super().__init__(surface, pos)
        self.view = view

        self._resizable = False
        self.path = path


        self.image = _pygame.image.load(self.path).convert_alpha()

        self.action = None

    def create(self):
        self.surface.blit(self.image,self.rect)

    
    def scaleToFill(self, view="surface"):
        if view == "surface" and self._resizable:
            self.image = _pygame.transform.scale(self.image, (self.surface.get_width(), self.surface.get_height()))
        elif view == "view" and self._resizable:
            pass

    def onTap(self, action):
        self.action = action

    def update(self, events):
        mouse_pos = _pygame.mouse.get_pos()
        for event in events:
            if event.type == _pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(mouse_pos):
                    try:
                        self.action()
                    except: pass

    def frame(self, width=0, height=0):
        if self._resizable:
            pass


class _SpriteImage(_Sprite):
    def __init__(self, imageFolder, rect,scale,flip,fps):
        self.clock = pygame.time.Clock()

        super(_SpriteImage, self).__init__()

        self.imageFolder = os.listdir(imageFolder)
        self.images = []

        self.fps = fps

        self.scale = scale
        self.flip = flip

        for i in self.imageFolder:
            self.img = pygame.image.load(imageFolder+i)
            self.img = pygame.transform.scale(self.img,self.scale)
            self.img= pygame.transform.flip(self.img,self.flip,False)
            self.images.append(self.img)   

        self.index = 0

        self.image = self.images[self.index]
        
        self.rect = _pygame.Rect(rect)


    def update(self,imageFolder):
        

        self.clock.tick(self.fps)

        self.images.clear()
        self.imageFolder = os.listdir(imageFolder)
        for i in self.imageFolder:
            self.img = pygame.image.load(imageFolder+i)
            self.img = pygame.transform.scale(self.img,self.scale)
            self.img = pygame.transform.flip(self.img,self.flip,False)
            self.images.append(self.img)


        self.index += 0.2

        if self.index >= len(self.images):
            self.index = len(self.images)-1
        self.image = self.images[int(self.index)]


    def returnIndex(self):
        self.index = 0
        


class ImageAnimation(Widget):
    def __init__(self, surface, rect=None, imageFolder=None,scale = None,flip = None,fps = None):
        super().__init__(surface, rect)

        if imageFolder is None:
            imageFolder = ''
        self.imageFolder = imageFolder
        self.scale = scale
        self.flip = flip
        self.fps = fps
        self._imageSprite = _SpriteImage(self.imageFolder, self.rect,scale = self.scale,flip = self.flip,fps = self.fps)
        self._groupSprite = pygame.sprite.Group(self._imageSprite)

    def update(self, events):
        self._groupSprite.update(self.imageFolder)

    def create(self):
        self._groupSprite.draw(self.surface)

