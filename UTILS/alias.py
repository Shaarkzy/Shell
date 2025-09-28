
#------------------------------------------------------------------------------------------------------------------------------


from os import system
import subprocess as sub
import os



#------------------------------------------------------------------------------------------------------------------------------



def load_file():
    home = os.environ["HOME"]
    file = f"{home}/Shell/UTILS/.shellrc"

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

    home = os.environ["HOME"]
    detect_shell = os.environ.get("SHELL", "/bin/bash").split("/")[-1]
    shell = ".zshrc" if detect_shell == "zsh" else ".bashrc"
    bash_alias_file = f"{home}/{shell}"
    shell_alias_file = f"{home}/Shell/UTILS/.shellrc"


    open_file = open(bash_alias_file, "r")
    read_file = open_file.readlines()
    length = len(read_file)
    open_file.close()

    open_file = open(shell_alias_file, "a")


    num = 0
    memory = {}
    for i in range(length):
        data = read_file[num].strip()
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
                open_file.write(construct+"\n")
            else:
                memory.update({key: value})

    open_file.close()
    return memory


#------------------------------------------------------------------------------------------------------------------------------
#end line 95







        







