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
    def __init__(self, surface,width,height):
        self.width = width
        self.height = height

        self.button_singleplay = uix.Button(surface, (self.width//160,300, 150, 60),text = 'SinglePlayer',color= (32,178,170),bottom_rect_color=(255,255,255))
        self.button_setting = uix.Button(surface,(self.width//160,400,200,60),text = 'Settings',color= (32,178,170),bottom_rect_color=(255,255,255))

        self.groupWidget = uix.GroupWidget()
        self.groupWidget.widgets.append(self.button_singleplay)
        self.groupWidget.widgets.append(self.button_setting)
    def create_widgets(self):
        self.groupWidget.create_widget()

    def update(self,events):
        self.groupWidget.update(events)


class SinglePlayerView:
    def __init__(self,surface,width,height):
        self.width = width
        self.height = height

        self.button_rock = uix.Button(surface,(300,600,50,50),'Rock',(180,180,180),(120,120,120))
        self.button_paper = uix.Button(surface,(400,600,50,50),'Paper',(180,180,180),(120,120,120))
        self.button_scissors = uix.Button(surface,(500,600,50,50),'Scissors',(180,180,180),(120,120,120))
        self.button_back = uix.Button(surface,(0,0,70,70),'Back',(220,220,220),(95,95,95))   


        self.groupWidget_single = uix.GroupWidget()
        self.groupWidget_single.widgets.append(self.button_rock)
        self.groupWidget_single.widgets.append(self.button_paper)
        self.groupWidget_single.widgets.append(self.button_scissors)
        self.groupWidget_single.widgets.append(self.button_back)

    def create_widgets(self):   
        self.groupWidget_single.create_widget()
        
    def update(self,events):
        self.groupWidget_single.update(events)

class MultiPlayerView:
    def __init__(self):
        pass

class Settings:
    def __init__(self,width,height):
        pass
    def create_widgets(self):
        pass
    def update(self,events):
        pass
class RockPaperScissor(MenuView):
    def __init__(self):
        self.width = 900
        self.height = 700
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.clock = pygame.time.Clock()

        self.layer = {
            'Main Menu': True,
            'SinglePlay Menu': False,
            'Settings Menu': False,
            'Back': True
        }

        self.count = 0


        # Main widgets which contain all widget on screen but at first it's empty
        # You have to add your own widget after creating it
        # Use this code to add widget: self.groupWidgets.widgets.append(<widget>)
        
        #GroupWidget 
        self.groupWidget_single = uix.GroupWidget()
        # Initialize any view on screen here


        self.menuView = MenuView(self.screen,self.width,self.height)
        self.menuView.button_singleplay.on_press_action = self.single_play   

        self.singlePlayerView = SinglePlayerView(self.screen,self.width,self.height)
        self.singlePlayerView.button_back.on_press_action = self.back

        
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

            
                
            
            if self.layer['SinglePlay Menu']:
                self.singlePlayerView.create_widgets()
                self.singlePlayerView.update(events)
            elif self.layer['Main Menu']:
                self.menuView.create_widgets()
                self.menuView.update(events)
            


            
    

    
            # Update and set FPS
            self.clock.tick(FPS)
            # self.screen.blit(self.layer1,(0,0))

            pygame.display.flip()
            pygame.display.update()
    def single_play(self):
        self.layer['SinglePlay Menu'] =  True
    def back(self):
        self.layer['SinglePlay Menu'] = False
    def multiplayer_play(self):
        pass

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
