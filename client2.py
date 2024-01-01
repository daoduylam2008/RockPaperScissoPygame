import networking

host = int(input("chọn server hay client: "))
	
data = networking.Database()

print(data.getIDS())

allUsers = data.getUsersName()

uuid = data.createID()
print("ID của bạn là", uuid)
print("phòng: ", uuid)

transform = {
	"rock": "bua",
	"scissors": "keo",
	"paper": "bao"
}


def gameplay(server, client, host=""):
	client = transform[client]
	if server == client:
		print("draw")
	elif (server == "keo" and client == "bao") or (server == "bua" and client == "keo") or (
			server == "bao" and client == "bua"):
		if host == "server":
			print("win")
		else:
			print("lose")
	else:
		if host == "client":
			print("win")
		else:
			print("lose")


if host == 1:
	name = input("Tên: ")
	while name in data.getUsersName():
		print("Tên đã có người dùng")
		name = input("Tên: ")
	user = networking.User(name, uuid)
	user.updateToData()

	server = networking.Server(user)
	server.createRoom()

	while True:
		server.updateChoice("")

		choice = input("chọn: ")
		if choice == "QUIT()":
			break
		server.updateChoice(choice)
		while True:
			client = server.clientChoice()
			if client != "":
				gameplay(server.getChoice(), client, "server")
				break
			else:
				continue

	server.resetRoomData()
	user.resetUserData()


elif host == 0:
	name = input("Tên: ")
	while name in data.getUsersName():
		print("Tên đã có người dùng")
		name = input("Tên: ")

	user = networking.User(name, uuid)
	user.updateToData()

	client = networking.Client(user)

	room = input("phong: ")
	while room not in data.getRooms():
		if room == "QUIT()":
			break
		room = input("phong: ")
	while not client.joinRoom(room):
		if room == "QUIT()":
			break
		room = input("phong: ")

	while True:
		if room == "QUIT()":
			break

		client.updateChoice("")

		choice = input("chọn: ")

		if choice == "QUIT()":
			break

		client.updateChoice(choice)

		while True:
			server = client.serverChoice()
			if server != "":
				gameplay(server, client.getChoice(), "client")
				break
			else:
				continue

	user.resetUserData()
	client.resetData()
