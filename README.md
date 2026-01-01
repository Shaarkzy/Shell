# Shark Shell

Shell like emulator with extra utilities
Run Setup for libary installations and binary setup.
Program only for Linux.

**Run:**

```$ ./setup.sh ``` 

to build and configure program (Android | Debian based system only).

**Program File Structure (Architecture)**
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
│   ├── .config.json
│   ├── site_check.py
│   └── version.py
├── __version__
├── relink
├── setup.sh
└── shell.py

```

**Note:**
```
1. Some utilities requires superuser privilege (on feature 9)...
2. For Debian installation run setup as root: $ sudo ./setup.sh
3. Program Folder must be in the home directory (~/Shell , /root/Shell)
4. On Debian system, it's advisable to run setup on Non root Terminal
5. Run: $ ./relink on Non root terminal if setup was run on Root Terminal and you wish to run shell command from Non root terminal.
6. On Debian system, To start shell on Non root Terminal run: sudo shell.
7. Setup File is configured for Android and Debian based systems only
```

**List Of Libraries Required**
```
1. colorama
2. regex
3. tqdm
4. xdg
5. uuid
6. ipaddress
7. requests
8. psutil
9. netifaces
10. phonenumbers
11. pycryptodome
12. prompt_toolkit
13. bs4
```

**Features:**
```
1. Binary Tools
2. Port Scanner(multi/single)
3. File Management (Supports Cryptography)
4. Wifi Chat Room
5. File Transfer Via Wifi
6. Shell Host/Client
7. Weather Tools
8. Network Information
9. Cpu Information (might work without root access on earlier Android versions)
10. Mobile Number Osint(excluding personal information)
11. Grab Website Ip
12. Gather Information About An Ip Address.
13. File Searching
14. File and Folder Properties Viewer
15. Clone Aliases
16. Site Up&Down Checker
```

**Good luck**
