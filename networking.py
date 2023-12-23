import firebase_admin
from firebase_admin import credentials, db, firestore
import json

cred = credentials.Certificate("data/serviceKey/serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
	'databaseURL': "https://rockpaperscissor-6753d-default-rtdb.asia-southeast1.firebasedatabase.app/"
})

u = db.reference("/")
u.set(
	{
		"Users": {
			"*": "*"
		},
		"room": {
			"*": "*"
		}
	}
)


class User:
	def __init__(self, username, uuid, choice=""):
		self.username = username
		self.uid = uuid
		self.choice = choice
		self.highestScore = 0

		self.updateToData()

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
		data = db.reference("/")
		data.child("Users/").update({self.username: self.getData()})


class Server:
	def __init__(self, user: User):
		self.user = user
		self.room = db.reference("room/")

	def createRoom(self):
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
		userInRoom = dict(self.room.child(self.provideRoomID()).get())

		client = {}

		for user in userInRoom:
			if user != self.user.username:
				client = userInRoom[user]
		try:
			return client["choice"]
		except:
			return ""


class Client:
	def __init__(self, user: User):
		self.user = user
		self.room = db.reference("room/")

	def joinRoom(self, room_id: str):
		self.room = self.room.child(room_id + "/")
		self.room.update(self.user.getData())

	def updateChoice(self, choice):
		self.user.choice = choice
		self.room.child(self.user.username).update({"choice": choice})

	def getChoice(self) -> str:
		return self.user.choice

	def serverChoice(self) -> str:
		userInRoom = dict(self.room.get())

		server = {}

		for user in userInRoom:
			if user != self.user.username:
				server = userInRoom[user]
		try:
			return server["choice"]
		except:
			return ""
