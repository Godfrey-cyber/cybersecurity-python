## Python is widely used in cybersecurity due to its versatility, ease of use, and a variety of libraries that help with tasks such as penetration testing, vulnerability scanning, malware analysis, and network security.

## In this project we are going to explore some of the ways python can be explited in the filed of cyber Security

## Port Scaning 
	- A port scanner can be used to detect open ports on a target machine.
	- This script connects to each port in the range 1-1024 on the given host and checks if the port is open. It uses socket.connect_ex to try and connect to the port and checks if the connection was successful.

## Password Cracking (Brute Force)
	- A basic example of using Python to brute-force a password by trying common passwords (like in a dictionary attack):
	- This script performs a simple brute-force attack by iterating through a password dictionary file (password_file) and trying each password against a login form. It checks if the response contains "Login successful". This is a simple form of credential stuffing.

## Network Sniffing (Packet Capture)
	- This script uses the scapy library to sniff network packets on your local machine. It captures network packets and displays their details using the packet.show() method.
## Simple Keylogger
	- A keylogger records all the keystrokes on the keyboard and saves them to a file.
	- This keylogger records all keystrokes (including special keys) and saves them to a text file (keystrokes.txt). It uses the pynput library to listen for key presses and releases.

## Malware Analysis (Detecting Obfuscated Code)
	- This simple Python script can be used to detect obfuscated code by analyzing suspicious patterns like repeated function calls, eval functions, or base64 encoded data.
	- This script checks a given script for common obfuscation patterns such as eval(), setInterval(), and base64 decoding. It uses regular expressions to search for these patterns, which are often used in malicious scripts.

##                           ------------------  THE END  ----------------------------