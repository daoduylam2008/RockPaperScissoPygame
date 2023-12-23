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

        self.layer = {
            'Main Menu': True,
            'Play Menu': True,
            'Settings Menu': False,
            'Back': True
        }

        self.count = 0


        # Main widgets which contain all widget on screen but at first it's empty
        # You have to add your own widget after creating it
        # Use this code to add widget: self.groupWidgets.widgets.append(<widget>)
        
        #GroupWidget 
        self.groupWidget = uix.GroupWidget()
        self.groupWidget_single = uix.GroupWidget()
        # Initialize any view on screen here
        self.button_play = uix.Button(self.screen, (self.width//160,300, 150, 60),text = 'Play',color= (32,178,170),bottom_rect_color=(255,255,255))
        self.button_setting = uix.Button(self.screen,(self.width//160,400,200,60),text = 'Settings',color= (32,178,170),bottom_rect_color=(255,255,255))

        #Single Button
        self.button_rock = uix.Button(self.screen,(300,400,50,50),'Rock',(180,180,180),(120,120,120))
        self.button_paper = uix.Button(self.screen,(400,400,50,50),'Paper',(180,180,180),(120,120,120))
        self.button_scissors = uix.Button(self.screen,(500,400,50,50),'Scissors',(180,180,180),(120,120,120))
        
        
        #Back Button
        self.button_back = uix.Button(self.screen,(0,0,70,70),'Back',(220,220,220),(95,95,95))   


        #Widgets for button rock paper scissors
        self.groupWidget_single.widgets.append(self.button_rock)
        self.groupWidget_single.widgets.append(self.button_paper)
        self.groupWidget_single.widgets.append(self.button_scissors)
        self.groupWidget_single.widgets.append(self.button_back)

        #Widgets for button play settings
        self.groupWidget.widgets.append(self.button_play)
        self.groupWidget.widgets.append(self.button_setting)

        
    def run(self):

        while True:
            # Fill the screen with BLACK instead of an empty screen
            self.screen.fill('black')

            # Event
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.close()


        
            # Update all widget on screen (GroupWidgets optimize your code by add all widget into a list
            # Then update itself once
            
            # print(self.layer['Back'],self.button_back.access)

            
                
            if self.button_play.clicked:
                self.groupWidget_single.create_widget()
                self.groupWidget_single.update(events)
                self.layer['Main Menu'] = False
            if self.button_back.clicked:
                
                self.layer['Main Menu'] = True
                
            if self.layer['Main Menu']:
                self.groupWidget.update(events)
                self.groupWidget.create_widget()



            
            



           



            if self.layer['Settings Menu']:
                pass

            # print(self.layer['Play Menu'],self.layer['Back'])
            
                
        


            # self.layer['Play Menu']= self.button_play.clicked
            # self.layer['Back'] = self.button_back.clicked

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
