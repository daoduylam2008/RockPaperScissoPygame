"""
Rock Paper Scissor Game GUI Application

The program is used some of the libraries which are installed from PyPI (Python Package Index)

Developed by DAO DUY LAM, PHAM MINH KHOI, LE CONG TIEN
"""
# Python Package Index
import pygame
import pygame as _pygame
from pygame.sprite import Sprite as _Sprite
pygame.init()

# System Module and Libraries
import sys
import os

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import random
import csv

import firebase_admin
from firebase_admin import credentials, db

# Authorize information, gmail
__author1__ = "daoduylam2020@gmail.com"  # DAO DUY LAM
__author2__ = "phamminhkhoi10122008@gmail.com"  # PHAM MINH KHOI
__author3__ = "ltien9505@gmail.com"  # LE CONG TIEN


# ___ MAIN ___
# Graphic User Interface
class Widget:
	def __init__(self, surface, rect):
		self.surface = surface
		self.rect = _pygame.Rect(rect)

	def update(self, events):
		pass

	def create(self):
		pass


class GroupWidget:
	def __init__(self,
				 widgets=None):
		if widgets is None:
			widgets = []
		self.widgets = widgets

	def update(self, events):
		for widget in self.widgets:
			widget.update(events)

	def create_widget(self):
		for widget in self.widgets:
			widget.create()


class Text(Widget):
	def __init__(self,
				 surface,
				 rect,
				 text="text",
				 size=32,
				 color=(0, 0, 0)
				 ):
		super().__init__(surface, rect)
		self._font = None
		self._txt = None
		self.text = text
		self.color = color
		self.size = size

	def create(self, text):
		self.text = text
		self._txt = self.render_text()
		self.surface.blit(self._txt, self.rect)

	def update(self, events):
		pass

	def render_text(self):
		self._font = _pygame.font.Font(None, self.size)
		_txt = self._font.render(self.text, True, self.color)
		return _txt


class Button(Widget):
	def __init__(self,
				 surface,
				 rect: tuple,
				 text="Button",
				 color=(180, 180, 180),
				 on_touch_color=(150, 150, 150),
				 bottom_rect_color=(0, 0, 0),
				 text_color=(255, 255, 255),
				 on_press_action=...,
				 on_touch_action=...,
				 button=1,
				 alignment="center",
				 text_size=30,
				 elevation=6,
				 border_radius=10
				 ):
		super().__init__(surface, rect)

		self.original_color = color
		self.color = color
		self.on_touch_color = on_touch_color
		self.text_color = text_color

		self.text_size = text_size

		self.text = self.textForButton(text)

		self.on_press_action = on_press_action
		self.on_touch_action = on_touch_action

		self.button = button

		self.alignment = alignment

		# Make the elevation for button
		self.elevation = elevation
		self.border_radius = border_radius

		# The bottom rectangle under the top rectangle
		self.bottom_rect = pygame.Rect(rect)
		self.bottom_rect_color = bottom_rect_color

		self.access = False

	def create(self):
		mouse_pos = _pygame.mouse.get_pos()
		start_time, time = 110, 0
		timing = pygame.time.get_ticks()

		x, y = self._alignment(self.alignment)

		self.bottom_rect.center = self.rect.center
		self.bottom_rect.y = self.rect.y + self.elevation + 2

		if self.rect.collidepoint(mouse_pos):
			if _pygame.mouse.get_pressed()[0]:
				#
				self.rect.y += self.elevation

				y += 3
				_pygame.draw.rect(self.surface, self.bottom_rect_color, self.bottom_rect,
								  border_radius=self.border_radius)
				_pygame.draw.rect(self.surface, self.color, self.rect, border_radius=self.border_radius)

				if timing - time > start_time:
					time = timing
					self.rect.y -= self.elevation


			else:
				_pygame.draw.rect(self.surface, self.bottom_rect_color, self.bottom_rect,
								  border_radius=self.border_radius)
				_pygame.draw.rect(self.surface, self.color, self.rect, border_radius=self.border_radius)

		else:
			_pygame.draw.rect(self.surface, self.bottom_rect_color, self.bottom_rect, border_radius=self.border_radius)
			_pygame.draw.rect(self.surface, self.color, self.rect, border_radius=self.border_radius)

			try:
				self.on_touch_action()
			except:
				pass

		self.surface.blit(self.text, (x, y))

	def update(self, events):
		mouse_pos = _pygame.mouse.get_pos()

		for event in events:
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == self.button:
					if self.rect.collidepoint(mouse_pos):
						if pygame.mouse.get_pressed()[0]:
							self.on_press_action()

	def _alignment(self, alignment):
		if alignment == "center":
			x = self.rect.x + (self.rect.width - self.text.get_width()) / 2
			y = self.rect.y + (self.rect.height - self.text.get_height()) / 2
		elif alignment == "left":
			x = self.rect.x
			y = self.rect.y + (self.rect.height - self.text.get_height()) / 2
		elif alignment == "right":
			x = self.rect.x + self.rect.width - self.text.get_width()
			y = self.rect.y + (self.rect.height - self.text.get_height()) / 2
		elif alignment == "top":
			x = self.rect.x + (self.rect.width - self.text.get_width()) / 2
			y = self.rect.y
		elif alignment == "bottom":
			x = self.rect.x + (self.rect.width - self.text.get_width()) / 2
			y = self.rect.y + self.rect.height - self.text.get_height()
		elif alignment == "top-left":
			x = self.rect.x
			y = self.rect.y
		elif alignment == "top-right":
			x = self.rect.x + self.rect.width - self.text.get_width()
			y = self.rect.y
		elif alignment == "bottom-left":
			x = self.rect.x
			y = self.rect.y + self.rect.height - self.text.get_height()
		elif alignment == "bottom-right":
			x = self.rect.x + self.rect.width - self.text.get_width()
			y = self.rect.y + self.rect.height - self.text.get_height()
		else:
			x = 0
			y = 0
		return x, y

	def textForButton(self, text):
		font = _pygame.font.SysFont('timesnewroman', self.text_size)
		txt = font.render(text, True, self.text_color)

		return txt


class InputBox(Widget):

	def __init__(self,
				 surface,
				 rect,
				 text='',
				 action=None
				 ):
		super().__init__(surface, rect)

		self._COLOR_INACTIVE = _pygame.Color('lightskyblue3')
		self._COLOR_ACTIVE = _pygame.Color('dodgerblue2')
		self._FONT = _pygame.font.Font(None, self.rect.height - 20)

		self.color = self._COLOR_INACTIVE

		self.text = text
		self.txt_surface = self._FONT.render(text, True, self.color)

		self.active = False

		self.action = action

	def _update(self):
		# Resize the box if the text is too long.
		width = max(300, self.txt_surface.get_width() + 10)
		self.rect.w = width

	def update(self, events):
		for event in events:
			if event.type == _pygame.MOUSEBUTTONDOWN:
				# If the user clicked on the input_box rect.
				if self.rect.collidepoint(event.pos):
					# Toggle the active variable.
					self.active = not self.active
				else:
					self.active = False

				# Change the current color of the input box.
				self.color = self._COLOR_ACTIVE if self.active else self._COLOR_INACTIVE
			if event.type == _pygame.KEYDOWN:
				if self.active:
					if event.key == _pygame.K_RETURN:
						self.text = ''
						try:
							self.action()
						except:
							pass
					elif event.key == _pygame.K_BACKSPACE:
						self.text = self.text[:-1]
					else:
						if len(self.text) <= 6:
							self.text += event.unicode
					# Re-render the text.
					self.txt_surface = self._FONT.render(self.text, True, self.color)

	def create(self):
		# Update input box's width
		self._update()

		# Blit the text.
		self.surface.blit(self.txt_surface, (self.rect.x + 90, self.rect.y + 5))

		# Blit the rect.
		_pygame.draw.rect(self.surface, self.color, self.rect, 2)

	def reset_text(self):
		self.text = self.text[:-1]


class Image(Widget):
	def __init__(self,
				 surface,
				 path,
				 pos: tuple,
				 view=None,
				 animation=None
				 ):
		super().__init__(surface, pos)
		self.view = view

		self._resizable = False
		self.path = path

		self.image = _pygame.image.load(self.path).convert()

		self.action = None

	def create(self):
		self.image = _pygame.image.load(self.path).convert()
		self.surface.blit(self.image, self.rect)

	def scaleToFill(self, view="surface"):
		if view == "surface" and self._resizable:
			self.image = _pygame.transform.scale(self.image, (self.surface.get_width(), self.surface.get_height()))
		elif view == "view" and self._resizable:
			pass

	def onTap(self, action):
		self.action = action

	def update(self, events):
		mouse_pos = _pygame.mouse.get_pos()
		for event in events:
			if event.type == _pygame.MOUSEBUTTONDOWN:
				if self.rect.collidepoint(mouse_pos):
					try:
						self.action()
					except:
						pass

	def frame(self, width=0, height=0):
		if self._resizable:
			pass


class _SpriteImage(_Sprite):
	def __init__(self, imageFolder, rect, scale, flip, fps, angle):
		self.clock = pygame.time.Clock()

		super(_SpriteImage, self).__init__()

		self.imageFolder = os.listdir(imageFolder)
		self.images = []

		self.fps = fps

		self.scale = scale
		self.flip = flip
		self.angle = angle

		for i in self.imageFolder:
			self.images = [pygame.transform.rotate(
				pygame.transform.flip(pygame.transform.scale(pygame.image.load(imageFolder + i), self.scale), self.flip,
									  False), self.angle) for i in self.imageFolder]

		self.index = 0

		self.image = self.images[self.index]

		self.rect = _pygame.Rect(rect)

	def update(self, imageFolder):
		self.clock.tick(self.fps)

		self.images.clear()
		self.imageFolder = os.listdir(imageFolder)
		self.imageFolder.sort(reverse=False)
		for i in self.imageFolder:
			self.images = [pygame.transform.rotate(
				pygame.transform.flip(pygame.transform.scale(pygame.image.load(imageFolder + i), self.scale), self.flip,
									  False), self.angle) for i in self.imageFolder]

		self.index += 0.4

		if self.index > len(self.images):
			self.index = len(self.images) - 1
		self.image = self.images[int(self.index)]

	def returnIndex(self):
		self.index = 0


class ImageAnimation(Widget):
	def __init__(self, surface, rect=None, imageFolder=None, scale=None, flip=None, fps=None, angle=0):
		super().__init__(surface, rect)

		if imageFolder is None:
			imageFolder = ''
		self.imageFolder = imageFolder
		self.scale = scale
		self.flip = flip
		self.fps = fps
		self.angle = angle
		self._imageSprite = _SpriteImage(self.imageFolder, self.rect, scale=self.scale, flip=self.flip, fps=self.fps,
										 angle=self.angle)
		self._groupSprite = pygame.sprite.Group(self._imageSprite)

	def update(self, events):
		self._groupSprite.update(self.imageFolder)

	def returnIndex(self):
		self._imageSprite.returnIndex()

	def create(self):
		self._groupSprite.draw(self.surface)


class Separator(Widget):
	def __init__(self, surface, rect, color):
		super().__init__(surface, rect)

		self.color = color

	def update(self, events): pass

	def create(self):
		pygame.draw.rect(self.surface, self.color, self.rect)


# networking
# Create environment for firebase
cred = credentials.Certificate("data/serviceKey/serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
	'databaseURL': "https://rockpaperscissor-6753d-default-rtdb.asia-southeast1.firebasedatabase.app/"
})


class User:
	def __init__(self, username, uuid, choice=""):
		self.username = username
		self.uid = uuid
		self.choice = choice
		self.highestScore = 0

	def getData(self):
		return {
			self.username: {
				"username": self.username,
				"id": self.uid,
				"choice": self.choice,
				"highest_score": self.highestScore,
			}
		}

	def updateToData(self):
		# Write data directly to database
		data = db.reference("/")
		data.child("Users/").update(self.getData())

	def resetUserData(self):
		# After using data we should delete user data to prevent from overloading
		data = db.reference("/")
		data.child("Users/" + self.username + "/").set({})


class Server:
	def __init__(self, user: User):
		self.user = user
		self.room = db.reference("room/")

	def createRoom(self):
		print(self.user.getData())
		self.room.update(
			{
				self.user.uid: self.user.getData()
			}
		)

	def updateChoice(self, choice):
		self.user.choice = choice
		self.room.child(self.user.uid + "/" + self.user.username).update({"choice": choice})

	def provideRoomID(self) -> str:
		return self.user.uid

	def getChoice(self) -> str:
		return self.user.choice

	def clientChoice(self) -> str:
		userInRoom = self.room.child(self.provideRoomID()).get()

		client = {}

		for user in userInRoom:
			if user != self.user.username:
				client = userInRoom[user]
		try:
			return client["choice"]
		except:
			return ""

	def resetRoomData(self):
		self.room.child(self.provideRoomID()).set({})


class Client:
	def __init__(self, user: User):
		self.user = user
		self.room = db.reference("room/")

	def joinRoom(self, room_id: str) -> bool:
		self.room = self.room.child(room_id + "/")
		userInRoom = 0
		try:
			for i in self.room.get():
				userInRoom += 1
		except:
			userInRoom = -1

		if userInRoom == 1:
			self.room.update(self.user.getData())
			print("tham gia vô vòng", room_id)
			return True
		elif userInRoom == -1:
			print("Khong tim thay")
			return False
		else:
			print("Phòng đầy người")
			return False

	def updateChoice(self, choice):
		self.user.choice = choice
		self.room.child(self.user.username).update({"choice": choice})

	def getChoice(self) -> str:
		return self.user.choice

	def serverChoice(self) -> str:
		userInRoom = self.room.get()

		server = {}

		for user in userInRoom:
			if user != self.user.username:
				server = userInRoom[user]
		try:
			return server["choice"]
		except:
			return ""

	def resetData(self):
		self.room.child(self.user.username).set({})


class Database:
	def __init__(self):
		self.ref = db.reference("/")

	def getUsersName(self) -> list:
		listOfUsers = []
		try:
			for user in self.ref.child("Users/").get():
				listOfUsers.append(user)
		except:
			self.ref.update({
				"Users": {
					"*": "*"
				},

				"room": {
					"*": "*"
				}

			})
			for user in self.ref.child("Users/").get():
				listOfUsers.append(user)
		return listOfUsers

	def getRooms(self) -> list:
		rooms = []
		for room in self.ref.child("room/").get():
			rooms.append(room)
		return rooms

	def getIDS(self) -> list:
		IDS = []
		users = self.getUsersName()
		users.remove("*")
		for user in users:
			IDS.append(self.ref.child("Users/" + user + "/").get()["id"])

		return IDS

	def createID(self) -> str:
		IDS = self.getIDS()
		max_id = [i for i in range(1, 999999)]
		availableID = max_id
		try:
			for i in IDS:
				for j in max_id:
					if int(i) - j == 0:
						availableID.remove(j)
		except:
			availableID = [1]

		return str((6 - len(str(availableID[0]))) * "0" + str(availableID[0]))


# Machine Learning
class Computer:
	def __init__(self):
		self.computer_choices = [1, 2, 3]
		self.history = []
		self.our_state = []

		with open('data/history.txt', 'r') as file:
			self.history = [int(i) for i in file.read()]
		with open('data/history1.txt', 'r') as file1:
			self.our_state = [int(i) for i in file1.read()]

	def easy(self):
		return random.choice(self.computer_choices)

	def medium(self):
		if not self.our_state == 6:
			return random.choice(self.computer_choices)
		elif self.our_state[-1] == 4:
			return self.computer_choices[int(self.history[-2]) - 1]
		elif self.our_state[-1] == 5:
			if self.history[-2] - 1 <= 1:
				return self.computer_choices[self.history[-2]]
			else:
				return self.computer_choices[0]
		else:
			return random.choice(self.computer_choices)

	def hard(self):
		if len(self.history) <= 3:
			return random.choice(self.computer_choices)
		else:
			# Clean and setup data
			player_choice_dict = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}
			our_state_dict = {4: 'Win', 5: 'Lose', 6: 'Draw'}
			fields = ['player_choice', 'our_choice', 'our_state']
			rows = []
			our_choice = 0
			for i in range(len(self.history) - 1):
				if our_state_dict[self.our_state[i]] == 'Draw':
					our_choice = self.history[i]
				elif our_state_dict[self.our_state[i]] == 'Win':
					match player_choice_dict[self.history[i]]:
						case 'Rock':
							our_choice = 2
						case 'Paper':
							our_choice = 3
						case 'Scissors':
							our_choice = 1
				else:
					match player_choice_dict[self.history[i]]:
						case 'Rock':
							our_choice = 3
						case 'Paper':
							our_choice = 1
						case 'Scissors':
							our_choice = 2
				rows.append([self.history[i], our_choice, self.our_state[i]])

			with open('data/temp.csv', 'w') as csv_file:
				csvwriter = csv.writer(csv_file)
				csvwriter.writerow(fields)
				csvwriter.writerows(rows)

			df = pd.read_csv('data/temp.csv')
			features = ['player_choice', 'our_state']
			X = df.dropna(axis=0)[features].values
			y = df.dropna(axis=0)['our_choice']
			X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=0)

			# Train and evaluate models
			dt_model = DecisionTreeClassifier(random_state=1)
			dt_model.fit(X_train, y_train)
			dt_model_score = dt_model.score(X_test, y_test)

			rf_model = RandomForestClassifier(random_state=1)
			rf_model.fit(X_train, y_train)
			rf_model_score = rf_model.score(X_test, y_test)

			# Compare evaluation
			if rf_model_score >= dt_model_score:
				return (rf_model.predict([[self.history[len(self.history) - 1], 4]])[0])
			else:
				return (dt_model.predict([[self.history[len(self.history) - 1], 4]])[0])


# Initialization
FPS = 30

transform = {
	"": 0,
	"rock": 1,
	"scissors": 2,
	"paper": 3
}

data = Database()
allUsers = data.getUsersName()

uuid = data.createID()

user = User("", uuid)


def game_play(player, opponent) -> str:
	if player == opponent:
		return "Draw"
	elif (player == 1 and opponent == 2) or (player == 3 and opponent == 1) or (
			player == 2 and opponent == 3):
		music('win_sound')
		return "Win"
	elif (player == 1 and opponent == 3) or (player == 3 and opponent == 2) or (
			player == 2 and opponent == 1):
		music('lose_sound')
		return "Lose"
	else:
		raise ValueError("Unrecognized value")


def music(name_music):
	win_sound = pygame.mixer.Sound('data/soundeffect/win.mp3')
	lose_sound = pygame.mixer.Sound('data/soundeffect/lose.mp3')
	button_sound = pygame.mixer.Sound('data/soundeffect/button_sound.wav')
	music_background = pygame.mixer.Sound('data/soundeffect/music_background.mp3')

	match name_music:
		case 'win_sound':
			win_sound.play()
			win_sound.set_volume(0.5)
		case 'lose_sound':
			lose_sound.play()
			lose_sound.set_volume(1)
		case 'button_sound':
			button_sound.play()
			button_sound.set_volume(0.3)
		case 'music_background':
			music_background.play()


def writeSizeScreen(size):
	with open('data/size.txt', 'w') as file:
		if size == 'small':
			file.write('680\n')
			file.write('620')
		elif size == 'medium':
			file.write('900\n')
			file.write('700')
		elif size == 'large':
			file.write('1008\n')
			file.write('888')
		elif size == 'fullscreen':
			file.write('fullscreen\n')
			file.write('fullscreen')
	user.resetUserData()

	pygame.quit()
	sys.exit()


class MenuView:
	BUTTON_COLOR = (204, 204, 196)
	BUTTON_RECT_COLOR = (255, 255, 255)
	BUTTON_TEXT_COLOR = '#FFFF00'
	BUTTON_QUIT_COLOR = (32, 178, 170)

	def __init__(self, surface, width, height):
		self.background = None
		self.width = width
		self.height = height

		self.inputBox = InputBox(surface,
									 (surface.get_rect().center[0] - 160, surface.get_rect().center[1] - 150, 100, 60))
		self.button_singleplay = self.create_button(surface, 'SinglePlayer', -50)
		self.button_setting = self.create_button(surface, 'Settings', 150, self.BUTTON_QUIT_COLOR)
		self.button_multiplay = self.create_button(surface, 'MultiPlayer', 50)
		self.button_quit = self.create_button(surface, 'Quit', 250)

		self.button_quit.on_press_action = self.close

		self.groupWidget = GroupWidget()
		self.groupWidget.widgets.extend(
			[self.button_singleplay, self.button_multiplay, self.button_setting, self.button_quit, self.inputBox])

		self.background_image = pygame.image.load('data/menu.png')
		self.background_image = pygame.transform.scale(self.background_image, (int(self.width), int(self.height)))

	def create_button(self, surface, text, y_offset, color=BUTTON_COLOR):
		button = Button(surface, (
			surface.get_rect().center[0] - 80, surface.get_rect().center[1] + y_offset, 150, 60), text=text,
							color=color, bottom_rect_color=self.BUTTON_RECT_COLOR,
							text_color=self.BUTTON_TEXT_COLOR)

		return button

	def close(self):
		try:
			user.resetUserData()
		except:
			print("No user to delete")
		pygame.quit()
		sys.exit()

	def create_widgets(self):
		self.groupWidget.create_widget()

	def update(self, events):
		self.groupWidget.update(events)

	def image_background(self, surface):
		surface.blit(self.background_image, (0, 0))


class SinglePlayerView:

	def __init__(self, surface, width, height, back, who_win, input_text):
		self.width = width
		self.height = height
		self.who_win = who_win
		self.input_text = input_text
		self.clicked = False
		self.imageBot_choice_list = []
		self.numberPlayerChoice = 1

		self.button_action = {
			'rock': self.rock,
			'paper': self.paper,
			'scissors': self.scissors
		}
		self.buttons = {name: self.create_buttons(surface, name.capitalize(), action) for name, action in
						self.button_action.items()}

		self.button_back = Button(surface, (0, 0, 70, 30), 'Back', '#ff6680', bottom_rect_color='#ed7700',
									  text_color='black', text_size=20)
		self.button_back.on_press_action = back

		self.groupWidget_single = GroupWidget()
		self.groupWidget_single.widgets.extend(self.buttons.values())
		self.groupWidget_single.widgets.append(self.button_back)

		# The Image Rock Paper Scissors in Single Player View for player
		self.imagePlayer = ImageAnimation(surface, rect=(20, surface.get_rect().bottomright[1] - 235, 100, 100),
											  imageFolder='data/scissors_animation/', scale=(230, 230), flip=False,
											  fps=60, angle=0)

		# The Image Rock Paper Scissors in Single Player View for bot
		self.imageBot = ImageAnimation(surface, rect=(surface.get_rect().topright[0] - 260, 10, 100, 100),
										   imageFolder='data/scissors_animation/', scale=(230, 230),
										   flip=True, fps=90, angle=90)

		# Blit the text win or lose or draw
		self.who_will_win = Text(surface, (
			surface.get_rect().center[0] - 53, surface.get_rect().center[1] - 20, 50, 50),
									 size=64,
									 color='black', text=self.who_win)
		# The Player Name
		self.playerName = Text(surface, (50, surface.get_rect().bottomright[1] - 100, 50, 50), size=32,
								   color='black',
								   text=self.input_text)
		# The Bot nAME
		self.bot = Text(surface, (surface.get_rect().topright[0] - 130, 80, 50, 50), size=32, color='black',
							text='Bot')

		self.backgroundImageSinglePlayer = pygame.image.load('data/background.png')
		self.backgroundImageSinglePlayer = pygame.transform.scale(self.backgroundImageSinglePlayer,
																  (int(self.width) + 90, int(self.height) + 90))

	def create_buttons(self, surface, text, action, x_offset=0):
		match text:
			case 'Rock':
				x_offset = 300
			case 'Scissors':
				x_offset = 200
			case 'Paper':
				x_offset = 100
		button = Button(surface, rect=(
			surface.get_rect().bottomright[0] - x_offset, surface.get_rect().bottomright[1] - 80, 90, 50), text=text,
							color='#ff6680', bottom_rect_color='#ed7700', text_color='black', text_size=23)
		button.on_press_action = action
		return button

	def create_widgets(self):
		self.groupWidget_single.create_widget()

	def update(self, events):
		self.groupWidget_single.update(events)

	def rock(self):
		self.who_win, self.numberPlayerChoice = self.which_button_rpg_clicked(1)
		self.imagePlayer.imageFolder = 'data/rock_animation/'
		music('button_sound')

	def paper(self):
		self.who_win, self.numberPlayerChoice = self.which_button_rpg_clicked(3)
		self.imagePlayer.imageFolder = 'data/paper_animation/'
		music('button_sound')

	def scissors(self):
		self.who_win, self.numberPlayerChoice = self.which_button_rpg_clicked(2)
		self.imagePlayer.imageFolder = 'data/scissors_animation/'
		music('button_sound')

	def which_button_rpg_clicked(self, playerChoice):
		self.clicked = True

		self.imageBot.returnIndex()
		self.imagePlayer.returnIndex()
		difficulty = self.getDifficulty()

		if difficulty == "easy":
			imageBot_choice = Computer().easy()
		elif difficulty == "medium":
			imageBot_choice = Computer().medium()
		elif difficulty == "hard":
			imageBot_choice = Computer().hard()
		else:
			imageBot_choice = Computer().easy()

		self.imageBot_choice_list.append(imageBot_choice)
		self.imageBot_choice_list = self.imageBot_choice_list[-1:]

		rpg_choice = {1: 'rock',
					  2: 'scissors',
					  3: 'paper'
					  }
		ourState = {
			'Win': '4',
			'Lose': '5',
			'Draw': '6'
		}

		self.imageBot.imageFolder = 'data/' + rpg_choice[self.imageBot_choice_list[-1]] + '_animation/'

		self.who_win = game_play(playerChoice, self.imageBot_choice_list[-1])

		with open('data/history.txt', 'a') as file:
			file.write(str(playerChoice))
		with open('data/history1.txt', 'a') as file1:
			file1.write(ourState[self.who_win])

		return self.who_win, self.numberPlayerChoice

	def backgroundImageSingle(self, surface):
		surface.blit(self.backgroundImageSinglePlayer, (-50, -50))

	def getDifficulty(self):
		with open("data/difficulty.txt", 'r') as f:
			return f.readline()


class ServerView(Widget):
	def __init__(self, surface, on_back_press):
		rect = (0, 0, surface.get_width(), surface.get_height())
		super().__init__(surface, rect)
		# Networking
		self.server = Server(user)
		try:
			self.server.createRoom()
		except:
			pass
		self.room = self.server.provideRoomID()
		self.isJoin = False
		self.isChoose = False
		self.who_win = ""

		# View
		self.view = GroupWidget()
		self.button_rock = Button(surface, (
			surface.get_rect().bottomright[0] - 300, surface.get_rect().bottomright[1] - 80, 90, 50), 'Rock', '#ff6680',
									  bottom_rect_color='#ed7700', text_color='black', text_size=23)

		self.button_scissors = Button(surface, (
			surface.get_rect().bottomright[0] - 200, surface.get_rect().bottomright[1] - 80, 90, 50), 'Scissors',
										  '#ff6680',
										  bottom_rect_color='#ed7700', text_color='black', text_size=23)

		self.button_paper = Button(surface, (
			surface.get_rect().bottomright[0] - 100, surface.get_rect().bottomright[1] - 80, 90, 50), 'Paper',
									   '#ff6680',
									   bottom_rect_color='#ed7700',
									   text_color='black', text_size=23)

		self.button_back = Button(self.surface, (0, 0, 70, 30), 'Back', '#ff6680', bottom_rect_color='#ed7700',
									  text_color='black', text_size=20)

		self.imagePlayer = ImageAnimation(surface, rect=(20, surface.get_rect().bottomright[1] - 235, 100, 100),
											  imageFolder='data/rock_animation/', scale=(230, 230), flip=False,
											  fps=60, angle=0)

		# The Image Rock Paper Scissors in Single Player View for bot
		self.imageOpponent = ImageAnimation(surface, rect=(surface.get_rect().topright[0] - 260, 10, 100, 100),
												imageFolder='data/rock_animation/', scale=(230, 230),
												flip=True, fps=90, angle=90)
		self.who_will_win = Text(surface, (
			surface.get_rect().center[0] - 53, surface.get_rect().center[1] - 20, 50, 50),
									 size=64,
									 color='black', text=self.who_win)
		self.message = ""
		self.messageText = Text(self.surface, (150, 20, 100, 60), color=(255, 0, 0),
									size=40,
									text=self.message)

		# Action for button
		self.button_rock.on_press_action = self.on_rock_press
		self.button_paper.on_press_action = self.on_paper_press
		self.button_scissors.on_press_action = self.on_scissors_press
		self.button_back.on_press_action = on_back_press

		self.view.widgets.append(self.button_rock)
		self.view.widgets.append(self.button_back)
		self.view.widgets.append(self.button_paper)
		self.view.widgets.append(self.button_scissors)
		self.view.widgets.append(self.imagePlayer)
		self.view.widgets.append(self.imageOpponent)

	def create(self):
		self.who_will_win.create(self.who_win)
		self.messageText.create(self.message)
		self.view.create_widget()

	def update(self, events):
		self.message = "Room ID:" + self.room
		try:
			client = self.server.clientChoice()
		except:
			client = "101"
			print("123")
		if not self.isChoose:
			self.server.updateChoice("")
		else:
			self.who_win = "Choose rock paper or scissors"
		if client != "":
			try:
				self.who_win = game_play(transform[self.server.getChoice()], transform[client])
			except:
				pass

			if self.isChoose:
				self.imageOpponent.imageFolder = "data/" + client + "_animation/"
			self.isChoose = False
		elif client == "" and self.isChoose:
			self.who_win = "Wait your opponent"
		if client == "101":
			self.who_win = "Wait your opponent to join the room\nThe room id:" + self.server.provideRoomID()
		self.view.update(events)

	def on_rock_press(self):
		self.imagePlayer.imageFolder = "data/rock_animation/"
		music('button_sound')
		self.play("rock")

	def on_scissors_press(self):
		self.imagePlayer.imageFolder = "data/scissors_animation/"
		music('button_sound')
		self.play("scissors")

	def on_paper_press(self):
		self.imagePlayer.imageFolder = "data/paper_animation/"
		music('button_sound')
		self.play("paper")

	def play(self, choice):
		self.server.updateChoice(choice)
		self.isChoose = True


class ClientView(Widget):
	def __init__(self, surface, on_back_press):
		self.server = None
		rect = (0, 0, surface.get_width(), surface.get_height())
		super().__init__(surface, rect)

		self.who_win = "Fight"

		self.client = Client

		self.view = GroupWidget()
		self.button_rock = Button(surface, (
			surface.get_rect().bottomright[0] - 300, surface.get_rect().bottomright[1] - 80, 90, 50), 'Rock', '#ff6680',
									  bottom_rect_color='#ed7700', text_color='black', text_size=23)

		self.button_scissors = Button(surface, (
			surface.get_rect().bottomright[0] - 200, surface.get_rect().bottomright[1] - 80, 90, 50), 'Scissors',
										  '#ff6680',
										  bottom_rect_color='#ed7700', text_color='black', text_size=23)

		self.button_paper = Button(surface, (
			surface.get_rect().bottomright[0] - 100, surface.get_rect().bottomright[1] - 80, 90, 50), 'Paper',
									   '#ff6680',
									   bottom_rect_color='#ed7700',
									   text_color='black', text_size=23)

		self.button_back = Button(self.surface, (0, 0, 70, 30), 'Back', '#ff6680', bottom_rect_color='#ed7700',
									  text_color='black', text_size=20)

		self.imagePlayer = ImageAnimation(surface, rect=(20, surface.get_rect().bottomright[1] - 235, 100, 100),
											  imageFolder='data/rock_animation/', scale=(230, 230), flip=False,
											  fps=60, angle=0)

		# The Image Rock Paper Scissors in Single Player View for bot
		self.imageOpponent = ImageAnimation(surface, rect=(surface.get_rect().topright[0] - 260, 10, 100, 100),
												imageFolder='data/rock_animation/', scale=(230, 230),
												flip=True, fps=90, angle=90)

		self.who_will_win = Text(surface, (
			surface.get_rect().center[0] - 53, surface.get_rect().center[1] - 20, 50, 50),
									 size=64,
									 color='black', text=self.who_win)  # Action for button
		self.message = ""
		self.messageText = Text(self.surface, (self.surface.get_rect().center[0] - 160,
												   self.surface.get_rect().center[1] - 170, 100, 60), color=(255, 0, 0),
									text=self.message)

		self.button_rock.on_press_action = self.on_rock_press
		self.button_paper.on_press_action = self.on_paper_press
		self.button_scissors.on_press_action = self.on_scissors_press
		self.button_back.on_press_action = on_back_press

		self.view.widgets.append(self.button_rock)
		self.view.widgets.append(self.button_back)
		self.view.widgets.append(self.button_paper)
		self.view.widgets.append(self.button_scissors)
		self.view.widgets.append(self.imagePlayer)
		self.view.widgets.append(self.imageOpponent)

		# networking
		self.room = ""
		self.client = Client(user)
		self.isJoin = False
		self.isChoose = False

	def create(self):
		self.who_will_win.create(self.who_win)
		self.messageText.create(self.message)
		self.view.create_widget()

	def update(self, events):
		if not self.isJoin:
			self.client.joinRoom(self.room)
			print("Joined to room id:", self.room)
			self.isJoin = True
		self.view.update(events)

		server = self.client.serverChoice()
		if not self.isChoose:
			self.client.updateChoice("")
		else:
			self.who_win = "Choose rock paper or scissors"
		if server != "":
			try:
				self.who_win = game_play(transform[self.client.getChoice()], transform[server])
			except:
				pass

			if self.isChoose:
				self.imageOpponent.imageFolder = "data/" + server + "_animation/"
			self.isChoose = False
		elif server == "" and self.isChoose:
			self.who_win = "Wait your opponent"

	def on_rock_press(self):
		self.imagePlayer.imageFolder = "data/rock_animation/"
		music('button_sound')
		self.play("rock")

	def on_scissors_press(self):
		self.imagePlayer.imageFolder = "data/scissors_animation/"
		music('button_sound')
		self.play("scissors")

	def on_paper_press(self):
		self.imagePlayer.imageFolder = "data/paper_animation/"
		music('button_sound')
		self.play("paper")

	def play(self, choice):
		self.client.updateChoice(choice)
		self.isChoose = True


class SelectClientServerView(Widget):
	def __init__(self, surface, back_action):
		rect = (0, 0, surface.get_width(), surface.get_height())
		super().__init__(surface, rect)

		# Networking

		# View
		self.view = GroupWidget()

		# Layer for view
		self.layer = {
			"selection": True,
			"server": False,
			"client": False
		}

		# Create the button for view
		self.roomInputBox = InputBox(self.surface, (
			self.surface.get_rect().center[0] - 150, self.surface.get_rect().center[1] - 150, 100, 60))

		self.joinRoomButton = Button(self.surface, (
			self.surface.get_rect().center[0] - 80, self.surface.get_rect().center[1] - 50, 160, 60),
										 text='Join Room',
										 color=(32, 178, 170), bottom_rect_color=(255, 255, 255))
		self.joinRoomButton.on_press_action = self.joinRoom

		self.createRoomButton = Button(self.surface, (
			self.surface.get_rect().center[0] - 80, self.surface.get_rect().center[1] + 50, 160, 60),
										   text='Create Room',
										   color=(32, 178, 170), bottom_rect_color=(255, 255, 255))
		self.createRoomButton.on_press_action = self.createRoom

		self.button_back = Button(surface, (0, 0, 70, 30), 'Back', '#ff6680', bottom_rect_color='#ed7700',
									  text_color='black', text_size=20)
		self.button_back.on_press_action = back_action

		self.message = ""
		self.messageText = Text(self.surface, (self.surface.get_rect().center[0] - 160,
												   self.surface.get_rect().center[1] - 170, 100, 60), color=(255, 0, 0),
									text=self.message)

		self.view.widgets = [
			self.roomInputBox,
			self.joinRoomButton,
			Separator(self.surface,
						  (self.surface.get_rect().center[0] - 80, self.surface.get_rect().center[1] + 25, 150, 2),
						  (0, 0, 0)),
			self.createRoomButton,
			self.button_back,
		]
		self.serverView = ServerView(self.surface, self.backToSelection)
		self.clientView = ClientView(self.surface, self.backToSelection)

	def update(self, events):
		if self.layer["selection"]:
			self.view.update(events)
		elif self.layer['server']:
			self.serverView.update(events)
		elif self.layer['client']:
			self.clientView.update(events)

	def create(self):
		if self.message != "":
			self.messageText.create(self.message)
		if self.layer["selection"]:
			self.view.create_widget()
		elif self.layer['server']:
			self.serverView.create()
		elif self.layer['client']:
			self.clientView.create()

	def joinRoom(self):
		if self.roomInputBox.text not in data.getRooms():
			self.message = "Type room again"
		else:
			self.message = ""
			self.clientView.room = self.roomInputBox.text
			self.layer['selection'] = False
			self.layer['server'] = False
			self.layer['client'] = True

	def createRoom(self):
		print("Created room successfully")
		self.layer['selection'] = False
		self.layer['server'] = True
		self.layer['client'] = False

	def backToSelection(self):
		user.resetUserData()
		print("Reset user data")
		self.layer['selection'] = True
		self.layer['server'] = False
		self.layer['client'] = False


class MultiPlayerView(Widget):
	def __init__(self, surface, back_action):
		rect = (0, 0, surface.get_width(), surface.get_height())
		super().__init__(surface, rect)

		self.view = GroupWidget()

		# Networking
		self.user_infor = None

		self.selectionView = SelectClientServerView(surface, back_action)

		self.view.widgets = [
			self.selectionView
		]

	def create(self):
		self.view.create_widget()

	def update(self, events):
		self.view.update(events)


class Settings:
	BUTTON_COLOR = (204, 204, 196)
	BUTTON_RECT_COLOR = (255, 255, 255)
	BUTTON_TEXT_COLOR = '#FFFF00'
	BUTTON_QUIT_COLOR = (32, 178, 170)

	def __init__(self, surface, width, height, func_back, view, settingView):
		self.groupWidget_chooseDifficulty = None
		self.labelAnouncementEasy = None
		self.width = width
		self.height = height
		self.surface = surface
		self.view = view
		self.settingsView = settingView

		self.resizeWindow = self.create_button(surface, 'Resize Window', -150)
		self.resizeWindow.on_press_action = self.resize

		self.difficulty = self.create_button(surface, 'Difficulty', -50)
		self.difficulty.on_press_action = self.choose_difficulty

		self.button_back = Button(surface, (0, 0, 70, 30), 'Back', '#ff6680', bottom_rect_color='#ed7700',
									  text_color='black', text_size=20)
		self.button_back.on_press_action = func_back

		self.groupWidget_settings = GroupWidget()
		self.groupWidget_settings.widgets.extend([self.resizeWindow, self.button_back, self.difficulty])

		self.groupWidget_resize = GroupWidget()

		self.difficultyString = "Default difficulty is Medium"

	def create_button(self, surface, text, y_offset, color=BUTTON_COLOR):
		button = Button(surface, (
			surface.get_rect().center[0] - 80, surface.get_rect().center[1] + y_offset, 150, 60), text=text,
							color=color, bottom_rect_color=self.BUTTON_RECT_COLOR,
							text_color=self.BUTTON_TEXT_COLOR)
		return button

	def create_widgets(self):
		self.groupWidget_settings.create_widget()

	def update(self, events):
		self.groupWidget_settings.update(events)

	def resize(self):
		self.settingsView['Resize Window'] = True

		resizeSmallButton = self.create_button(self.surface, 'Small', -150)
		resizeSmallButton.on_press_action = self.resize_small

		resizeMediumButton = self.create_button(self.surface, 'Medium', -50)
		resizeMediumButton.on_press_action = self.resize_medium

		resizeLargeButton = self.create_button(self.surface, 'Large', 50)
		resizeLargeButton.on_press_action = self.resize_large

		resizeFullScreenButton = self.create_button(self.surface, 'Full Screen', 150)
		resizeFullScreenButton.on_press_action = self.resize_fullscreen

		resizeBackButton = Button(self.surface, (0, 0, 70, 30), 'Back', '#ff6680', bottom_rect_color='#ed7700',
									  text_color='black', text_size=20)
		resizeBackButton.on_press_action = self.resize_back

		self.label_anouncement = Text(self.surface, (
			self.surface.get_rect().center[0] - 240, self.surface.get_rect().center[1] - 250, 150, 60),
										  text='After resize your screen game, you need to restart game', color='black')

		self.groupWidget_resize.widgets.append(resizeSmallButton)
		self.groupWidget_resize.widgets.extend(
			[resizeSmallButton, resizeMediumButton, resizeLargeButton, resizeFullScreenButton, resizeBackButton])

	def resizeCreateUpdate(self, events):
		self.groupWidget_resize.create_widget()
		self.groupWidget_resize.update(events)
		self.label_anouncement.create(text='After resize your screen game, you need to restart')

	def resize_back(self):
		self.settingsView['Resize Window'] = False

	def resize_small(self):
		writeSizeScreen('small')

	def resize_medium(self):
		writeSizeScreen('medium')

	def resize_large(self):
		writeSizeScreen('large')

	def resize_fullscreen(self):
		writeSizeScreen('fullscreen')

	def on_easy(self):
		with open("data/difficulty.txt", 'w') as f:
			f.write("easy")

		self.difficultyString = "Difficulty: Easy"

	def on_medium(self):
		with open("data/difficulty.txt", 'w') as f:
			f.write("medium")

		self.difficultyString = "Difficulty: Medium"

	def on_hard(self):
		with open("data/difficulty.txt", 'w') as f:
			f.write("hard")

		self.difficultyString = "Difficulty: Hard"

	def choose_difficulty(self):
		self.settingsView['Difficulty'] = True

		easyButton = self.create_button(self.surface, text='Easy Mode', y_offset=-50)
		mediumButton = self.create_button(self.surface, text="Medium mode", y_offset=50)
		difficultyButton = self.create_button(self.surface, text='Difficult Mode', y_offset=+150)

		easyButton.on_press_action = self.on_easy
		mediumButton.on_press_action = self.on_medium
		difficultyButton.on_press_action = self.on_hard

		resizeBackButtonDiff = Button(self.surface, (0, 0, 70, 30), 'Back', '#ff6680', bottom_rect_color='#ed7700',
										  text_color='black', text_size=20)
		resizeBackButtonDiff.on_press_action = self.resizeBackButtonDiff

		self.labelAnouncementEasy = Text(self.surface, (
			self.surface.get_rect().center[0] - 140, self.surface.get_rect().center[1] - 250, 150, 60),
											 text=self.difficultyString, color='black')

		self.groupWidget_chooseDifficulty = GroupWidget()
		self.groupWidget_chooseDifficulty.widgets.extend(
			[easyButton, mediumButton, difficultyButton, resizeBackButtonDiff])

	def chooseDifficultyCreateUpdate(self, events):
		self.groupWidget_chooseDifficulty.create_widget()
		self.groupWidget_chooseDifficulty.update(events)
		with open("data/difficulty.txt", 'r') as f:
			difficulty = f.readline()
			self.difficultyString = "Difficult: " + difficulty
		self.labelAnouncementEasy.create(text=self.difficultyString)

	def resizeBackButtonDiff(self):
		self.settingsView['Difficulty'] = False


class RockPaperScissor:
	def __init__(self):
		self.imageBot_choice = None
		self.width, self.height = self.readSizeScreen()
		if self.width == 'fullscreen':
			self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		else:
			self.screen = pygame.display.set_mode((int(self.width), int(self.height)))

		self.clock = pygame.time.Clock()

		self.view = {
			'Main Menu': True,
			'SinglePlay Menu': False,
			'Settings Menu': False,
			"MultiPlay Mene": False,
			'Back': False
		}
		self.SetingsView = {
			'Resize Window': False,
			'Difficulty': False
		}

		self.playerChoice = ''
		self.numberPlayerChoice = 0
		self.imageBot_choice_list = []
		self.who_win = 'Fight'
		self.clicked = False

		# Main widgets which contain all widget on screen but at first it's empty
		# You have to add your own widget after creating it
		# Use this code to add widget: self.groupWidgets.widgets.append(<widget>)

		# The Menu Screen
		self.menuView = MenuView(self.screen, self.width, self.height)  # Create the menu
		self.menuView.button_singleplay.on_press_action = self.single_play
		self.menuView.button_setting.on_press_action = self.setting
		self.menuView.button_multiplay.on_press_action = self.multi_play

		# The Single Player View
		self.singlePlayerView = SinglePlayerView(self.screen, self.width, self.height,
												 self.back, self.who_win, self.menuView.inputBox.text)
		# The Multi Player View
		self.multiPlayerView = MultiPlayerView(self.screen, self.back)

		# The Settings View
		self.settingsView = Settings(self.screen, self.width, self.height, self.back, self.view, self.SetingsView)

		music('music_background')
		# Message
		self.message = ""
		self.messageText = Text(self.screen,
									(self.screen.get_rect().center[0] - 160,
									 self.screen.get_rect().center[1] - 170, 100, 60),
									color=(255, 0, 0))

	def run(self):

		while True:
			self.screen.fill((0, 0, 0))
			# Fill the screen with BLACK instead of an empty screen
			self.menuView.image_background(self.screen)

			# Event
			events = pygame.event.get()
			for event in events:
				if event.type == pygame.QUIT:
					self.close()
			if self.message != "":
				self.messageText.create(self.message)
			if self.view['SinglePlay Menu']:
				self.singlePlayerView.backgroundImageSingle(self.screen)

				self.singlePlayerView.create_widgets()
				self.singlePlayerView.update(events)

				self.singlePlayerView.imagePlayer.create()
				self.singlePlayerView.imageBot.create()

				if self.singlePlayerView.clicked:
					self.singlePlayerView.imagePlayer.update(events)
					self.singlePlayerView.imageBot.update(events)

					self.singlePlayerView.who_will_win.create(self.singlePlayerView.who_win)
				self.singlePlayerView.playerName.create(self.menuView.inputBox.text)
				self.singlePlayerView.bot.create('Bot')
			elif self.view['Settings Menu']:

				if self.settingsView.settingsView['Resize Window']:
					self.settingsView.resizeCreateUpdate(events)
				elif self.settingsView.settingsView['Difficulty']:
					self.settingsView.chooseDifficultyCreateUpdate(events)
				else:
					self.settingsView.create_widgets()
					self.settingsView.update(events)
			elif self.view['Main Menu']:
				self.menuView.create_widgets()
				self.menuView.update(events)
			elif self.view['MultiPlay Menu']:
				self.multiPlayerView.update(events)
				self.multiPlayerView.create()

			# Update and set FPS
			self.clock.tick(FPS)

			pygame.display.flip()
			pygame.display.update()

	def single_play(self):
		self.view['SinglePlay Menu'] = True
		self.view['Settings Menu'] = False
		self.view['MultiPlay Menu'] = False
		self.view['Main Menu'] = False

	def back(self):
		self.view['SinglePlay Menu'] = False
		self.view['Settings Menu'] = False
		self.view['MultiPlay Menu'] = False
		self.view['Main Menu'] = True

	##########
	# Warning: This code has to be inside the setting view class, not here
	def setting(self):
		self.view['SinglePlay Menu'] = False
		self.view['Settings Menu'] = True
		self.view['MultiPlay Menu'] = False
		self.view['Main Menu'] = False

	def backSettings(self):
		self.SetingsView['Resize Window'] = False
		self.view['Settings Menu'] = True

	##########

	def multi_play(self):
		if self.menuView.inputBox.text == "":
			self.message = "Please type your name"
		elif self.menuView.inputBox.text in data.getUsersName():
			self.message = "This name has been used"
		elif self.multiPlayerView.selectionView.roomInputBox.text == "":
			self.message = "Please type your room"
			self.message = ""

			self.view['SinglePlay Menu'] = False
			self.view['Settings Menu'] = False
			self.view['MultiPlay Menu'] = True
			self.view['Main Menu'] = False
			user.username = self.menuView.inputBox.text

			print("Update user's data")
			user.updateToData()

	def close(self):
		# self.user.resetUserData()
		pygame.quit()
		sys.exit()

	@staticmethod
	def readSizeScreen():
		with open('data/size.txt', 'r') as file:
			size = [i.rstrip() for i in file.readlines()]
		return size


game = RockPaperScissor()
game.run()
