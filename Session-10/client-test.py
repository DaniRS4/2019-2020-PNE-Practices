from Client0 import Client

<<<<<<< HEAD
IP = "212.128.253.128"
PORT = 8080
c = Client(IP, PORT)
talk = 'Message'

for e in range(5):
    talk += str(e)
    c.debug_talk(talk)
    talk = "Message"
=======
IP = "212.128.253.172"
PORT = 8083

for i in range(5):

    c = Client(IP, PORT)

    c.debug_talk(f"Message {i}")
>>>>>>> origin/master
