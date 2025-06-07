# Shark Shell

Shell like emulator with utilities
Run Setup for libary installations and binary setup.
Program only for Linux.

**Run:**

```$ ./setup.sh ``` 

to build and configure program

**Program File Structure (Architecture)**
```Shell/
├── LICENSE
├── README.md
├── setup.sh
├── shell.py
├── __version__
├── relink
├── UTILS/
│   ├── android_setup.sh
│   ├── kali_setup.sh
│   ├── .shell_history
│   ├── .shell_help
│   ├── check_os.py
│   ├── version.py
│   ├── resistor.py
│   ├── __pycache__
│   │       ├── check_os.cpython-312.pyc
│   │       └── version.cpython-312.pyc
│   └── BOOT_SETUP/
│       ├── util_boot.py
│       ├── pycryptodome.sh
│       ├── update.sh
│       └── __pycache__
│           └── util_boot.cpython-312.pyc
│       

```

**Note:**
```
1. Tested under Kali LInux Os and Android OS (Configured For Termux Terminal Only)
2. Some utilities requires superuser privilege (on feature 10)...
3. For kali installation run setup as root: $ sudo ./setup.sh
4. Program Folder must be in the home directory (~/Shell , /root/Shell)
5. On Kali, it's advisable to run setup on Non root Terminal, Run: $ ./relink on Non root terminal if setup was run on Root Terminal and you wish to run shell command from Non root terminal.
6. On kali, To start shell on Non root Terminal run: sudo shell.
7. On kali, the program runs on root environment.
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
```

# Program Executable

**Program File Structure (Architecture)**

```Shell/                                                       ├── LICENSE                                                     ├── README.md                                                   ├── UTILS
│   ├── BOOT_SETUP
│   │   └── update.sh                                           │   ├── android_setup.sh                                        │   └── kali_setup.sh
├── __version__
├── relink
├── setup.sh
├── shell_android
└── shell_kali                                                  
```    
**Link To Software**
https://www.dropbox.com/scl/fi/8tlky09l7rvdwymfzbiel/shell_exec.tar.gz?rlkey=rqlheo4xbyzom4e5x7z5oer35&st=ts1igrgd&dl=0 

# Security Check                                                
**Android Executable**: https://www.virustotal.com/gui/file/82453bf5a16da27eec3eb4be0b4fc8ad73213f77c54657770d83633bb4b04cda/detection                                                          
**Kali Executable**: https://www.virustotal.com/gui/file-analysis/OGUyYjA5ODI0MzQxMDFjMDI0MzkxMTNjYjVjZDU3NmM6MTc0OTEzMTY2OQ==/detection

**Good luck**
