# -- Client chat example
import socket

# SERVER IP, PORT
PORT = 8081
IP = "212.128.253.171"

while True:
    # -- Ask the user for a message
    m = input("Message to send: ")

    # -- Create the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Establish the connection to the Server (IP, PORT)
    s.connect((IP, PORT))

    # Send data
    s.send(str.encode(m))

    # Closing the socket
    s.close()
