import socket

IP = "212.128.253.172"
PORT = 8081

# ---We create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# --- Establishing the connection with the server
s.connect((IP, PORT))

# --- Send data to the server
s.send(str.encode("Cristina Cifuentes borra de su currículum el máster de la Universidad Rey Juan Carlos"))

# --- Receive data from the server
msg = s.recv(2000)

print("Message from the server; ")
print(msg.decode("utf-8"))

# --- Closing the connection
s.close()
