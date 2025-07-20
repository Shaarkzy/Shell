#------------------------------------------------------------------------------------------------------------------------------
#imports
try:
    import subprocess as sub
    from ..version import check
    from ..check_os import detect_os
    import os
    import shutil
    import time as tm
    from os import system as sys
    import subprocess as sub
    from colorama import Fore
except:
    pass
    quit(0)


#------------------------------------------------------------------------------------------------------------------------------


#detect operating system
if detect_os() == True or detect_os() == False:
    pass
else:
    print(Fore.RED+"[x]Possible Error: Unsupported OS or Corrupted Shell Folder [exit folder now]")
    quit(0)

#------------------------------------------------------------------------------------------------------------------------------
#software update trigger 
def trigger_software_update():
    check_res = check()

    if check_res != False and check_res != "null_internet":
        #software update function
        option = input(f"{Fore.YELLOW}[?]NEW UPDATE [{check_res}] AVAILABLE WISH TO UPDATE [y/n] "+Fore.WHITE).lower().strip()
        if option == "y":
            software_update()
            return ""
        else:
            return f"{Fore.CYAN}[*]Update Quited"

    elif check_res == False:
        return f"{Fore.CYAN}[*]Software Up To Date"

    elif check_res == 'null_internet':
        return f"{Fore.RED}[x]No Internet Connection"


#------------------------------------------------------------------------------------------------------------------------------

def software_update():
    #detect os
    if detect_os():
        folder = '/data/data/com.termux/files/home/'
    else:
        user = sub.getoutput('whoami')
        folder = "/root/" if os.geteuid() == 0 else f'/home/{user}/'

    form = f'{folder}Shell'

    #quit update if user in shell directory
    if form in sub.getoutput("pwd"):
        print(Fore.RED+"[x]POTENTIAL ERROR: WON'T RUN UPDATE ON SHELL SOFTWARE FOLDER")
        tm.sleep(4)

    #run update script
    else:
        sys("./Shell/UTILS/BOOT_SETUP/update.sh")
        tm.sleep(4)



#------------------------------------------------------------------------------------------------------------------------------

def load_libraries():
    print(Fore.GREEN+"[*]LOADING LIBRARIES......"+Fore.BLUE)
    global sy, F, B, Sty, tm, socket, sub, rd, exists, os, re, uuid
    global ipaddress, r, json, tqdm, pt, p, phone, carrier, geocoder
    global timezone, AES, get_random_bytes, mimetypes
    global datetime, glob, sys, ifaddresses, interfaces
    global AF_INET, AF_INET6, n, readline, at

    import sys as sy
    print("━"*2+" •", end="\r", flush=True)

    from colorama import Fore as F, Back as B, Style as Sty
    print("━"*4+" •", end="\r", flush=True)

    import time as tm
    print("━"*6+" •", end="\r", flush=True)

    import socket
    print("━"*8+" •", end="\r", flush=True)

    import subprocess as sub
    print("━"*10+" •", end="\r", flush=True)

    import random as rd
    print("━"*12+" •", end="\r", flush=True)

    from os.path import exists
    print("━"*14+" •", end="\r", flush=True)

    import os
    print("━"*16+" •", end="\r", flush=True)

    import re
    print("━"*18+" •", end="\r", flush=True)

    import uuid
    print("━"*20+" •", end="\r", flush=True)

    import ipaddress
    print("━"*22+" •", end="\r", flush=True)

    import requests as r
    print("━"*24+" •", end="\r", flush=True)

    import json
    print("━"*26+" •", end="\r", flush=True)

    from tqdm import tqdm
    print("━"*28+" •", end="\r", flush=True)

    import platform as pt
    print("━"*30+" •", end="\r", flush=True)

    import psutil as p
    print("━"*32+" •", end="\r", flush=True)

    import phonenumbers as phone
    print("━"*34+" •", end="\r", flush=True)

    from phonenumbers import carrier, geocoder, timezone
    print("━"*36+" •", end="\r", flush=True)

    from Crypto.Cipher import AES
    print("━"*38+" •", end="\r", flush=True)

    from Crypto.Random import get_random_bytes
    print("━"*40+" •", end="\r", flush=True)

    from netifaces import interfaces, ifaddresses, AF_INET, AF_INET6
    import netifaces as n
    print("━"*42+" •", end="\r", flush=True)

    import mimetypes
    print("━"*44+" •", end="\r", flush=True)

    from datetime import datetime
    print("━"*46+" •", end="\r", flush=True)

    import glob
    print("━"*48+" •", end="\r", flush=True)
    
    from os import system as sys
    print("━"*50+" •", end="\r", flush=True)
    
    import readline
    print("━"*52+" •", end="\r", flush=True)
    
    import atexit as at
    print("━"*54+" •", end="\r", flush=True)
 

#------------------------------------------------------------------------------------------------------------------------------


__all__ = [
    "sy", "F", "B", "Sty", "tm", "socket", "sub", "rd", "exists", "os", "re", "uuid",
    "ipaddress", "r", "json", "tqdm", "pt", "p", "phone", "carrier", "geocoder", 
    "timezone", "AES", "get_random_bytes", "interfaces", "ifaddresses", "AF_INET", "AF_INET6", "mimetypes", "datetime", "glob", "sys", "n", "readline", "at"
]
try:
    trigger_software_update()
    load_libraries()
except Exception as er:
    print(Fore.RED+"[x]",er)
    quit(0)
except KeyboardInterrupt:
    quit(0)


#------------------------------------------------------------------------------------------------------------------------------
#end line 184
