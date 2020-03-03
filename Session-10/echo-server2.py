import socket

IP = "212.128.253.172"
PORT = 8081

# ---Step 1: Creating the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# ---Step 2: Bind the socket to the server's IP and PORT
ls.bind((IP, PORT))



# ---Step 3: Convert into a listening socket
ls.listen()

number_connections = 0

print("Server is configured")

while True:

    print("Waiting for Clients to connect")

    try:
        # ---Step 4: Wait for client to connect
        (cs, client_ip_port) = ls.accept()

    except KeyboardInterrupt:
        print("Server is done!")
        ls.close()
        exit()

    else:
        number_connections =+ 1
        print(f"CONNECTION {number_connections}. Client IP,PORT: {client_ip_port}  ")
        # --- Step 5: Receiving information from the client
        msg_raw = cs.recv(2000)
        msg = msg_raw.decode()

        print(f"Received message: {msg}")

        # --- Step 6: Send a response message to the client
        response = f"ECHO {msg}\n"
        cs.send(response.encode())

        cs.close()