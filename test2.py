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


class MenuView:
    def __init__(self, surface):
        self.surface = surface
        width = 50
        x = self.surface.get_width()/2 - width/2
        self.singlePlayerButton = uix.Button(self.surface, (x, 100, 200, 50))

    def update(self, events):
        pass

    def create(self):
        self.singlePlayerButton.create()


class SinglePlayerView:
    def __init__(self):
        pass


class MultiPlayerView:
    def __init__(self):
        pass


class RockPaperScissor:
    def __init__(self):
        self.width = 900
        self.height = 700
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.clock = pygame.time.Clock()

        # Main widgets which contain all widget on screen but at first it's empty
        # You have to add your own widget after creating it
        # Use this code to add widget: self.groupWidgets.widgets.append(<widget>)
        self.groupWidgets = uix.GroupWidget()

        # Initialize any view on screen here
        self.menuView = MenuView(self.screen)
        self.groupWidgets.widgets.append(self.menuView)

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

            # Create all widget on screen
            self.groupWidgets.create_widget()

            # Update and set FPS
            self.clock.tick(FPS)

            pygame.display.flip()
            pygame.display.update()

    def close(self):
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = RockPaperScissor()
    try:
        game.run()
    except Exception as bug:
        print(bug)
        game.close()
