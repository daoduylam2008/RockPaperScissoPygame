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


rps_trans = {
    1: "Rock",
    2: "Scissors",
    3: "Paper"
}


def game_play(player, opponent) -> str:
    if player == opponent:
        return "Draw"
    elif (player == "Rock" and opponent == "Scissors") or (player == "Paper" and opponent == "Rock") or (
            player == "Scissors" and opponent == "Paper"):
        return "Win"
    elif (player == "Rock" and opponent == "Paper") or (player == "Paper" and opponent == "Scissors") or (
            player == "Scissors" and opponent == "Rock"):
        return "Lose"
    else:
        raise ValueError("Unrecognized value")


class MenuView:
    def __init__(self, surface):
        self.surface = surface
        self.background = None

        self.inputBox = uix.InputBox(self.surface, (self.surface.get_rect().center[0]-160, self.surface.get_rect().center[1]-150, 100, 60))
        self.button_singleplay = uix.Button(self.surface, (self.surface.get_rect().center[0]-80, self.surface.get_rect().center[1]-50, 150, 60), text='SinglePlayer',
                                            color=(204, 204, 196), bottom_rect_color=(255, 255, 255),
                                            text_color='#FFFF00')
        self.button_setting = uix.Button(self.surface, (self.surface.get_rect().center[0]-80, self.surface.get_rect().center[1]+150, 150, 60), text='Settings',
                                         color=(32, 178, 170), bottom_rect_color=(255, 255, 255))

        self.button_multiplay = uix.Button(self.surface, (self.surface.get_rect().center[0]-80, self.surface.get_rect().center[1]+50, 150, 60), text='MultiPlayer',
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

    def image_background(self):
        img = Image.open('data/background.png')
        img = img.resize((self.surface.get_width(), self.surface.get_height()),
                                        Image.LANCZOS)
        img.save('data/background_1.png', quality=75)
        imageBackground = uix.Image(self.surface, 'data/background.png', (0, 0, 0, 0))

        imageBackground.rect = imageBackground.image.get_rect(center=imageBackground.surface.get_rect().center)
        imageBackground.create()


class SinglePlayerView:
    def __init__(self, surface, on_press_action_list):
        self.surface = surface

        self.on_press_action_list = on_press_action_list

        self.button_rock = uix.Button(self.surface, (300, 600, 90, 50), 'Rock', '#ff6680', bottom_rect_color='#ed7700',
                                      text_color='black', text_size=23)
        self.button_scissors = uix.Button(self.surface, (400, 600, 90, 50), 'Scissors', '#ff6680',
                                          bottom_rect_color='#ed7700', text_color='black', text_size=23)
        self.button_paper = uix.Button(self.surface, (500, 600, 90, 50), 'Paper', '#ff6680', bottom_rect_color='#ed7700',
                                       text_color='black', text_size=23)
        self.button_back = uix.Button(self.surface, (0, 0, 70, 30), 'Back', '#ff6680', bottom_rect_color='#ed7700',
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


class ServerView(uix.Widget):
    def __init__(self, surface):
        rect = (0, 0, surface.get_width(), surface.get_height())
        super().__init__(surface, rect)

        self.view = uix.GroupWidget()

        self.button_rock = uix.Button(self.surface, (300, 600, 90, 50), 'Rock', '#ff6680', bottom_rect_color='#ed7700',
                                      text_color='black', text_size=23)
        self.button_scissors = uix.Button(self.surface, (400, 600, 90, 50), 'Scissors', '#ff6680',
                                          bottom_rect_color='#ed7700', text_color='black', text_size=23)
        self.button_paper = uix.Button(self.surface, (500, 600, 90, 50), 'Paper', '#ff6680',
                                       bottom_rect_color='#ed7700',
                                       text_color='black', text_size=23)
        self.button_back = uix.Button(self.surface, (0, 0, 70, 30), 'Back', '#ff6680', bottom_rect_color='#ed7700',
                                      text_color='black', text_size=20)

        # Action for button
        self.button_rock.on_press_action = self.on_rock_press
        self.button_paper.on_press_action = self.on_paper_press
        self.button_scissors.on_press_action = self.on_scissors_press
        self.button_back.on_press_action = self.on_back_press

        self.view.widgets.append(self.button_rock)
        self.view.widgets.append(self.button_back)
        self.view.widgets.append(self.button_paper)
        self.view.widgets.append(self.button_scissors)

    def on_rock_press(self): pass

    def on_scissors_press(self): pass

    def on_paper_press(self): pass

    def on_back_press(self): pass


class ClientView(uix.Widget):
    def __init__(self, surface):
        rect = (0, 0, surface.get_width(), surface.get_height())
        super().__init__(surface, rect)

        self.view = uix.GroupWidget()

        self.button_rock = uix.Button(self.surface, (300, 600, 90, 50), 'Rock', '#ff6680', bottom_rect_color='#ed7700',
                                      text_color='black', text_size=23)
        self.button_scissors = uix.Button(self.surface, (400, 600, 90, 50), 'Scissors', '#ff6680',
                                          bottom_rect_color='#ed7700', text_color='black', text_size=23)
        self.button_paper = uix.Button(self.surface, (500, 600, 90, 50), 'Paper', '#ff6680',
                                       bottom_rect_color='#ed7700',
                                       text_color='black', text_size=23)
        self.button_back = uix.Button(self.surface, (0, 0, 70, 30), 'Back', '#ff6680', bottom_rect_color='#ed7700',
                                      text_color='black', text_size=20)

        # Action for button
        self.button_rock.on_press_action = self.on_rock_press
        self.button_paper.on_press_action = self.on_paper_press
        self.button_scissors.on_press_action = self.on_scissors_press
        self.button_back.on_press_action = self.on_back_press

        self.view.widgets.append(self.button_rock)
        self.view.widgets.append(self.button_back)
        self.view.widgets.append(self.button_paper)
        self.view.widgets.append(self.button_scissors)

    def on_rock_press(self): pass

    def on_scissors_press(self): pass

    def on_paper_press(self): pass

    def on_back_press(self): pass


class SelectClientServerView(uix.Widget):
    def __init__(self, surface):
        rect = (0, 0, surface.get_width(), surface.get_height())
        super().__init__(surface, rect)

        self.view = uix.GroupWidget()

        # Layer for view
        self.layer = {
            "selection": True,
            "server": False,
            "client": False
        }

        # Create the button for view
        self.roomInputBox = uix.InputBox(self.surface, (self.surface.get_rect().center[0]-150, self.surface.get_rect().center[1]-150, 100, 60))
        self.joinRoomButton = uix.Button(self.surface, (self.surface.get_rect().center[0]-80, self.surface.get_rect().center[1]-50, 160, 60), text='Join Room',
                                            color=(204, 204, 196), bottom_rect_color=(255, 255, 255),
                                            text_color='#FFFF00')
        self.joinRoomButton.on_press_action = self.joinRoom

        self.createRoomButton = uix.Button(self.surface, (self.surface.get_rect().center[0]-80, self.surface.get_rect().center[1]+50, 160, 60), text='Create Room',
                                         color=(32, 178, 170), bottom_rect_color=(255, 255, 255))
        self.createRoomButton.on_press_action = self.createRoomButton

        self.view.widgets = [
            self.roomInputBox,
            self.joinRoomButton,
            uix.Separator(self.surface, (self.surface.get_rect().center[0]-80, self.surface.get_rect().center[1]+25, 150, 2), (0, 0, 0)),
            self.createRoomButton
        ]

    def update(self, events):
        self.view.update(events)

    def create(self):
        self.view.create_widget()

    def joinRoom(self):
        self.layer['selection'] = False
        self.layer['server'] = False
        self.layer['client'] = True

    def createRoom(self):
        self.layer['selection'] = False
        self.layer['server'] = True
        self.layer['client'] = False


class MultiPlayerView(uix.Widget):
    def __init__(self, surface):
        rect = (0, 0, surface.get_width(), surface.get_height())
        super().__init__(surface, rect)

        self.view = uix.GroupWidget()

        self.selectionView = SelectClientServerView(surface)

        self.view.widgets = [
            self.selectionView
        ]

    def create(self):
        self.view.create_widget()

    def update(self, events):
        self.view.update(events)


class Settings:
    def __init__(self, width, height):
        pass

    def create_widgets(self):
        pass

    def update(self, events):
        pass


def close():
    pygame.quit()
    sys.exit()


class RockPaperScissor:
    def __init__(self):
        self.imageBot_choice = None
        self.width = 900
        self.height = 700
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.clock = pygame.time.Clock()

        self.view = {
            'Menu View': True,
            'SinglePlay View': False,
            'MultiPlay View'
            'Settings View': False,
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
        # Menu View initialization
        self.menuView = MenuView(self.screen)
        self.menuView.button_singleplay.on_press_action = self.single_play
        # Single View initialization
        self.singlePlayerView = SinglePlayerView(self.screen,
                                                 [self.rock, self.paper, self.scissors, self.back])
        # Multiplayer View initialization
        self.multiPlayerView = MultiPlayerView(self.screen)

        ###################
        # WARN: This code has to be inside the single view instead of this class

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
        ###################

    def run(self):
        while True:
            # Fill the screen with BLACK instead of an empty screen
            self.menuView.image_background()

            # Event
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    close()

            if self.view['SinglePlay View']:
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
            elif self.view['Menu View']:
                self.menuView.create_widgets()
                self.menuView.update(events)
            elif self.view["MultiPlay View"]:
                self.multiPlayerView.create()
                self.multiPlayerView.update(events)

            # Update and set FPS
            self.clock.tick(FPS)

            pygame.display.flip()
            pygame.display.update()

    ################
    # This code is for single view, so it has to be initialized in singe view instead of this class
    def single_play(self):
        self.view['SinglePlay View'] = True
        self.view['Menu View'] = False
        self.view["MultiPlay View"] = False
        self.view["Setting View"] = False

    #######
    # Warning: This code should not be here
    def back(self):
        self.view['SinglePlay View'] = False
        self.view['Menu View'] = True
        self.view["MultiPlay View"] = False
        self.view["Setting View"] = False
    #########

    def multi_play(self):
        self.view['SinglePlay View'] = False
        self.view['Menu View'] = False
        self.view["MultiPlay View"] = True
        self.view["Setting View"] = False

    def setting(self):
        self.view['SinglePlay View'] = False
        self.view['Menu View'] = False
        self.view["MultiPlay View"] = False
        self.view["Setting View"] = True

    def rock(self):
        self.who_win,self.imageBot_choice,self.playerChoice=self.which_button_rpg_clicked('Rock')

    def paper(self):
        self.who_win,self.imageBot_choice,self.playerChoice=self.which_button_rpg_clicked('Paper')

    def scissors(self):
        self.who_win,self.imageBot_choice,self.playerChoice=self.which_button_rpg_clicked('Scissors')

    def which_button_rpg_clicked(self, playerChoice):
        self.clicked = True

        self.imageBot.returnIndex()
        self.imagePlayer.returnIndex()

        # This code has not been done yet, after update the machine learning and difficulty it will change
        imageBot_choice = random.randint(1, 3)
        self.imageBot_choice_list.append(imageBot_choice)
        self.imageBot_choice_list = self.imageBot_choice_list[-1:]

        match self.imageBot_choice_list[-1]:
            case 1:
                self.imageBot.imageFolder = 'data/rock_animation/'
            case 2:
                self.imageBot.imageFolder = 'data/scissors_animation/'
            case 3:
                self.imageBot.imageFolder = 'data/paper_animation/'

        match playerChoice:
            case 'Paper':
                self.imagePlayer.imageFolder = 'data/paper_animation/'
            case 'Rock':
                self.imagePlayer.imageFolder = 'data/rock_animation/'
            case 'Scissors':
                self.imagePlayer.imageFolder = 'data/scissors_animation/'
        who_win = game_play(playerChoice, self.imageBot_choice_list[-1])

        return who_win, imageBot_choice,self.playerChoice
    #################


if __name__ == "__main__":
    game = RockPaperScissor()
    game.run()
