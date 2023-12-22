import firebase_admin
from firebase_admin import credentials, db
import json

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