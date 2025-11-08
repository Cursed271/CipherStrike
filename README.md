<div align="center">

  <p align="center"><img src="https://github.com/Cursed271/Cursed271/blob/main/Logo.png" width="30%"></a></p>
  <h1>CipherStrike</h1>
  
  <p>
    CipherStrike simulates ransomware behavior, testing EDR defenses by encrypting files, exfiltrating data, and more.
  </p>
  
  <h4>
    <a href="https://github.com/Cursed271/CipherStrike/issues/new?labels=bug&template=bug_report.md">Report Bug</a>
  <span> · </span>
    <a href="https://github.com/Cursed271/CipherStrike/issues/new?labels=enhancement&template=feature_request.md">Request Feature</a>
  </h4>

</div>

## 📖 Table of Contents

- [Introduction](#-introduction)
- [Features](#-features)
- [Installation and Usage](#%EF%B8%8F-installation-and-usage)
- [Feedback](#-feedback)
- [Contributors](#-contributors)
- [License](#-license)

## 🚀 Introduction

CipherStrike is a Python-based ransomware simulation tool designed to test endpoint detection and response (EDR) systems. It mimics a real-world ransomware attack, encrypting files, exfiltrating data, and providing decryption functionality. A command-and-control (C2) server is included for victim communication, enabling testing and strengthening of cybersecurity defenses.

<p align="center">
  <h4>CipherStrike Ransomware</h4>
  <img src = "https://github.com/Cursed271/CipherStrike/blob/main/CipherStrike.png">
</p>

<p align="center">
  <h4>CipherStrike C2 Server</h4>
  <img src = "https://github.com/Cursed271/CipherStrike/blob/main/CipherStrikeC2.png">
</p>

<p align="center">
  <h4>CipherStrike PII Generator</h4>
  <img src = "https://github.com/Cursed271/CipherStrike/blob/main/CipherStrikePII.png">
</p>

## ✨ Features:

- 🛡️ Simulates Ransomware Attacks: Encrypts files and mimics real-world ransomware behavior.

- 💻 Command-and-Control (C2) Server: Allows communication between attacker and infected systems.

- 🔐 File Encryption: Uses AES encryption to secure victim data.

- 💾 Data Exfiltration: Sends encrypted data to a C2 server for testing exfiltration detection.

- 📝 Ransom Note: Generates a ransom note for victim systems to simulate a full attack scenario.

## ⚙️ Installation and Usage:

1. **Pre-requisites**: Ensure you have Python3 installed on your system.
2. **Clone the Repo**: Use "***git clone https://github.com/Cursed271/CipherStrike***"
3. **Traverse into the Directory**: Use "***cd CipherStrike***"
4. **Install Dependencies**: Use "***pip3 install -r requirements.txt***"
5. **Execute the PII Generator Script**: Use "***python3 CipherStrikePII.py***"
6. **Execute the C2 Server Script**: Use "***python3 CipherStrikeC2.py***"
7. **Execute the Ransomware Script**: Use "***python3 CipherStrike.py***"
8. **Choose the Ransomware Mode: Encryption, Decryption or C2 Simulation**

## 💬 Feedback  

Have suggestions or feature requests? Feel free to reach out via:  

- 🐦 **Twitter**: [@Cursed271](https://x.com/Cursed271)  
- 🐙 **GitHub**: [@Cursed271](https://github.com/Cursed271)  
- 🔗 **LinkedIn**: [Steven Pereira](https://www.linkedin.com/in/Cursed271/)  
- 📧 **Email**: [cursed.pereira@proton.me](mailto:cursed.pereira@proton.me)  
- 🐞 **File an Issue**: [GitHub Issues](https://github.com/Cursed271/CipherStrike/issues)  
- 💡 **Request a Feature**: [Feature Requests](https://github.com/Cursed271/CipherStrike/issues/new?labels=enhancement&template=feature_request.md) 

Your feedback helps improve CipherStrike! Contributions and PRs are always welcome. 🚀

## 🙌 Contributors

- **Steven Pereira (aka Cursed)** - Creator & Maintainer  

## 📜 License - CURSEDSEC OWNERSHIP EDICT

CipherStrike is licensed under the **COE or CursedSec Ownership Edict License**.

**This software is proprietary intellectual property owned exclusively by CursedSec.**

Unauthorized redistribution, modification, and re-uploading to any other repository (public or private) are strictly forbidden and constitute a direct violation of the **CursedSec Ownership Edict (COE)**.

**Consider this a warning: I track every copy. Get your own ideas, you lazy little shits.**

Violators will face immediate legal action and DMCA takedown requests. All development must be conducted via approved Pull Requests on this official repository.
