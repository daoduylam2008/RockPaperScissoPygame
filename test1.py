"""
Rock Paper Scissor Game GUI Application

The program is used some of the libraries which are installed from PyPI (Python Package Index)

Developed by DAO DUY LAM, PHAM MINH KHOI, LE CONG TIEN
"""
# Python Package Index
import pygame

# System Module and Libaries
import sys
import uix
import scripts
from scripts import Color

# Authorize information, gmail
__author1__ = "daoduylam2020@gmail.com"  # DAO DUY LAM
__author2__ = ""  # PHAM MINH KHOI
__author3__ = ""  # LE CONG TIEN

# ___ MAIN ___


class RockPaperScissor:
    def __init__(self):
        self.width = 900
        self.height = 700
        self.screen = pygame.display.set_mode((self.width, self.height))

        # Main widgets which contain all widget on screen but at first it's empty
        # You have to add your own widget after creating it
        # Use this code to add widget: self.groupWidgets.widgets.append(<widget>)
        self.groupWidgets = uix.GroupWidget()

        # Initialize any object on screen here
        self.button = uix.Button(self.screen, (100, 200, 300, 100), on_press_action=self.action)
        self.groupWidgets.widgets.append(self.button)

        self.inputBox = uix.InputBox(self.screen, (50, 50, 100, 30))
        self.groupWidgets.widgets.append(self.inputBox)

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

            pygame.display.flip()
            pygame.display.update()

    def close(self):
        pygame.quit()
        sys.exit()

    def action(self): print("Hello")


if __name__ == "__main__":
    game = RockPaperScissor()
    try:
        game.run()
    except Exception as bug:
        print(bug)
        game.close()
