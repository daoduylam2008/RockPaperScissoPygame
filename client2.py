import firebase_admin
from firebase_admin import credentials, db
import json


class Client:
	def __init__(self, username, uuid, choice=""):
		self.username = username
		self.uid = uuid
		self.choice = choice

	def getData(self):
		return {
			self.username: {
				"username": self.username,
				"id": self.uid,
				"choice": self.choice
			}
		}


cred = credentials.Certificate("data/serviceKey/serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
	'databaseURL': "https://rockpaperscissor-6753d-default-rtdb.asia-southeast1.firebasedatabase.app/"
})


uid = "000000"
name = input("Name: ")

user = Client(name, uid)

room = db.reference("room/")
room.update(
	{
		user.uid: user.getData()
	}
)

while True:
	choice = input("chọn: ")
	room.child(uid+"/"+name).update({"choice": choice})
