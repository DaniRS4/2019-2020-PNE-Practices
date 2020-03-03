from Client0 import Client

IP = "212.128.253.172"
PORT = 8083

for i in range(5):

    c = Client(IP, PORT)

    c.debug_talk(f"Message {i}")