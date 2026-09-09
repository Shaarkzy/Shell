# Shark Shell

🐚 Shell Like Simulator With Linux Extension Toolkit
⚙️ Run Setup for libary installations and binary setup.
🐧 Software built for Linux.

**▶️ Run:**

```$ ./setup.sh ``` 

To build and configure program (Android [Termux-only] | Debian based system only).

**📁 Program File Structure (Architecture)**
```
    Shell
    |
    ├── Boot
    │   ├── update.sh
    │   └── util_boot.py
    ├── Core
    │   ├── relink
    │   └── shell.py
    ├── Data
    │   ├── config.json
    │   ├── logs
    │   ├── ports
    │   ├── shell_help
    │   ├── shellrc
    │   └── __version__
    ├── Features
    │   ├── ip_calculator.py
    │   ├── obfuscate.py
    │   ├── resistor.py
    │   ├── scanner.py
    │   └── site_check.py
    ├── launcher.py
    ├── LICENSE
    ├── README.md
    ├── Setup
    │   ├── android_setup.sh
    │   ├── debian_setup.sh
    │   ├── pycryptodome.sh
    │   └── setup.sh
    └── Utils
        ├── alias.py
        ├── fix.sh
        └── version.py
```

**📌 Note:**
```
1. 📂 Program Folder must be in the home directory (~/Shell , /root/Shell)

2. 💻 On Debian system, setup script must run as root as it calls (apt-get) command

3. 🔗 Run: $ bash /.../Shell/Core/relink on (root, non-root terminal) to link [launcher.py, shell] so you can start the program by calling [~$ shell] -> debian only.

4. 🚀 On Debian system, To start shell on Non root Terminal run: sudo shell.

5. ⚙️ Setup File is configured for Non-root Android Termux and Debian based systems only

6. 🛠️ Each update may require system-level fixes. The script fix.sh is executed automatically with every update.
--------fix.sh runs every time, regardless of whether fixes are needed.
--------If no fixes are required, fix.sh remains empty.
--------If fixes are necessary, fix.sh contains the relevant commands.
--------The script contents are shown to the user before execution.
------- The user can then choose whether to run it immediately or execute it later manually.
```

**📚 List Of Libraries Required**
```
1. 🎨 colorama
2. 🔤 regex
3. 📊 tqdm
4. 📁 xdg
5. 🌐 requests
6. 🛜 netifaces
7. 📱 phonenumbers
8. 🔐 pycryptodome
9. ⌨️ prompt_toolkit
10.📄 Beautiful Soup

Note: install libraries that failed to install.
    : Use (pip or building from source)
```

**✨ Features:**
```
1. 🔧 Binary Tools
2. 🔍 Port Scanner (multi/single) : (Aggresive) (Conservative)
3. 📂 File Management (Supports Cryptography)
4. 💬 Wifi Chat Room
5. 📤 File Transfer Via Wifi
6. 🖥️ Shell Host/Client
7. 🌤️ Weather Tools
8. 🌐 Network Information
9. 📱 Mobile Number Osint(excluding personal information)
10. 🏠 Grab Website Ip
11. 📍 Gather Information About An Ip Address.
12. 🔎 File Searching
13. 👁️ File and Folder Properties Viewer
14. 🔗 Clone Aliases
15. ✅ Site Up & Down Checker
16. 🖧 IP CALCULATOR
17. 📇 PYTHON FILE OBFUSCATOR
```

**🍀 Good luck**