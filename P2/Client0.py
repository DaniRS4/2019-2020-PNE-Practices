# -- init method --
class Client:
    def __init__(self,IP,PORT):
        self.IP=IP
        self.PORT=PORT
    def ping(self):
        print("OK")
        return self

IP="1"
PORT="1"
c=Client(IP,PORT)

print(c.ping())