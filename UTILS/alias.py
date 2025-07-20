
#------------------------------------------------------------------------------------------------------------------------------


from os import system
from .check_os import detect_os
import subprocess as sub
import os



#------------------------------------------------------------------------------------------------------------------------------



def load_file():
    if detect_os():
        file = "/data/data/com.termux/files/home/Shell/UTILS/.shellrc"
    else:
        user = sub.getoutput("whoami")
        file = "/root/Shell/UTILS/.shellrc" if os.geteuid() == 0 else f'/home/{user}/Shell/UTILS/.shellrc'

    open_file = open(file, "r")

    open_file_data = open_file.readlines()
    open_file.close()
    return open_file_data



#------------------------------------------------------------------------------------------------------------------------------



def compute():
    num = 0
    memory = {}
    length = len(load_file())
    for i in range(length):
        try:
            extract = load_file()[num]
            num += 1
            retrieve = extract.split("=")
            key = retrieve[0]
            value = retrieve[1]
            memory.update({key: value})
        except IndexError:
            continue

    return memory



#------------------------------------------------------------------------------------------------------------------------------




def clone_alias(mode):
    if detect_os():
        bash_alias_file = "/data/data/com.termux/files/home/.bashrc"
        shell_alias_file = "/data/data/com.termux/files/home/Shell/UTILS/.shellrc"

    else:
        detect_shell = os.environ.get("SHELL", "/bin/bash").split("/")[-1]
        shell = ".zshrc" if detect_shell == "zsh" else ".bashrc"
        user = sub.getoutput("whoami")
        bash_alias_file = f"/root/{shell}" if os.geteuid() == 0 else f'/home/{user}/{shell}'
        shell_alias_file = f"/root/Shell/UTILS/.shellrc" if os.geteuid() == 0 else f"/home/{user}/Shell/UTILS/.shellrc"


    open_file = open(bash_alias_file, "r")
    read_file = open_file.readlines()
    length = len(read_file)
    open_file.close()

    open_file = open(shell_alias_file, "a")


    num = 0
    memory = {}
    for i in range(length):
        data = read_file[num]
        num += 1
        if data.startswith("alias"):
            #alias ii="pkg update && pkg upgrade"
            split_line = data.split("=")
            key = split_line[0].split()[1]
            value = split_line[1]
            value = value.replace('"', '')
            value = value.replace("'", "")

            if mode:
                construct = key+"="+value
                open_file.write(construct)
            else:
                memory.update({key: value})

    open_file.close()
    return memory


#------------------------------------------------------------------------------------------------------------------------------
#end line 103







        







