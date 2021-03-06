import socket
import termcolor

IP = "212.128.253.128"
PORT = 8080
# -- Step 1: Create a socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Step 2: Bind socket to server's IP address and port
ls.bind((IP, PORT))

# -- Step 3: Convert into a listening socket
ls.listen()

print("EL server está activado")

while True:

    # -- Wait for client to connect
    print("Waiting for Clients to connect")
    try:
        (cs, client_ip_port) = ls.accept()

        print("A client has connected to the server!")
    except KeyboardInterrupt:
        print("Hola que tal?")
        ls.close
        exit()

    # -- Read the message from the client
    # -- The received message is in raw bytes
    msg_raw = cs.recv(2048)

    # -- We decode it for converting it
    # -- into a human-redeable string
    msg = msg_raw.decode()
    msg_color = termcolor.colored(msg, 'green')

    # -- Print the received message
    print(f"Received Message: {msg_color}")

    response = (f"{msg}\n")
    cs.send(response.encode())


    # -- Close the socket


    cs.close()