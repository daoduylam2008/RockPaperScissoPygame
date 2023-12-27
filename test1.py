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
import random
from PIL import Image

# Color


# Authorize information, gmail
__author1__ = "daoduylam2020@gmail.com"  # DAO DUY LAM
__author2__ = ""  # PHAM MINH KHOI
__author3__ = ""  # LE CONG TIEN

# ___ MAIN ___
FPS = 60


class MenuView:
    def __init__(self, surface, width, height):
        self.background = None
        self.width = width
        self.height = height

        self.inputBox = uix.InputBox(surface,
                                     (surface.get_rect().center[0] - 160, surface.get_rect().center[1] - 150, 100, 60))
        self.button_singleplay = uix.Button(surface, (
            surface.get_rect().center[0] - 80, surface.get_rect().center[1] - 50, 150, 60), text='SinglePlayer',
                                            color=(204, 204, 196), bottom_rect_color=(255, 255, 255),
                                            text_color='#FFFF00')
        self.button_setting = uix.Button(surface, (
            surface.get_rect().center[0] - 80, surface.get_rect().center[1] + 150, 150, 60), text='Settings',
                                         color=(32, 178, 170), bottom_rect_color=(255, 255, 255))

        self.button_multiplay = uix.Button(surface, (
            surface.get_rect().center[0] - 80, surface.get_rect().center[1] + 50, 150, 60), text='MultiPlayer',
                                           color=(204, 204, 196), bottom_rect_color=(255, 255, 255),
                                           text_color='#FFFF00')

        self.groupWidget = uix.GroupWidget()
        self.groupWidget.widgets.append(self.button_singleplay)
        self.groupWidget.widgets.append(self.button_multiplay)
        self.groupWidget.widgets.append(self.button_setting)
        self.groupWidget.widgets.append(self.inputBox)

    def create_widgets(self):
        self.groupWidget.create_widget()

    def update(self, events):
        self.groupWidget.update(events)

    def image_background(self, surface):
        #img = Image.open('data/background.png')
        #img = img.resize((surface.get_width(),surface.get_height()),
                         #Image.LANCZOS)
        #img.save('data/background.png', quality=95)
        imageBackground = uix.Image(surface, 'data/paper_animation/paper_animation1.png', (0, 0, 0, 0))
        imageBackground.rect = imageBackground.image.get_rect(
            center=imageBackground.surface.get_rect().center)
        imageBackground.create()


class SinglePlayerView:
    def __init__(self, surface, width, height, on_press_action_list):
        self.width = width
        self.height = height

        self.on_press_action_list = on_press_action_list

        self.button_rock = uix.Button(surface, (surface.get_rect().bottomright[0]-300, surface.get_rect().bottomright[1]-80, 90, 50), 'Rock', '#ff6680', bottom_rect_color='#ed7700',
                                      text_color='black', text_size=23)
        self.button_scissors = uix.Button(surface, (surface.get_rect().bottomright[0]-200, surface.get_rect().bottomright[1]-80, 90, 50), 'Scissors', '#ff6680',
                                          bottom_rect_color='#ed7700', text_color='black', text_size=23)
        self.button_paper = uix.Button(surface, (surface.get_rect().bottomright[0]-100, surface.get_rect().bottomright[1]-80, 90, 50), 'Paper', '#ff6680', bottom_rect_color='#ed7700',
                                       text_color='black', text_size=23)
        self.button_back = uix.Button(surface, (0, 0, 70, 30), 'Back', '#ff6680', bottom_rect_color='#ed7700',
                                      text_color='black', text_size=20)

        self.list_button_singlePlayer = [
            self.button_rock,
            self.button_paper,
            self.button_scissors,
            self.button_back
        ]

        self.groupWidget_single = uix.GroupWidget()
        for i in self.list_button_singlePlayer:
            self.groupWidget_single.widgets.append(i)

        self.on_press_action()

    def on_press_action(self):
        for i in self.list_button_singlePlayer:
            match i:
                case self.button_rock:
                    self.button_rock.on_press_action = self.on_press_action_list[0]
                case self.button_paper:
                    self.button_paper.on_press_action = self.on_press_action_list[1]
                case self.button_scissors:
                    self.button_scissors.on_press_action = self.on_press_action_list[2]
                case self.button_back:
                    self.button_back.on_press_action = self.on_press_action_list[3]

    def create_widgets(self):
        self.groupWidget_single.create_widget()

    def update(self, events):
        self.groupWidget_single.update(events)


class MultiPlayerView:
    def __init__(self):
        pass


class Settings:
    def __init__(self, surface,width, height,func_back,func_resizeWindow):
        self.width = width
        self.height = height
        self.back = func_back
        self.resize = func_resizeWindow

        self.resizeWindow = uix.Button(surface, (
            surface.get_rect().center[0] - 80, surface.get_rect().center[1] - 50, 150, 60), text='Resize Window',
                                            color=(204, 204, 196), bottom_rect_color=(255, 255, 255),
                                            text_color='#FFFF00')
        self.resizeWindow.on_press_action = self.resize

        self.button_back = uix.Button(surface, (0, 0, 70, 30), 'Back', '#ff6680', bottom_rect_color='#ed7700',
                                text_color='black', text_size=20)
        self.button_back.on_press_action = self.back

        self.groupWidget_settings = uix.GroupWidget()
        self.groupWidget_settings.widgets.append(self.resizeWindow)
        self.groupWidget_settings.widgets.append(self.button_back)

    def create_widgets(self):
        self.groupWidget_settings.create_widget()

    def update(self, events):
        self.groupWidget_settings.update(events)

    def buttonResizeWindow(self,surface,checkCreate_Update,events,func):
        back_settings  = func[0]
        resizeFullScreen  = func[1]
        resizeSmall  = func[2]
        resizeMedium  = func[3]
        resizeLarge  = func[4]
        #Button Back
        self.button_backSettings = uix.Button(surface, (0, 0, 70, 30), 'Back', '#ff6680', bottom_rect_color='#ed7700',
                                text_color='black', text_size=20)
        self.button_backSettings.on_press_action = back_settings

        #Button FullScreen
        self.fullScreen = uix.Button(surface, (
            surface.get_rect().center[0] - 80, surface.get_rect().center[1] - 150, 150, 60), text='Full Screen',
                                            color=(204, 204, 196), bottom_rect_color=(255, 255, 255),
                                            text_color='#FFFF00')
        self.fullScreen.on_press_action = resizeFullScreen

        #Button Small
        self.small = uix.Button(surface, (
            surface.get_rect().center[0] - 80, surface.get_rect().center[1] - 50, 150, 60), text='Small',
                                            color=(204, 204, 196), bottom_rect_color=(255, 255, 255),
                                            text_color='#FFFF00')
        self.small.on_press_action = resizeSmall

        self.medium = uix.Button(surface, (
            surface.get_rect().center[0] - 80, surface.get_rect().center[1] + 50, 150, 60), text='Medium',
                                            color=(204, 204, 196), bottom_rect_color=(255, 255, 255),
                                            text_color='#FFFF00')
        # self.medium.on_press_action = resizeMedium

        self.large = uix.Button(surface, (
            surface.get_rect().center[0] - 80, surface.get_rect().center[1] + 150, 150, 60), text='Large',
                                            color=(204, 204, 196), bottom_rect_color=(255, 255, 255),
                                            text_color='#FFFF00')
        # self.large.on_press_action = resizeLarge
        
        self.groupWidget_resizeWindow = uix.GroupWidget()
        self.groupWidget_resizeWindow.widgets.append(self.fullScreen)        
        self.groupWidget_resizeWindow.widgets.append(self.small)        
        self.groupWidget_resizeWindow.widgets.append(self.medium)        
        self.groupWidget_resizeWindow.widgets.append(self.large)        
        self.groupWidget_resizeWindow.widgets.append(self.button_backSettings)

        if checkCreate_Update:
            self.groupWidget_resizeWindow.create_widget()
        if checkCreate_Update:
            self.groupWidget_resizeWindow.update(events)        


class RockPaperScissor:
    def __init__(self):
        self.imageBot_choice = None
        self.width = 900
        self.height = 700
        self.screen = pygame.display.set_mode((self.width,self.height))

        self.clock = pygame.time.Clock()

        self.view = {
            'Main Menu': True,
            'SinglePlay Menu': False,
            'Settings Menu': False,
            'Back': True
        }
        self.SetingsView = {
            'Resize Window': False
        }


        self.playerChoice = ''
        self.numberPlayerChoice = 0
        self.imageBot_choice_list = []
        self.who_win = 'Fight'
        self.clicked = False

        # Main widgets which contain all widget on screen but at first it's empty
        # You have to add your own widget after creating it
        # Use this code to add widget: self.groupWidgets.widgets.append(<widget>)

        
        #The Menu Screen
        self.menuView = MenuView(self.screen, self.width, self.height) #Create the menu
        self.menuView.button_singleplay.on_press_action = self.single_play 
        self.menuView.button_setting.on_press_action = self.setting

        #The Single Player View
        self.singlePlayerView = SinglePlayerView(self.screen, self.width, self.height,
                                                 [self.rock, self.paper, self.scissors, self.back])

        #The Settings View
        self.settingsView = Settings(self.screen,self.width,self.height,self.back,self.resize)

        
        #The Image Rock Paper Scissors in Single Player View for player
        self.imagePlayer = uix.ImageAnimation(self.screen, rect=(20, self.screen.get_rect().bottomright[1]-235, 100, 100),
                                              imageFolder='data/scissors_animation/', scale=(230, 230), flip=False,
                                              fps=30,angle=0)

        #The Image Rock Paper Scissors in Single Player View for bot
        self.imageBot = uix.ImageAnimation(self.screen, rect=(self.screen.get_rect().topright[0]-260,10, 100, 100),
                                           imageFolder='data/scissors_animation/', scale=(230, 230),
                                           flip=True, fps=60,angle=90)

        #Blit the text win or lose or draw
        self.who_will_win = uix.Text(self.screen, (
            self.screen.get_rect().center[0] - 53, self.screen.get_rect().center[1] - 20, 50, 50),
                                     size=64,
                                     color='black', text=self.who_win)
        #The Player Name
        self.playerName = uix.Text(self.screen, (50, self.screen.get_rect().bottomright[1]-100, 50, 50), size=32, color='black',
                                   text=self.menuView.inputBox.text)
        #The Bot nAME
        self.bot = uix.Text(self.screen, (self.screen.get_rect().topright[0]-130, 80, 50, 50), size=32, color='black', text='Bot')

    def run(self):

        while True:
            # Fill the screen with BLACK instead of an empty screen
            # self.menuView.image_background(self.screen)
            self.screen.fill('Black')

            # Event
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.close()

            if self.view['SinglePlay Menu']:
                self.singlePlayerView.create_widgets()
                self.singlePlayerView.update(events)

                self.imagePlayer.create()
                self.imageBot.create()


                if self.clicked:
                    self.imagePlayer.update(events)
                    self.imageBot.update(events)

                self.who_will_win.create(self.who_win)
                self.playerName.create(self.menuView.inputBox.text)
                self.bot.create('Bot')
            elif self.view['Settings Menu']:
                

                if self.SetingsView['Resize Window']:
                    self.settingsView.buttonResizeWindow(self.screen,True,events,[self.backSettings,self.resizeFullScreen,self.resizeSmall,self.resizeMedium,self.resizeLarge])
                else:
                    self.settingsView.create_widgets()
                    self.settingsView.update(events)   

            elif self.view['Main Menu']:
                self.menuView.create_widgets()
                self.menuView.update(events)
            

            # Update and set FPS
            self.clock.tick(FPS)
            # self.screen.blit(self.view1,(0,0))

            pygame.display.flip()
            pygame.display.update()

    def single_play(self):
        self.view['SinglePlay Menu'] = True

    def back(self):
        self.view['SinglePlay Menu'] = False
        self.view['Settings Menu'] = False
        self.view['Main Menu'] = True
    def setting(self):
        self.view['Settings Menu'] = True
        self.view['Main Menu'] = False
    def resize(self):
        self.SetingsView['Resize Window'] = True
    def resizeFullScreen(self):
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.resizeWindow()

    def resizeSmall(self):
        self.screen = pygame.display.set_mode((640,520))
        self.resizeWindow()
    def resizeMedium(self):
        self.screen = pygame.display.set_mode((self.width,self.height))
    def resizeLarge(self):
        self.screen = pygame.display.set_mode((1008,888))

    def resizeWindow(self):
        self.settingsView.resizeWindow.rect[0] = self.screen.get_rect().center[0] - 80
        self.settingsView.resizeWindow.rect[1] = self.screen.get_rect().center[1] - 50

        self.playerName.rect[0],self.playerName.rect[1] = 50, self.screen.get_rect().bottomright[1]-100
        
        self.bot.rect[0],self.bot.rect[1] = self.screen.get_rect().topright[0]-130, 80

        self.who_will_win.rect[0],self.who_will_win.rect[1] = self.screen.get_rect().center[0] - 53, self.screen.get_rect().center[1] - 20

        self.imagePlayer.rect[0],self.imagePlayer.rect[1] = 20, self.screen.get_rect().bottomright[1]-235
        self.imageBot.rect[0],self.imageBot.rect[1] = self.screen.get_rect().topright[0]-260,10


        self.singlePlayerView.button_rock.rect[0],self.singlePlayerView.button_rock.rect[1] = self.screen.get_rect().bottomright[0]-300, self.screen.get_rect().bottomright[1]-80
        self.singlePlayerView.button_paper.rect[0],self.singlePlayerView.button_paper.rect[1] = self.screen.get_rect().bottomright[0]-100, self.screen.get_rect().bottomright[1]-80
        self.singlePlayerView.button_scissors.rect[0],self.singlePlayerView.button_scissors.rect[1] = self.screen.get_rect().bottomright[0]-200, self.screen.get_rect().bottomright[1]-80

        self.menuView.button_singleplay.rect[0],self.menuView.button_singleplay.rect[1] =   self.screen.get_rect().center[0] - 80, self.screen.get_rect().center[1] - 50
        self.menuView.button_multiplay.rect[0],self.menuView.button_multiplay.rect[1] =   self.screen.get_rect().center[0] - 80, self.screen.get_rect().center[1] + 50
        self.menuView.button_setting.rect[0],self.menuView.button_setting.rect[1] =   self.screen.get_rect().center[0] - 80, self.screen.get_rect().center[1] + 150
        self.menuView.inputBox.rect[0],self.menuView.inputBox.rect[1] = self.screen.get_rect().center[0] - 160, self.screen.get_rect().center[1] - 150
    def backSettings(self):
        self.SetingsView['Resize Window'] = False
        self.view['Settings Menu'] = True


    def multiplayer_play(self):
        pass

    def rock(self):
        self.who_win, self.numberPlayerChoice = self.which_button_rpg_clicked('Rock')

    def paper(self):
        self.who_win, self.numberPlayerChoice = self.which_button_rpg_clicked('Paper')

    def scissors(self):
        self.who_win, self.numberPlayerChoice = self.which_button_rpg_clicked('Scissors')

    def which_button_rpg_clicked(self, playerChoice):
        self.clicked = True
        self.playerChoice = playerChoice

        self.imageBot.returnIndex()
        self.imagePlayer.returnIndex()

        self.imageBot_choice = random.randint(1, 3)
        self.imageBot_choice_list.append(self.imageBot_choice)
        self.imageBot_choice_list = self.imageBot_choice_list[-1:]

        match self.imageBot_choice_list[-1]:
            case 1:
                self.imageBot.imageFolder = 'data/rock_animation/'

            case 2:
                self.imageBot.imageFolder = 'data/scissors_animation/'

            case 3:
                self.imageBot.imageFolder = 'data/paper_animation/'
        match self.playerChoice:
            case 'Paper':
                self.numberPlayerChoice = 2
                self.imagePlayer.imageFolder = 'data/paper_animation/'
                if self.imageBot_choice_list[-1] == 1:
                    self.who_win = 'Win'
                if self.imageBot_choice_list[-1] == 2:
                    self.who_win = 'Lose'
                if self.imageBot_choice_list[-1] == 3:
                    self.who_win = 'Draw'
            case 'Rock':
                self.numberPlayerChoice = 1
                self.imagePlayer.imageFolder = 'data/rock_animation/'
                if self.imageBot_choice_list[-1] == 1:
                    self.who_win = 'Draw'
                if self.imageBot_choice_list[-1] == 2:
                    self.who_win = 'Win'
                if self.imageBot_choice_list[-1] == 3:
                    self.who_win = 'Lose'
            case 'Scissors':
                self.numberPlayerChoice = 3
                self.imagePlayer.imageFolder = 'data/scissors_animation/'
                if self.imageBot_choice_list[-1] == 1:
                    self.who_win = 'Lose'
                if self.imageBot_choice_list[-1] == 2:
                    self.who_win = 'Draw'
                if self.imageBot_choice_list[-1] == 3:
                    self.who_win = 'Win'
        return self.who_win, self.numberPlayerChoice

    def close(self):
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = RockPaperScissor()
    game.run()
    # except Exception as bug:
    #     print(bug)
    #     game.close()
