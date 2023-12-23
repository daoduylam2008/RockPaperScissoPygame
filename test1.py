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

#Color

# Authorize information, gmail
__author1__ = "daoduylam2020@gmail.com"  # DAO DUY LAM
__author2__ = ""  # PHAM MINH KHOI
__author3__ = ""  # LE CONG TIEN


# ___ MAIN ___
FPS = 30


class MenuView:
    def __init__(self, surface):
        pass


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

        self.layer  = {
            'Main Menu': True,
            'Play Menu': False,
            'Settings Menu': False
        }



        # Main widgets which contain all widget on screen but at first it's empty
        # You have to add your own widget after creating it
        # Use this code to add widget: self.groupWidgets.widgets.append(<widget>)
        self.groupWidget = uix.GroupWidget()
        # Initialize any view on screen here
        self.button_play = uix.Button(self.screen, (self.width//160,300, 150, 60),text = 'Play',color= (32,178,170),bottom_rect_color=(255,255,255))
        self.button_setting = uix.Button(self.screen,(self.width//160,400,200,60),text = 'Settings',color= (32,178,170),bottom_rect_color=(255,255,255))

        #Play
        self.button_bua = uix.Button(self.screen,(200,100,50,50),'Búa',(180,180,180),(120,120,120))
        self.button_bao = uix.Button(self.screen,(400,100,50,50),'Bao',(180,180,180),(120,120,120))
        self.button_keo = uix.Button(self.screen,(600,100,50,50),'Kéo',(180,180,180),(120,120,120))

        # Initialize any object on screen here
        if self.layer['Main Menu']:
            self.groupWidget.widgets.append(self.button_play)
            self.groupWidget.widgets.append(self.button_setting)

    def run(self):

        while True:
            # Fill the screen with BLACK instead of an empty screen
            self.screen.fill('black')
            self.layer['Play Menu'] = self.button_play.access


            # Event
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.close()


            if self.layer['Play Menu']:
                self.groupWidget.widgets.clear()

            # Update all widget on screen (GroupWidgets optimize your code by add all widget into a list
            # Then update itself once
            self.groupWidget.update(events)

            # Create all widget on screen
            self.groupWidget.create_widget()



            # Update and set FPS
            self.clock.tick(FPS)
            # self.screen.blit(self.layer1,(0,0))

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
