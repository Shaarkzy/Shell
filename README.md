# Shark Shell

<<<<<<< HEAD
🐚 Shell like emulator with extra utilities
⚙️ Run Setup for libary installations and binary setup.
🐧 Program only for Linux.
=======
🐚 Shell Like Simulator With Linux Extension Toolkit
⚙️ Run Setup for libary installations and binary setup.
🐧 Software built for Linux.
>>>>>>> origin/main

**▶️ Run:**

```$ ./setup.sh ``` 

to build and configure program (Android | Debian based system only).

**📁 Program File Structure (Architecture)**
<<<<<<< HEAD
```Shell/
├── LICENSE
├── README.md
├── UTILS
│   ├── BOOT_SETUP
│   │   ├── pycryptodome.sh
│   │   ├── update.sh
│   │   └── util_boot.py
│   ├── alias.py
│   ├── android_setup.sh
│   ├── debian_setup.sh
│   ├── resistor.py
│   ├── scanner.py
│   ├── .shellrc
│   ├── .shell_help
│   ├── .port
|   ├── .logs
│   ├── .config.json
│   ├── site_check.py
│   └── version.py
├── __version__
├── relink
├── setup.sh
└── shell.py

=======
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
>>>>>>> origin/main
```

**📌 Note:**
```
<<<<<<< HEAD
1. ⚠️ Some utilities requires superuser privilege (on feature 9)...
2. 🐧 For Debian installation run setup as root: $ sudo ./setup.sh
3. 📂 Program Folder must be in the home directory (~/Shell , /root/Shell)
4. 💻 On Debian system, it's advisable to run setup on Non root Terminal
5. 🔗 Run: $ ./relink on Non root terminal if setup was run on Root Terminal and you wish to run shell command from Non root terminal.
6. 🚀 On Debian system, To start shell on Non root Terminal run: sudo shell.
7. ⚙️ Setup File is configured for Android and Debian based systems only
=======
1. 🐧 For Debian installation run setup as root: $ sudo ./setup.sh
2. 📂 Program Folder must be in the home directory (~/Shell , /root/Shell)
3. 💻 On Debian system, it's advisable to run setup on Non root Terminal
4. 🔗 Run: $ sh Core/relink on Non root terminal if setup was run on Root Terminal and you wish to run shell command from Non root terminal.
5. 🚀 On Debian system, To start shell on Non root Terminal run: sudo shell.
6. ⚙️ Setup File is configured for Android and Debian based systems only
7. 🛠️ Each update may require system-level fixes. The script fix.sh is executed automatically with every update.
--------fix.sh runs every time, regardless of whether fixes are needed.
--------If no fixes are required, fix.sh remains empty.
--------If fixes are necessary, fix.sh contains the relevant commands.
--------The script contents are shown to the user before execution.
------- The user can then choose whether to run it immediately or execute it later manually.
>>>>>>> origin/main
```

**📚 List Of Libraries Required**
```
1. 🎨 colorama
2. 🔤 regex
3. 📊 tqdm
4. 📁 xdg
<<<<<<< HEAD
5. 🆔 uuid
6. 🔢 ipaddress
7. 🌐 requests
8. 💾 psutil
9. 🛜 netifaces
10. 📱 phonenumbers
11. 🔐 pycryptodome
12. ⌨️ prompt_toolkit
13. 📄 bs4
=======
5. 🌐 requests
6. 🛜 netifaces
7. 📱 phonenumbers
8. 🔐 pycryptodome
9. ⌨️ prompt_toolkit
10.📄 Beautiful Soup
>>>>>>> origin/main
```

**✨ Features:**
```
1. 🔧 Binary Tools
2. 🔍 Port Scanner(multi/single)
3. 📂 File Management (Supports Cryptography)
4. 💬 Wifi Chat Room
5. 📤 File Transfer Via Wifi
6. 🖥️ Shell Host/Client
7. 🌤️ Weather Tools
8. 🌐 Network Information
<<<<<<< HEAD
9. ⚡ Cpu Information (might work without root access on earlier Android versions)
10. 📱 Mobile Number Osint(excluding personal information)
11. 🏠 Grab Website Ip
12. 📍 Gather Information About An Ip Address.
13. 🔎 File Searching
14. 👁️ File and Folder Properties Viewer
15. 🔗 Clone Aliases
16. ✅ Site Up&Down Checker
```

**🍀 Good luck**
=======
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
>>>>>>> origin/main
