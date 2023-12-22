import networking

host = input("chọn server hay client: ")


if host == 1:
	uuid = "000000"
	name = input("Tên")
	user = networking.User(name, uuid)

	server = networking.Server(user)
	server.createRoom()

	while True:
		choice = input("chọn: ")
		server.updateChoice(choice)

elif host == 0:
	pass
