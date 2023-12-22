import firebase_admin
from firebase_admin import credentials, db
import json

cred = credentials.Certificate("data/serviceKey/serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
	'databaseURL': "https://rockpaperscissor-6753d-default-rtdb.asia-southeast1.firebasedatabase.app/"
})

room = db.reference("room/")


