"""
Rock Paper Scissor Game GUI Application

The program is used some of the libraries which are installed from PyPI (Python Package Index)

Developed by DAO DUY LAM, PHAM MINH KHOI, LE CONG TIEN
"""
# Python Package Index
import pygame

# System Module and Libraries
import sys
import uix
import scripts
import networking
from scripts import Color

# Authorize information, gmail
__author1__ = "daoduylam2020@gmail.com"  # DAO DUY LAM
__author2__ = ""  # PHAM MINH KHOI
__author3__ = ""  # LE CONG TIEN


# ___ MAIN ___
FPS = 30


def update():
    print("Hello")


class MenuView:
    def __init__(self, surface):
        self.surface = surface
        height = 70
        width = 300
        x = self.surface.get_width()/2 - width/2

        self.nameInputText = uix.InputBox(self.surface, (x, 300, width, height))
        self.singlePlayerButton = uix.Button(self.surface, (x, 500, width, height), text="Single Player")
        self.multiPlayerButton = uix.Button(self.surface, (x, 400, width, height), text="Multi Player")

        self.group = uix.GroupWidget()
        self.group.widgets.append(self.nameInputText)
        self.group.widgets.append(self.singlePlayerButton)
        self.group.widgets.append(self.multiPlayerButton)

    def update(self, events):
        self.group.update(events)

    def create(self):
        self.group.create_widget()


class SinglePlayerView:
    def __init__(self, surface):
        self.surface = surface
        self.group = uix.GroupWidget()

        self.rockButton = uix.Button(self.surface, (100, 100, 200, 30))
        self.group.widgets.append(self.rockButton)

    def update(self, events):
        self.group.update(events)

    def create(self):
        self.group.create_widget()


class MultiPlayerView:
    def __init__(self, surface):
        self.surface = surface
        self.group = uix.GroupWidget()

    def update(self, events):
        self.group.update(events)

    def create(self):
        self.group.create_widget()


class RockPaperScissor:
    def __init__(self):
        self.width = 900
        self.height = 700
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.clock = pygame.time.Clock()

        self.openMenu = True
        self.openMultiView = False
        self.openSingleView = False

        # Main widgets which contain all widget on screen but at first it's empty
        # You have to add your own widget after creating it
        # Use this code to add widget: self.groupWidgets.widgets.append(<widget>)
        self.groupWidgets = uix.GroupWidget()

        # Initialize any view on screen here
        self.menuView = MenuView(self.screen)
        self.menuView.singlePlayerButton.on_press_action = self.open_single_view
        self.menuView.multiPlayerButton.on_press_action = self.open_multi_view

        self.singleView = SinglePlayerView(self.screen)

        self.multiView = MultiPlayerView(self.screen)
        # Initialize any object on screen here

    def run(self):
        while True:
            # Fill the screen with BLACK instead of an empty screen
            self.screen.fill(Color.black)

            # Event
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.close()

            # Update all widget on screen (GroupWidgets optimize your code by add all widget into a list
            # Then update itself once
            self.groupWidgets.update(events)
            if self.openMenu:
                self.menuView.update(events)
                self.menuView.create()
            elif self.openMultiView:
                self.multiView.update(events)
                self.multiView.create()
            elif self.openSingleView:
                self.singleView.update(events)
                self.singleView.create()

            # Create all widget on screen
            self.groupWidgets.create_widget()

            # Update and set FPS
            self.clock.tick(FPS)

            pygame.display.flip()
            pygame.display.update()

    def close(self):
        pygame.quit()
        sys.exit()

    def open_single_view(self):
        if self.menuView.nameInputText.text != "":
            self.openMenu = False
            self.openMultiView = True
            self.openSingleView = False

    def open_multi_view(self):
        self.openMenu = False
        self.openMultiView = False
        self.openSingleView = True

    def open_menu_view(self):
        self.openMenu = True
        self.openMultiView = False
        self.openSingleView = False


if __name__ == "__main__":
    game = RockPaperScissor()
    try:
        game.run()
    except Exception as bug:
        print(bug)
        game.close()
