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
FPS = 80


class MenuView:
    def __init__(self, surface, width, height):
        self.background = None
        self.width = width
        self.height = height

        self.inputBox = uix.InputBox(surface,(surface.get_rect().center[0]-160, surface.get_rect().center[1]-150, 100, 60))
        self.button_singleplay = uix.Button(surface, (surface.get_rect().center[0]-80, surface.get_rect().center[1]-50, 150, 60), text='SinglePlayer',
                                            color=(204, 204, 196), bottom_rect_color=(255, 255, 255),
                                            text_color='#FFFF00')
        self.button_setting = uix.Button(surface, (surface.get_rect().center[0]-80, surface.get_rect().center[1]+150, 150, 60), text='Settings',
                                         color=(32, 178, 170), bottom_rect_color=(255, 255, 255))

        self.button_multiplay = uix.Button(surface, (surface.get_rect().center[0]-80, surface.get_rect().center[1]+50, 150, 60), text='MultiPlayer',
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

        self.img = Image.open('data/background.png')
        self.img = self.img.resize((surface.get_width(), surface.get_height()),
                                        Image.LANCZOS)
        self.img.save('data/background_1.png', quality=75)
        self.imageBackground = uix.Image(surface, 'data/background.png', (0, 0, 0, 0))

        self.imageBackground.rect = self.imageBackground.image.get_rect(center=self.imageBackground.surface.get_rect().center)
        self.imageBackground.create()


class SinglePlayerView:

    def __init__(self, surface, width, height, on_press_action_list):
        self.width = width
        self.height = height

        self.on_press_action_list = on_press_action_list

        self.button_rock = uix.Button(surface, (300, 600, 90, 50), 'Rock', '#ff6680', bottom_rect_color='#ed7700',
                                      text_color='black', text_size=23)
        self.button_scissors = uix.Button(surface, (400, 600, 90, 50), 'Scissors', '#ff6680',
                                          bottom_rect_color='#ed7700', text_color='black', text_size=23)
        self.button_paper = uix.Button(surface, (500, 600, 90, 50), 'Paper', '#ff6680', bottom_rect_color='#ed7700',
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
    def __init__(self, width, height):
        pass

    def create_widgets(self):
        pass

    def update(self, events):
        pass


class RockPaperScissor:
    def __init__(self):
        self.imageBot_choice = None
        self.width = 900
        self.height = 700
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.clock = pygame.time.Clock()

        self.view = {
            'Main Menu': True,
            'SinglePlay Menu': False,
            'Settings Menu': False,
            'Back': True
        }
        self.playerChoice = ''

        self.imageBot_choice_list = []
        self.who_win = 'Fight'
        self.clicked = False

        # Main widgets which contain all widget on screen but at first it's empty
        # You have to add your own widget after creating it
        # Use this code to add widget: self.groupWidgets.widgets.append(<widget>)

        # GroupWidget
        self.groupWidget_single = uix.GroupWidget()
        # Initialize any view on screen here

        self.menuView = MenuView(self.screen, self.width, self.height)
        self.menuView.button_singleplay.on_press_action = self.single_play

        self.singlePlayerView = SinglePlayerView(self.screen, self.width, self.height,
                                                 [self.rock, self.paper, self.scissors, self.back])

        self.imagePlayer = uix.ImageAnimation(self.screen, rect=(50, 300, 100, 100),
                                              imageFolder='data/scissors_animation/', scale=(230, 230), flip=False,
                                              fps=30)
        self.imageBot = uix.ImageAnimation(self.screen, rect=(650, 300, 100, 100),
                                           imageFolder='data/scissors_animation/', scale=(230, 230), flip=True, fps=60)

        self.who_will_win = uix.Text(self.screen, (
            self.screen.get_rect().center[0] - 53, self.screen.get_rect().center[1] - 20, 50, 50),
                                    size=64,
                                     color='black',text= self.who_win)
        self.playerName = uix.Text(self.screen,(70,280,50,50),size = 32,color = 'black',text =self.menuView.inputBox.text)
        self.bot = uix.Text(self.screen,(770,280,50,50),size = 32,color = 'black',text ='Bot')

    def run(self):

        while True:
            # Fill the screen with BLACK instead of an empty screen
            self.menuView.image_background(self.screen)

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

    def multiplayer_play(self):
        pass

    def rock(self):
        self.who_win,self.imageBot_choice,self.playerChoice=self.which_button_rpg_clicked('Rock')

    def paper(self):
        self.who_win,self.imageBot_choice,self.playerChoice=self.which_button_rpg_clicked('Paper')

    def scissors(self):
        self.who_win,self.imageBot_choice,self.playerChoice=self.which_button_rpg_clicked('Scissors')

    def which_button_rpg_clicked(self,playerChoice):
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
                self.imagePlayer.imageFolder = 'data/paper_animation/'
                if self.imageBot_choice_list[-1] == 1:
                    self.who_win = 'Win'
                if self.imageBot_choice_list[-1] == 2:
                    self.who_win = 'Lose'
                if self.imageBot_choice_list[-1] == 3:
                    self.who_win = 'Draw'
            case 'Rock':
                self.imagePlayer.imageFolder = 'data/rock_animation/'
                if self.imageBot_choice_list[-1] == 1:
                    self.who_win = 'Draw'
                if self.imageBot_choice_list[-1] == 2:
                    self.who_win = 'Win'
                if self.imageBot_choice_list[-1] == 3:
                    self.who_win = 'Lose'
            case 'Scissors':
                self.imagePlayer.imageFolder = 'data/scissors_animation/'
                if self.imageBot_choice_list[-1] == 1:
                    self.who_win = 'Lose'
                if self.imageBot_choice_list[-1] == 2:
                    self.who_win = 'Draw'
                if self.imageBot_choice_list[-1] == 3:
                    self.who_win = 'Win'
        return self.who_win,self.imageBot_choice,self.playerChoice


    def close(self):
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = RockPaperScissor()
    game.run()
    # except Exception as bug:
    #     print(bug)
    #     game.close()
