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
		pass

	def resetUserData(self):
		pass


class Server:
	def __init__(self, user: User):
		self.user = user
		self.room = ""

	def createRoom(self):
		print(self.user.getData())

	def updateChoice(self, choice):
		self.user.choice = choice

	def provideRoomID(self) -> str:
		return self.user.uid

	def getChoice(self) -> str:
		return self.user.choice

	def clientChoice(self):
		pass

	def resetRoomData(self):
		pass


class Client:
	def __init__(self, user: User):
		self.user = user

	def joinRoom(self, room_id: str):
		pass

	def updateChoice(self, choice):
		self.user.choice = choice

	def getChoice(self) -> str:
		return self.user.choice

	def serverChoice(self):
		pass

	def resetData(self): pass


class Database:
	def __init__(self):
		pass

	def getUsersName(self) -> list:
		listOfUsers = []
		return listOfUsers

	def getRooms(self) -> list:
		rooms = []
		return rooms

	def getIDS(self) -> list:
		IDS = []

		return IDS

	def createID(self) -> str:
		return "000000"