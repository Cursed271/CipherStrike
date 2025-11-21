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
import random
from faker import Faker
from rich.console import Console

# ----- Global Declaration --------------------------------------- #

fake = Faker()
file_count = 1000
console = Console()
target_folder = "Important Data"
os.makedirs(target_folder, exist_ok=True)

# ----- Generate PAN Card ---------------------------------------- #

def generate_pan_card():
	return fake.random_uppercase_letter() + \
			''.join(fake.random_letters(length=4)).upper() + \
			str(random.randint(1000, 9999)) + \
			fake.random_uppercase_letter()

# ----- Generate File Content ------------------------------------ #

def generate_file_content():
	address = fake.address().replace("\n", ", ")
	return f"""
# ----- Personal Information ------------------------------ #
Full Name: {fake.name()}
Date of Birth: {fake.date_of_birth()}
Gender: {random.choice(['Male', 'Female', 'Other'])}
Nationality: {random.choice(['Indian', 'American', 'Australian', 'Nigerian', 'British', 'South African'])}

# ----- Contact Information ------------------------------- #
Phone Number: {fake.phone_number()}
Email Address: {fake.email()}
Address: {address}

# ----- Government ID Information ------------------------- #
Aadhaar Number: {random.randint(1000, 9999)} {random.randint(1000, 9999)} {random.randint(1000, 9999)}
PAN Card Number: {generate_pan_card()}
Passport Number: {fake.bothify(text='??#######').upper()}
Voter ID: {fake.bothify(text='???######').upper()}
Driving License: DL-{random.randint(1000,9999)}{random.randint(1000000,9999999)}
SSN (US): {fake.ssn()}
Medicare Number (AU): {random.randint(1000, 9999)} {random.randint(10000, 99999)} {random.randint(0,9)}
NIN (UK): QQ{random.randint(100000, 999999)}C
South Africa ID: {fake.msisdn()[:13]}
Nigerian NIN: {random.randint(10000000000, 99999999999)}

# ----- Financial Information ----------------------------- #
Bank Account Number: {random.randint(100000000000, 999999999999)}
IFSC Code: HDFC{random.randint(1000, 9999)}
Credit Card Number: 4111 1111 1111 1111
CVV: {random.randint(100, 999)}
Expiry Date: 12/{random.randint(25, 29)}
UPI ID: {fake.first_name().lower()}{random.randint(10,99)}@hdfcbank

# ----- Login Information --------------------------------- #
Username: {fake.user_name()}
Password: {fake.password(length=12, special_chars=True)}
Security Question: First pet's name?
Security Answer: {fake.first_name()}

# ----- Medical Information ------------------------------- #
Blood Group: {random.choice(['A+', 'B+', 'AB+', 'O+', 'A-', 'B-', 'AB-', 'O-'])}
Health Insurance Number: HIN-{random.randint(100000, 999999)}
Allergies: {random.choice(['None', 'Penicillin', 'Dust', 'Peanuts', 'Gluten'])}

# ----- Technology Information ---------------------------- #
IP Address: {fake.ipv4()}
MAC Address: {fake.mac_address()}
IMEI Number: {random.randint(100000000000000, 999999999999999)}
Browser Fingerprint: bfp_{fake.sha1()[:16]}

# ----- Employment Information ---------------------------- #
Employee ID: EMP{random.randint(100000, 999999)}
Designation: {fake.job()}
Company: {fake.company()}

# ----- Education Information ----------------------------- #
University: {fake.company()} Institute of Technology
Degree: {random.choice(['B.Tech', 'B.Sc', 'M.Tech', 'M.Sc'])} in {fake.job().split()[0]}
Graduation Year: {random.randint(2010, 2022)}
Student ID: {fake.bothify(text='UNI#######')}

# ----- Sensitive Information ----------------------------- #
Religion: {random.choice(['Hindu', 'Christian', 'Muslim', 'Jewish', 'Buddhist'])}
Marital Status: {random.choice(['Single', 'Married', 'Divorced'])}
Sexual Orientation: {random.choice(['Straight', 'Gay', 'Bisexual', 'Prefer not to say'])}
Political Affiliation: {random.choice(['Independent', 'Democrat', 'Republican', 'Other', 'Undisclosed'])}

# ----- End of File --------------------------------------- #
"""

# ----- Create Files --------------------------------------------- #

def create_files():
	console.print(rf"[green][+] Creating {file_count} fake PII files in '{target_folder}'.....")
	for i in range(1, file_count + 1):  # <--- fixed this line!
		file_path = os.path.join(target_folder, f"Important_{i:04}.txt")
		with open(file_path, 'w', encoding='utf-8') as f:
			f.write(generate_file_content())
	console.print(rf"[green][+] All fake data files have been created successfully.")

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
	create_files()
	console.print("[#C6ECE3]+--------------------------------------------------------------+")

# ----- End ------------------------------------------------------ #
