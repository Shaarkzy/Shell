
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


def compare_line(line, home):
    compute = line.split("=", 1)
    check_line_a = compute[0].split()[1]
    check_line_b = compute[1]

    check_line = check_line_a+"="+check_line_b
    check_line = check_line.replace("'", "").replace('"', '')

    shell_alias_file = f"{home}/Shell/UTILS/.shellrc"
    file = open(shell_alias_file, 'r')
    data = file.readlines()
    length = len(data)
    file.close()
    
    try:
        num = 0
        for i in range(length):
            num += 1
            if check_line.strip() == data[num].strip():
                return True
        return False
    except:
        return False



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
        if data.startswith('alias'): 
            if not compare_line(data, home): #function to compare if an alias already exists in the .shellrc file
                #alias ii="pkg update && pkg upgrade"
                split_line = data.split("=", 1)
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
#end line 120