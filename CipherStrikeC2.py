# ----- License -------------------------------------------------- # 

#  CipherStrike - CipherStrike simulates ransomware attacks to test EDR systems, enabling users to strengthen their defense strategies.
#  Copyright (c) 2025 - Steven Pereira aka Cursed.

#  This software is an open-source cybersecurity tool developed for
#  penetration testing, threat modeling, and security research. It   
#  is licensed under the MIT License, allowing free use, modification, 
#  and distribution under the following conditions:
#
#  You MUST include this copyright notice in all copies.
#  You MAY use this software for personal or educational purposes ONLY.
#  This software is provided "AS IS," WITHOUT WARRANTY of any kind. 
#  You MAY NOT use this software for any illegal or unauthorized activity.

#  DISCLAIMER:
#  This tool is intended for **educational or ethical testing** purposes only.
#  Unauthorized or malicious use of this software against systems without 
#  proper authorization is strictly prohibited and may violate laws and regulations.
#  The author assumes no liability for misuse or damage caused by this tool.

#  🔗 License: MIT License
#  🔗 Repository: https://github.com/Cursed271
#  🔗 Author: Steven Pereira (@Cursed271)

# ----- Libraries ------------------------------------------------ #

import os
import socket
from datetime import datetime
from rich.console import Console

# ----- Global Declaration --------------------------------------- #

port = 2701
host = "127.0.0.1"
console = Console()

# ----- C2 Server Initiation ------------------------------------- #

def c2_server():
	console.print(f"[red][+] CipherStrike C2 Server Started - Listening for CipherStrike Victims.....")
	try:
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
			server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			server.bind((host, port))
			server.listen()
			console.print(f"[#C6ECE3][*] Listening on {host}:{port}.....")
			while True:
				client, addr = server.accept()
				console.print(f"[green][+] Connection from {addr[0]}:{addr[1]}")
				with client:
					while True:
						data = client.recv(1024)
						if not data:
							break
						timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
						decoded = data.decode(errors='ignore').strip()
						console.print(f"[#C6ECE3][{timestamp}] [>] Exfiltrated: {decoded}")
	except KeyboardInterrupt:
		console.print("[red][!] Ctrl+C detected. Shutting down C2 server...")
	except Exception as e:
		console.print(f"[red][!] Error: {e}")
	finally:
		console.print("[#C6ECE3][*] Server stopped.")

# ----- Banner --------------------------------------------------- #

def ascii():
	console.print(rf"""[#C6ECE3]
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                                                                                                             │
│      .oooooo.    o8o             oooo                            .oooooo..o     .             o8o  oooo                     │ 
│     d8P'  `Y8b   `"'             `888                           d8P'    `Y8   .o8             `"'  `888                     │ 
│    888          oooo  oo.ooooo.   888 .oo.    .ooooo.  oooo d8b Y88bo.      .o888oo oooo d8b oooo   888  oooo   .ooooo.     │ 
│    888          `888   888' `88b  888P"Y88b  d88' `88b `888""8P  `"Y8888o.    888   `888""8P `888   888 .8P'   d88' `88b    │ 
│    888           888   888   888  888   888  888ooo888  888          `"Y88b   888    888      888   888888.    888ooo888    │ 
│    `88b    ooo   888   888   888  888   888  888    .o  888     oo     .d8P   888 .  888      888   888 `88b.  888    .o    │ 
│     `Y8bood8P'  o888o  888bod8P' o888o o888o `Y8bod8P' d888b    8""88888P'    "888" d888b    o888o o888o o888o `Y8bod8P'    │
│                        888                                                                                                  │
│                       o888o                                                                                                 │
│                                                                                                                             │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
	""")
	console.print(rf"[#C6ECE3]+--------------------------------------------------------------+")
	console.print(rf"[#C6ECE3]  CipherStrike - Test Defenses. Simulate Threats. Strike Silently.")
	console.print(rf"[#C6ECE3]  Created by [bold black]Cursed271")
	console.print(rf"[#C6ECE3]+--------------------------------------------------------------+")

# ----- Main Function -------------------------------------------- #

if __name__ == "__main__":
	os.system("cls" if os.name == "nt" else "clear")
	ascii()
	c2_server()
	console.print("[#C6ECE3]+--------------------------------------------------------------+")

# ----- End ------------------------------------------------------ #
