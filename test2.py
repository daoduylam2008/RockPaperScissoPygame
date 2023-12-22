import networking

host = int(input("chọn server hay client: "))


def gameplay(server, client):
	if server == client:
		print("draw")

	elif (server == "keo" and client == "bao") or (server == "bua" and client == "keo") or (server == "bao" and client == "bua"):
		print("win")
	else:
		print("lose")


if host == 1:
	uuid = "000000"
	name = input("Tên: ")
	user = networking.User(name, uuid)

	server = networking.Server(user)
	server.createRoom()

	while True:
		server.updateChoice("")

		choice = input("chọn: ")
		server.updateChoice(choice)
		client = server.clientChoice()
		while True:
			if client != "":
				gameplay(server.getChoice(), client)
				break
			else:
				continue


elif host == 0:
	uuid = "000001"
	name = input("ten: ")
	room = input("phong: ")
	user = networking.User(name, uuid)

	client = networking.Client(user)
	client.joinRoom(room)

	while True:
		client.updateChoice("")

		choice = input("chọn: ")
		client.updateChoice(choice)

		server = client.serverChoice()
		while True:
			if client != "":
				gameplay(server, client.getChoice())
				break
			else:
				continue
