import networking

host = int(input("chọn server hay client: "))

data = networking.Database()


def gameplay(server, client, host=""):
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
	uuid = "000000"

	name = input("Tên: ")
	while name in data.getUsersName():
		print("Tên đã có người dùng")
		name = input("Tên: ")
	user = networking.User(name, uuid)

	server = networking.Server(user)
	server.createRoom()

	while True:
		server.updateChoice("")

		choice = input("chọn: ")
		server.updateChoice(choice)
		while True:
			client = server.clientChoice()
			if client != "":
				gameplay(server.getChoice(), client, "server")
				break
			else:
				continue


elif host == 0:
	uuid = "000001"

	name = input("Tên: ")
	while name in data.getUsersName():
		print("Tên đã có người dùng")
		name = input("Tên: ")

	user = networking.User(name, uuid)

	client = networking.Client(user)

	room = input("phong: ")
	while room not in data.getRooms():
		print("Khong tim thay phong")
		room = input("phong: ")
	while not client.joinRoom(room):
		room = input("phong: ")

	while True:
		client.updateChoice("")

		choice = input("chọn: ")
		client.updateChoice(choice)

		while True:
			server = client.serverChoice()
			if server != "":
				gameplay(server, client.getChoice(), "client")
				break
			else:
				continue
