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

# Autorize information, gmail
__author1__ = "daoduylam2020@gmail.com"  # DAO DUY LAM
__author2__ = ""  # PHAM MINH KHOI
__author3__ = ""  # LE CONG TIEN

# ___ MAIN ___

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class MenuView:
    def __init__(self, surface):
        self.surface = surface


class RockPaperScissor:
    def __init__(self):
        self.width = 900
        self.height = 700
        self.screen = pygame.display.set_mode((self.width, self.height))

    def run(self):
        while True:
            # Initialize any object on screen here
            button = uix.Button(self.screen, (100, 100, 100, 100))
            # Event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close()
            self.screen.fill(BLACK)

            button.create()

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
