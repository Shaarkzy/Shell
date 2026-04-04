#!/usr/bin/env python3

#-----------------------------------import all libraries-------------------------------------------------------------------------------

from UTILS.BOOT_SETUP.util_boot import *
from UTILS.BOOT_SETUP.util_boot import trigger_software_update
from UTILS.resistor import *
from UTILS.alias import *
from UTILS.scanner import *
from UTILS.site_check import *
from UTILS.ip_calculator import *

#---------------------------------clear screen after loading libraries---------------------------------------------------------------------

sys("clear")

#--------------------------------------------change username-------------------------------------------------------------------------------

home = os.environ["HOME"]
with open(f'{home}/Shell/UTILS/.config.json', 'r') as file:
    try:data = json.load(file);username = data["username"]
    except:print(f"{F.RED}[!]FILE CORRUPTED REDOWNLOAD THE PROGRAM WITH {F.WHITE}./setup.sh {F.RED}COMMAND");quit(0)
            
if username: pass
else:
    print(f"{F.GREEN}[!]SkIP {F.WHITE}[HIT ENTER KEY]{F.GREEN} IF YOU WISH TO CONTINUE WITH SYSTEM NAME\n{F.YELLOW}YOU CAN UPDATE NAME ANYTIME WITH {F.WHITE}@name <name> {F.YELLOW} COMMAND")
    username = input(f"{F.CYAN}[*]Username: {F.WHITE}").strip()
    if not username:username = sub.getoutput("whoami")
            
    data["username"] = username
    with open(f"{home}/Shell/UTILS/.config.json", "w") as file:json.dump(data, file, indent=4);pass
        
sys("clear")       
              
#---------------------------------------input function------------------------------------------------------------------------------

def inpu():
    #get working directories
    
    # wrapper to hide non printable characters in prompt for readline compatibility
    def c(x):
        return f"\001{x}\002"

    try:
        print("\n")
        #get username
        direc = os.getcwd()
        new_path = "/".join(direc.split(os.sep)[-3:])
        new_path = F.CYAN+new_path+F.YELLOW

        prompt = (
            f"{c(F.YELLOW)}╭─({c(F.CYAN)}{username}{c(F.YELLOW)}@{c(F.CYAN)}Shell{c(F.YELLOW)})"
            f"——[{new_path}]\n│\n"
            f"{c(F.YELLOW)}╰─{c(F.CYAN)}§ {c(F.WHITE)}"
        )

        data = input(prompt)
        if data:
            readline.add_history(data)
        return data
    except KeyboardInterrupt:
        print("")
        return 1
    
def background(): #future background process
    #do something, call something, solve something
    pass

#log silent messages
def log(data):
    home = os.environ['HOME']
    log_file = f'{home}/Shell/UTILS/.logs'
    now = datetime.now()
    time = now.strftime('%Y-%m-%d %H:%M:%S')
    collide = f'{data} @ {time}\n'

    with open(log_file, 'a') as file:
        file.write(collide)

#--------------------------------initialize the class-----------------------------------------------------------------------------

class shark:
    def __init__(self):
        self.soc = socket
        self.os = os
        self.count_f = 0
        self.count_s = 0
       
    # load the welcome screen on start
    def main(self):
        home = os.environ["HOME"]
        version = open(f"{home}/Shell/__version__", "r").read().strip()
        data = f"""
                {F.CYAN}  ╭────────────────────────╮
                • │ {F.YELLOW}WELCOME·TO·SHARK-SHELL{F.CYAN} |─╮
                ╰─│  {F.GREEN}For Help: Run {F.WHITE}@help{F.CYAN}   │ •
                  │   {F.CYAN}UTILITY PROGRAMS     │
                  ╰────────────────────────╯
                    """
        print (data)
        log("[INFO] main() displayed welcome screen")

#------------------------------------function for list of tools------------------------------------------------------------------------------------------
    
    def help(self): #1
        home = os.environ["HOME"]
        data = open(f"{home}/Shell/UTILS/.shell_help", "r").read()
        log("[INFO] help() called")
        print(eval(f"f'''{data}'''"))

#--------------------------------------getting ip address of a site----------------------------------------------------------------------------------------

    def get_ip(self, host): #2
        try:
            log(f"[INFO] get_ip() resolving host={host}")
            data = self.soc.gethostbyname(host)
            print (F.CYAN+f"[✓]{host}: {F.BLUE}{data}")
        except:
            print (F.RED+"[x]Error, Maybe Invalid Host Or No Internet Connection")

#-------------------------------------gather information about an ip address----------------------------------------------------------------------------------------

    def ip_osint(self, ip):
        try:
            log(f"[INFO] ip_osint() querying ip={ip}")
            res = r.get(f"https://ipinfo.io/{ip}", timeout=5)
            fetch = res.json()
            for i in fetch.keys():
                if i != "readme":
                    print(f"{F.CYAN}[*]{i}:-->{F.GREEN}{fetch[i]}")
                else:
                    continue
        except:
            print(F.RED+"[x]Error Connecting To Server")

#--------------------------------------converting binary to number----------------------------------------------------------------------------------------

    def Bina_Num(self, binary, base): #5
        log(f"[INFO] Bina_Num() converting binary={binary} base={base}")
        print (F.GREEN+"[%]Output"+F.BLUE)
        print (F.BLUE+str(int(binary, int(base))))

#---------------------------------converting number to binary---------------------------------------------------------------------------------------------

    def Num_Bina(self, num, base): #6
        num = int(num)
        base = int(base)
        log(f"[INFO] Num_Bina() converting num={num} base={base}")
        print (F.GREEN+"[*]Output"+F.BLUE)
        print (F.BLUE+bin(num) [base: ])

#----------------------------------------repair binary files with invalid byte--------------------------------------------------------------------------------------

    def repair(self, file):
        try:
            log(f"[INFO] repair() repairing file={file}")
            open_file = open(file, 'r')
            read_file = open_file.read()
            open_file.close()
            data = read_file

            for i in read_file:
                if i != '1' and i != '0' and i != ' ':
                    new = data.replace(i, '')
                    data =  new
            new_file = open(file, 'w')
            new_file.write(data)
            new_file.close()
            print(F.CYAN+'[✓]File Repaired')
        except:
            print(F.RED+"[x]Unsuccessful: File Corrupted")

#-----------------------------------convert alphabet to binary-------------------------------------------------------------------------------------------

    def Alpha_Bina(self, file):
        file = self.get_file(file)
        log(f"[INFO] Alpha_Bina() converting file={file}")
        open_file = open(file, "r")
        data = open_file.read()
        open_file.close()
        save_data = ' '.join(format(ord(c), '08b') for c in data)
        s_file = file+".sbin"
        open_file = open(s_file, "w")
        open_file.write(save_data)
        print(F.CYAN+"[*]File Converted Successfully")
        open_file.close()

#-------------------------------------convert binary to alphabet-----------------------------------------------------------------------------------------

    def Bina_Alpha(self, file):
        file = self.get_file(file)
        log(f"[INFO] Bina_Alpha() converting file={file}")
        open_file = open(file, "r")
        data = open_file.read()
        open_file.close()
        binary_values = data.split(' ')
        try:
            save_data = ''.join(chr(int(b, 2)) for b in binary_values)
            s_file = file+".stxt"
            open_file = open(s_file, "w")
            open_file.write(save_data)
            print(F.CYAN+"[*]File Converted Succesfully")
            open_file.close()
        except:
            print(F.RED+"[x]Invalid Bytes Detected: Cleaning File")
            self.repair(file)

#------------------------------------get private ip address of a device------------------------------------------------------------------------------------------

    def get_private_addr(self):
        log("[INFO] get_private_addr() called")
        interfaces = n.interfaces()
        ip_all = ""
        for interface in interfaces:
            try:
                addresses = n.ifaddresses(interface)
                if n.AF_INET in addresses:
                    for addr in addresses[n.AF_INET]:
                        ip = addr['addr']
                        if ip.startswith('10.') or ip.startswith('172.') or ip.startswith('192.168.') or ip.startswith('169.254.') or ip.startswith('127.') or ip.startswith('0.0.0.0'):
                            ip_all = ip_all + "[" + ip + "] "
    
            except ValueError:
                continue
        return ip_all

#-------------------------------------get device network details and interfaces-----------------------------------------------------------------------------------------

    def get_device_ip(self):
        try:
            log("[INFO] get_device_ip() querying public IP")
            response = r.get('https://api.ipify.org?format=json', timeout=2)
            ip_data = response.json()
            print(F.WHITE+"—"*62)
            print(F.CYAN+"[*]Interface: - Public Address -")
            print(F.WHITE+"-- addr: ",ip_data['ip'])
            print(F.WHITE+"—"*62)
        except r.RequestException:
            print(F.WHITE+"—"*62)
            print(F.CYAN+"[*]Interface: - Public Address -")
            print(F.WHITE+"-- addr: ", "Network Not Reachable")
            print(F.WHITE+"—"*62)
        for interface in interfaces():
            print(f"{F.CYAN}[*]Interface: - {interface} -")
            addrs = ifaddresses(interface)
            
            if AF_INET in addrs:
                for addr in addrs[AF_INET]:
                    print(f"{F.WHITE}–– IPv4 Address  : {addr.get('addr', 'N/A')}")
                    print(f"-- Netmask       : {addr.get('netmask', 'N/A')}")
                    print(f"-- Broadcast     : {addr.get('broadcast', 'N/A')}")
            else:
                print(f"{F.MAGENTA}  No IPv4 Address")
    

            if AF_INET6 in addrs:
                for addr in addrs[AF_INET6]:
                    print(f"{F.WHITE}–– IPv6 Address  : {addr.get('addr', 'N/A')}")
                    print(f"-- Netmask       : {addr.get('netmask', 'N/A')}")
                    print(f"-- Broadcast     : {addr.get('broadcast', 'N/A')}")
            else:
                print(f"{F.MAGENTA}  No IPv6 Address")
            print(F.WHITE+"—"*62)

#-----------------------------------crazy encode-------------------------------------------------------------------------------------------

    def rcode(self, data, mode):
        if mode:
            data_bytes = data.encode('utf-8')
            data_bytes = bs64.b64encode(data_bytes)
            data = data_bytes.decode('utf-8')
            return data
        else:
            data_bytes = data.encode('utf-8')
            data_bytes = bs64.b64decode(data_bytes)
            data = data_bytes.decode('utf-8')
            return data

#------------------------------------------------------------------------------------------------------------------------------------------

    def sock_(self, s, data, mode):
        if mode:
            data = self.rcode(data, True)
            length = len(data.encode())
            s.send(length.to_bytes(4, byteorder='big'))
            s.send(data.encode())
            return True
        else:
            length = int.from_bytes(s.recv(4), byteorder='big')
            data = self.rcode(s.recv(length).decode(), False)
            return data

#-----------------------------------open server for wifi chat room-------------------------------------------------------------------------------------------

    def open_server(self): #11
        print (F.CYAN+"[Note]: Only Support TCP")
        print(F.CYAN+"......: To Close Chat: @bye")

        a1, a2, a3 = str(rd.randint(1,6)), str(rd.randint(1,6)), str(rd.randint(1,5))
        ip = self.get_private_addr()
        port = a3+a2+a1+a2+a3
        print (F.BLUE+"[✓]Server Started")
        print (F.CYAN+"[*]Possible IP Address Listed Below")
        print (F.CYAN+f"[*]Ip: {F.YELLOW}{ip}{F.CYAN}[*]Port: {F.YELLOW}{port}")
        print(" ")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(500)
    
        sock.bind(("0.0.0.0", int(port)))
        sock.listen(5)
        log(f"[INFO] open_server started on {ip}:{port}")
        while True:
            c = None
            try:
                c, addr = sock.accept()
                auth_s = '0x1000'
                self.sock_(c, auth_s, True)
                auth_r = self.sock_(c, True, False)
                if not auth_r: c.close(); continue
                if auth_s == auth_r:
                    log(f"[INFO] open_server accepted connection from {addr}")
                    break
                else: c.close(); log('[x] Invalid Connection On Open Server Func'); continue
            except KeyboardInterrupt: return 0
            except ConnectionResetError: c.close; log('[x]Invalid Connection On Open Server Func'); continue
            except socket.timeout: print(F.RED+"[x]Timed Out"); return 0
            
        host_name = username
        
        client_name = self.sock_(c, True, False)
        log(f"[INFO] open_server session established host={host_name} client={client_name} from={addr}")
        self.sock_(c, host_name, True)
        flag = False
        session = PromptSession()

        def send_():
            nonlocal flag
            while True:
                with patch_stdout():
                    try:
                        sen = session.prompt(ANSI(f"{B.GREEN}{F.BLACK} {host_name} {Sty.RESET_ALL} {F.WHITE}"))
                        print("")
                        if sen:
                            self.sock_(c, sen, True)
                    except KeyboardInterrupt: pass
                    except: c.close(); break

                if sen.strip() == '@bye':
                    c.close()
                    flag = True
                    break

                if flag == True:
                    c.close()
                    break

        def recv_():
            nonlocal flag
            while True:
                try:
                    data = self.sock_(c, True, False)
                    if not data:
                        flag = True
                        c.close()
                        print_formatted_text(ANSI(f'{F.RED}[x]CLIENT DISCONNECTED HIT ENTER TO CLOSE SESSION'))
                        break
                except KeyboardInterrupt: pass
                except: c.close(); break

                if data.strip() == '@bye':
                    print_formatted_text(ANSI(f'{F.RED}[!]USER CLOSED CHAT HIT ENTER TO CLOSE SESSION\n'))
                    c.close()
                    flag = True
                    break

                if flag == True:
                    c.close()
                    break

                print_formatted_text(ANSI(f"{B.BLUE}{F.BLACK} {client_name} {Sty.RESET_ALL} {B.WHITE}{F.BLACK}{data}"))
                print("")


        send__ = threading.Thread(target=send_)
        recv__ = threading.Thread(target=recv_)

        send__.start()
        recv__.start()


        send__.join()
        recv__.join()
        print(F.RED+'[✓]SESSION CLOSED')
        log(f"[INFO] open_server session closed host={host_name} client={client_name}")

#-----------------------------------connect to wifi chat room server-------------------------------------------------------------------------------------------

    def connect_server(self, ip, port): #12
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        log(f"[INFO] connect_server attempting connection to {ip}:{port}")
        while True:
            sock.connect((ip, int(port)))
             
            auth_r = self.sock_(sock, True, False)
            auth_s = '0x1000'
            self.sock_(sock, auth_s, True)

            if auth_r == auth_s:
                print(F.CYAN+'[NOTE]: Only Support Wlan')
                print(F.CYAN+'......: To Close Chat: @bye')
                print(F.BLUE+"[✓]Connected To Server")
                log(f"[INFO] connect_server connected to {ip}:{port}")
                print(" ")
                break
            else: print(F.RED+'[x]Invalid Connection'); sock.close(); return 0
             
             
        client_name = username
        self.sock_(sock, client_name, True)
        host_name = self.sock_(sock, True, False)
        flag = False
        session = PromptSession()

        def recv_cs():
            nonlocal flag
            while True:
                try:
                    rec = self.sock_(sock, True, False)
                    if not rec:
                        flag = True
                        sock.close()
                        print_formatted_text(ANSI(f'{F.RED}[x]SERVER DISCONNECTED HIT ENTER TO CLOSE SESSION'))
                        break
                except KeyboardInterrupt: pass
                except: sock.close(); break

                if rec.strip() == '@bye':
                    print_formatted_text(ANSI(f'{F.RED}[!]USER CLOSE CHAT HIT ENTER TO CLOSE SESSION\n'))
                    sock.close()
                    flag = True
                    break

                if flag == True:
                    sock.close()
                    break

                print_formatted_text(ANSI(f"{B.BLUE}{F.BLACK} {host_name} {Sty.RESET_ALL} {B.WHITE}{F.BLACK}{rec}"))
                print("")


        def send_cs():
            nonlocal flag
            while True:
                with patch_stdout():
                    try:
                        sen = session.prompt(ANSI(f"{B.GREEN}{F.BLACK} {client_name} {Sty.RESET_ALL} {F.WHITE}"))
                        print("")
                        if sen:
                            self.sock_(sock, sen, True)
                    except KeyboardInterrupt: pass
                    except: sock.close(); break
 
                if sen.strip() == "@bye":
                    sock.close()
                    flag = True
                    break

                if flag == True:
                    sock.close()
                    break

        recv__cs = threading.Thread(target=recv_cs)
        send__cs = threading.Thread(target=send_cs)

        send__cs.start()
        recv__cs.start()

        send__cs.join()
        recv__cs.join()
        print(F.RED+'[✓]SESSION CLOSED')
                 
#---------------------------------generate key for encryption---------------------------------------------------------------------------------------------

    def key(self, num):
        log(f"[INFO] key() generating key of length={num}")
        data = str(uuid.uuid4()).replace(':', '')[:num].replace('-', 'f')
        log(f"[DEBUG] key() generated key={data}")
        return data

#-------------------------------------get file size and format-----------------------------------------------------------------------------------------

    def byte_size(self, size):
        file_size_bytes = size
        if file_size_bytes < 1024:
            file_size = f"{file_size_bytes} bytes"
        elif file_size_bytes < 1024 ** 2:
            file_size = f"{file_size_bytes / 1024:.2f} KB"
        elif file_size_bytes < 1024 ** 3:
            file_size = f"{file_size_bytes / (1024 ** 2):.2f} MB"
        else:
            file_size = f"{file_size_bytes / (1024 ** 3):.2f} GB"
        return file_size

#--------------------------------------glob for file search----------------------------------------------------------------------------------------

    def get_file(self, file):
        path = file
        matches = glob.glob(path)
        if matches:
            if len(matches) == 1:
                check = matches[0]
                log(f"[INFO] get_file resolved pattern {path} -> {check}")
                return check.replace("'", "")
            else:
                print(F.RED+"[x] Multiple Entry Found")
                log(f"[WARN] get_file multiple matches for pattern {path}: {matches}")
                return False
        else:
            check = file
            log(f"[INFO] get_file no glob match for {path}, using literal")
            return check.replace("'", "")

#------------------------------------file utilities------------------------------------------------------------------------------------------      

    def file_sys(self, option, file): #13
        log(f"[INFO] file_sys called option={option} file={file}")
        if option == "-c":
            if exists(file) == False:
                log(f"[INFO] file_sys creating new file {file}")
                data = input(F.YELLOW+"[%]Enter Data: "+F.WHITE)
                open_file = open(file, "w")
                open_file.write(data)
                print (F.BLUE+"[✓]File Created Successfully".upper())
                open_file.close()
            else:
                print (F.RED+"[*]File Already Exist, Wish To Rewrite It".upper())
                opt = input(F.YELLOW+"[?]Y/N: "+F.WHITE).upper()
                if opt == "N":
                    print (F.BLUE+"[✓]File Was Maintained".upper())
                elif opt == "Y":
                    log(f"[INFO] file_sys overwriting file {file}")
                    data = input(F.YELLOW+"[%]Enter Data: "+F.WHITE)
                    open_file = open(file, "w")
                    open_file.write(data)
                    print (F.BLUE+"[✓]File Created Successully".upper())
                    open_file.close()
                else:
                    print (F.RED+"[x]Error, Try Inputing Valid Data".upper())


        elif option == "-a":
            file = self.get_file(file)
            if not file:
                return False
            if exists(file):
                log(f"[INFO] file_sys appending to file {file}")
                data = input(F.YELLOW+"[%]Enter Data: "+F.WHITE)
                open_file = open(file, "a")
                open_file.write(data)
                open_file.close()
                print (F.BLUE+"[✓]Done".upper())
            else:
                print (F.RED+"[x]File Doesn't Exist".uppper())
                log(f"[WARN] file_sys append failed, file not found: {file}")


        elif option == "-d":
            os = self.os
            file = self.get_file(file)
            if not file:
                return False
            if exists(file):
                log(f"[INFO] file_sys deleting file {file}")
                os.remove(file)
                print (F.BLUE+"[✓]File Deleted ".upper())
            else:
                print (F.RED+"[x]File Doesn't Exist".upper())
                log(f"[WARN] file_sys delete failed, file not found: {file}")


        elif option == "-v":
            file = self.get_file(file)

            if not file:
                return False
            log(f"[INFO] file_sys viewing info for {file}")
            os = self.os
            if os.path.isfile(file):
                size_bytes = os.path.getsize(file)
                file_size = self.byte_size(size_bytes)

                file_extension = os.path.splitext(file)[1] or "N/A"

                mime_type, _ = mimetypes.guess_type(file)
                add_f = "'"+file+"'"
                file_type_data = sub.getoutput(f"file {add_f}").replace(f"{file}", "").replace(": ", "")

                last_modified_timestamp = os.path.getmtime(file)
                last_modified_time = datetime.fromtimestamp(last_modified_timestamp).strftime('%d-%m-%Y %H:%M:%S')

                location = os.path.abspath(file)

                is_hidden = "Yes" if os.path.basename(file).startswith('.') else "No"
                is_executable = "Yes" if os.access(file, os.X_OK) else "No"

                data = {
                    "File Size": file_size,
                    "File Extension": file_extension,
                    "File Type": file_type_data,
                    "Last Modified Time D/M/Y": last_modified_time,
                    "Location": location,
                    "Hidden": is_hidden,
                    "Executable": is_executable,
                }

                for key, value in data.items():
                    print(f"{F.CYAN}[*]{key}: {F.GREEN}{value}")
                log(f"[INFO] file_sys displayed file info for {file}")

            elif os.path.isdir(file):
                c_file = file
                total_size = 0
                file_count = 0
                folder_count = 0
    
                for root, dirs, files in os.walk(c_file):
                    try:
                        folder_count += len(dirs)
                        file_count += len(files)
                        for file in files:
                            total_size += os.path.getsize(os.path.join(root, file))
                    except FileNotFoundError:
                        continue

                formatted_size = self.byte_size(total_size)
                last_modified_timestamp = os.path.getmtime(c_file)
                last_modified_time = datetime.fromtimestamp(last_modified_timestamp).strftime('%d-%m-%Y %H:%M:%S')

                location = os.path.abspath(c_file)

                is_hidden = "Yes" if os.path.basename(c_file).startswith('.') else "No"

                data = {
                    "Number of Files": file_count,
                    "Number of Subfolders":folder_count,
                    "Total Size": formatted_size,
                    "Last Modified Time D/M/Y": last_modified_time,
                    "Location": location,
                    "Hidden": is_hidden,
                }
                for key, value in data.items():
                    print(f"{F.CYAN}[*]{key}: {F.GREEN}{value}")
                log(f"[INFO] file_sys displayed directory info for {c_file}")
                    
            else:
                print (F.RED+"[x]No Such File Or Directory")
                log(f"[WARN] file_sys view failed, no such file or directory: {file}")
                
                
        elif option == "-r":
            file = self.get_file(file)
            if not file:
                return False
            os = self.os

            if exists(file):
                log(f"[INFO] file_sys reading file {file}")
                try:
                    open_file = open(file, "r")
                    print(F.BLUE+"[*]File.Content:"+F.WHITE+"")
                    buffer = 1024
                    while True:
                        data = open_file.read(buffer)
                        print(data, end="")
                        if not data:
                            break
                    log(f"[INFO] file_sys finished reading text file {file}")
                except:
                    open_file = open(file, 'rb')
                    buffer = 1024
                    while True:
                        data = open_file.read(buffer)
                        print(data, end="")
                        if not data:
                            break
                    log(f"[INFO] file_sys finished reading binary file {file}")
            else:
                print (F.RED+"[x]File Doesn't Exist")
                log(f"[WARN] file_sys read failed, file not found: {file}")


        elif option == "-ed":
            os = self.os
            file = self.get_file(file)
            log(f"[INFO] file_sys option='-ed' called for file={file}")
            if not file:
                return False
            if exists(file) and os.path.isfile(file):
                reg = file.endswith(".enc")
                if reg == True:
                    print (F.GREEN+"[*]File Is In Encrypted Format!!\n[*]Wish To Decrypt")
                    opt = input(F.YELLOW+"[?]Y/N: "+F.WHITE).upper()
                    if opt == "Y":
                        print(F.BLUE+"[Note]: Key Must Be EITHER 16, 24 Or 32 Bytes Character\n[*]Meaning Your Key Should Be ↑Above↑ Bytes Character Long")
                        key = input(F.CYAN+"[%]KEY: "+F.WHITE)
                        log(f"[INFO] file_sys decrypt requested for {file} with provided key length={len(key)}")
                        if len(key) == 16 or len(key) == 24 or len(key) == 32:
                            key = key.encode()
 
                            buffer_size = 65536
                            with open(file, "rb") as files:
                                files.seek(0,2)
                                size = files.tell()
                            
                            open_file = open(file, "rb")
                            iv = open_file.read(16)
                            size = size - len(iv)
  
                            cipher_encrypt = AES.new(key, AES.MODE_CFB, iv=iv)
                            buffer = open_file.read(buffer_size)
                            file = file.replace(".enc","")
                            output_file = open(file, "wb")
                            print(F.YELLOW+"")
                            with tqdm(total=size, unit='B', unit_scale=True, desc="Decrypting File", ascii=False) as progress_bar:
                                while len(buffer) > 0:
                                    new = buffer
                                    decrypted_bytes = cipher_encrypt.decrypt(new)
                                    new_data = decrypted_bytes
                                    output_file.write(new_data)
                                    buffer = open_file.read(buffer_size)
                                    progress_bar.update(len(new_data))

                            open_file.close()
                            output_file.close()
                            print (F.BLUE+"[✓]File Decrypted Successfully                             ")
                            print(f'{F.CYAN}[*]Decrypted File Is {F.YELLOW}{file}')
                            log(f"[INFO] file_sys decrypted file successfully -> {file}")

                        else:
                            print (F.RED+"[x] Invalid Key Byte Size Or No key Detected")
                            log(f"[ERROR] file_sys decryption failed for {file}: invalid key length={len(key)}")

                    elif opt == "N":
                        print (F.BLUE+"[✓]File Was Maintained")

                    else:
                        print (F.RED+"[x]Error, Invalid Input")

                elif reg == False:
                    print (F.GREEN+"[*]File Is In Decrypted Format!!\n[*]Wish To Encrypt")
                    opt = input(F.YELLOW+"[?]Y/N: "+F.WHITE).upper()
                    if opt == "Y":
                        print(F.BLUE+"[*]Note: Key Must Be Either 16, 24 OR 32 Bytes Character\n[*]Meaning Your Key Should Be ↑Above↑ Bytes Character Long")
                        option = input(F.CYAN+"[?]Generate Key [Y/N]: ").upper()
                        if option == "Y":
                            num = int(input(F.YELLOW+'[%]Key Length: '))
                            keyD = self.key(num)
                            log(f"[INFO] file_sys generated key for encryption of {file} with length={num}")
                        elif option == "N":
                            keyD = input(F.CYAN+"[%]Key: "+F.WHITE)
                        else:
                            print(F.RED+"[x] Invalid Input")
                            return True
                        if len(keyD) == 16 or len(keyD) == 24 or len(keyD) == 32:
                            print(f'{F.CYAN}[*]Your Key Is: {F.WHITE}{keyD}')
                            key = keyD.encode()
                            with open(file, "rb") as files:
                                files.seek(0,2)
                                size = files.tell()

                            buffer_size = 65536 
                            iv = os.urandom(16)
                            
                            cipher_encrypt = AES.new(key, AES.MODE_CFB, iv=iv)
                            open_file = open(file, 'rb')
                            buffer = open_file.read(buffer_size)
                            file = file+".enc"
                            output_file = open(file, "wb")
                            output_file.write(iv)
                            
                            print(F.YELLOW+"")
                            with tqdm(total=size, unit='B', unit_scale=True, desc="Encrypting File", ascii=False) as progress_bar:
                                while len(buffer) > 0:
                                    ciphered_bytes = cipher_encrypt.encrypt(buffer)
                                    new_data = ciphered_bytes
                                    output_file.write(new_data)
                                    buffer = open_file.read(buffer_size)
                                    progress_bar.update(len(new_data))
                            open_file.close()
                            output_file.close()
                            print (F.BLUE+"[✓]File Encrypted Succesfully")
                            file_ = "/".join(file.split(os.sep)[-1:])
                            print(f'{F.CYAN}[*]Encrypted File Is {F.WHITE}{file_}')

                            log(f"[INFO] file_sys encrypted file {file} -> {file_} with key length={len(keyD)}")

                            key_file = open("key.txt", "a")
                            cur_dir = os.getcwd()
                            data = "[Filnename= "+file+" :Key= "+keyD+" ]\n"
                            key_file.write(data)
                            print(f"{F.CYAN}[*]Key Saved On {F.YELLOW}{cur_dir}/{F.WHITE}key.txt")
                            log(f"[INFO] file_sys saved encryption key for {file} to {cur_dir}/key.txt")
                        else:
                            print(F.RED+"[x]Invalid Key Byte SIZE")

                    elif opt == "N":
                        print (F.BLUE+"[✓]File Was Maintained")

                    else:
                        print (F.RED+"[x]Error, Invalid Input")
            elif exists(file) and os.path.isdir(file):
                print (F.RED+"[x]Folder Not Supported")
            else:
                print(F.RED+"[x]File Not Found")
        else:
            print(F.RED+"[x]Invalid Option")

#-----------------------------------end message to a whatsapp contact-------------------------------------------------------------------------------------------          

    def send_mess(self, number): #14
        message = input(F.YELLOW+"[%]Message: "+F.WHITE).replace(" ", "%20")
        null = sub.getoutput(f'xdg-open https://wa.me/{number}?text={message}')
        print (F.BLUE+"[*]Opening Whatsapp....")

#-------------------------------------send file via wifi or localhost-----------------------------------------------------------------------------------------

    def send_file(self): #15
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(500)
        a1, a2, a3 = str(rd.randint(1,6)), str(rd.randint(1,6)), str(rd.randint(1,5))
        port = a3+a2+a1+a2+a3
        sock.bind(('0.0.0.0', int(port)))
        print (F.BLUE+"[✓]Server Started")
        print (F.CYAN+"[*]Possible IP Address Listed Below")
        ip = self.get_private_addr()
        print (F.CYAN+f"[*]Ip: {F.YELLOW}{ip}{F.CYAN}[*]Port: {F.YELLOW}{port}")

        log(f"[INFO] send_file server started on {ip}:{port}")

        sock.listen(5)

        file_path = input(F.YELLOW+"[%]/path/to/file: "+F.WHITE)
        file_path = self.get_file(file_path)
        if not file_path:
            return False
        if file_path:
            #
            with open(file_path, "rb") as file:
                file.seek(0, 2) 
                size = file.tell()
            size_s = self.byte_size(size)

            file = "/".join(file_path.split(os.sep)[-1:])

            while True:
                c = None
                try:
                    c, addr = sock.accept()
                    auth_s = '0x2000'
                    c.send(auth_s.encode())
                    auth_r = c.recv(6).decode()
                    if not auth_r: c.close(); continue
                    if auth_r == auth_s:
                        log(f"[INFO] send_file accepted connection from {addr}")
                        break
                    else: c.close(); log('[x] Invalid Connection On Send File Func'); continue
                except KeyboardInterrupt: return 0
                except ConnectionResetError: c.close; log('[x]Invalid Connection On Send File Func'); continue
                except socket.timeout: print(F.RED+"[x]Timed Out"); return 0

            print(F.CYAN+"[✓]User Connected")
            print(F.BLUE+"[*]Waiting For User To Accept")
            c.send(f'[*]Incoming File! [Name: {file}] [Size: {size_s}]\n'.encode())
            choice = c.recv(1024).decode()
            if "YES" in choice: 
                c.send(str(size).encode())
                print (F.CYAN+"") 
                with tqdm(total=size, unit='B', unit_scale=True, desc="Uploading", ascii=False) as progress_bar:
                    with open(file_path, 'rb') as file:
                        for data in iter(lambda:     file.read(1024), b''):
                            c.send(data)
                            progress_bar.update    (len(data))
                c.close()
                print(F.BLUE+"[✓]File Uploaded")
                log(f"[INFO] send_file uploaded {file} ({size_s}) to {addr}")
            else:
                print(F.CYAN+"[x]Reciever Aborted")
                log(f"[WARN] send_file receiver aborted transfer for {file} from {addr}")
                c.close()
        else:
            print(F.RED+"[x]Error: Empty Input")

#------------------------------------recieve file via wifi or localhost------------------------------------------------------------------------------------------

    def recv_file(self, ip, port): #16
        c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        log(f"[INFO] recv_file attempting connection to {ip}:{port}")
        while True:
            c_socket.connect((ip, int(port)))
            auth_s = '0x2000'
            auth_r = c_socket.recv(6).decode()
            c_socket.send(auth_s.encode())

            if auth_r == auth_s:
                print(F.CYAN+"[✓]Connected To Server")
                log(f"[INFO] recv_file connected to {ip}:{port}")
                break
            else: print(F.RED+'[x]Invalid Connection'); c_socket.close(); return 0

        data = c_socket.recv(1024).decode()
        print (F.BLUE+data)

        file = input(F.YELLOW+"[%]/save/to/path/to/file: "+F.WHITE)
        if file:

            choice = input(F.YELLOW+"[?]Wish To Accept: [Y/N]: "+F.WHITE).upper()
            if choice == "Y":
                c_socket.send("YES".encode())
                size = c_socket.recv(1024).decode()
                size = int(size)
                print (F.CYAN+"")
                with tqdm(total=size, unit='B', unit_scale=True, desc="Downloading", ascii=False) as progress_bar:
                    with open(file, 'wb') as new_file:
                        while True:
                            rec = c_socket.recv(1024)
                            if not rec:
                                break
                            new_file.write(bytes(rec))
                            progress_bar.update(len(rec))
                c_socket.close()
                print (F.BLUE+"[✓]File Downloaded")
                log(f"[INFO] recv_file downloaded file to {file} from {ip}:{port}")
            elif choice == "N":
                c_socket.send("...".encode())
                print(F.CYAN+"[*]Aborted")
                log(f"[WARN] recv_file user aborted download for target {file}")
                c_socket.close()
            else:
                c_socket.send("...".encode())
                print(F.RED+"[x]Invalid Input")
                c_socket.close()
        else:
            c_socket.send("...".encode())
            print(F.RED+"[x]Error: Empty Input")
            c_socket.close()

#----------------------------------- open server for shell-------------------------------------------------------------------------------------------

    def shell_host(self): #17
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(500)
        a1, a2, a3 = str(rd.randint(1,6)), str(rd.randint(1,6)), str(rd.randint(1,5))
        ip = self.get_private_addr()
        port = a3+a2+a1+a2+a3
        print(F.CYAN+"[Note]: Input <@exit> To Close Session")
        print (F.BLUE+"[✓]Shell Host Started")
        print (F.CYAN+"[*]Possible IP Address Listed Below")
        print (F.CYAN+f"[*]Ip: {F.YELLOW}{ip}{F.CYAN}[*]Port: {F.YELLOW}{port}")

        sock.bind(("0.0.0.0", int(port)))
        sock.listen(5)
        log(f"[INFO] shell_host started on {ip}:{port}")
        while True:
            c = None
            try:
                c, addr = sock.accept()
                auth_s = '0x3000'
                self.sock_(c, auth_s, True)
                auth_r = self.sock_(c, True, False)
                if not auth_r: c.close(); continue
                if auth_s == auth_r:
                    log(f"[INFO] shell_host accepted connection from {addr}")
                    break
                else: c.close(); log('[x] Invalid Connection On Shell Host Func'); continue
            except KeyboardInterrupt: return 0
            except ConnectionResetError: c.close; log('[x]Invalid Connection On Shell Host Func'); continue
            except socket.timeout: print(F.RED+"[x]Timed Out"); return 0

        print (F.GREEN+"[✓]Client Connected")
        log(f"[INFO] shell_host client connected {addr}")
        
        while True:
            data = input(F.CYAN+"\n[shell]: "+F.WHITE)

            if data == "@exit":
                self.sock_(c, data, True)
                print(F.RED+"[*]Closing Shell")
                log(f"[INFO] shell_host closing session with {addr}")
                c.close()
                break
            elif data == False:
                continue
            self.sock_(c, data, True)

            rec = self.sock_(c, True, False)
            if "::EXEC" in rec or "::DIR" in rec or "::FILE" in rec:
                for match in rec.split(" "):
                    if "::EXEC" in match:
                        print(F.GREEN+match.replace("::EXEC", ""))
                    elif "::DIR" in match:
                        print(F.BLUE+match.replace("::DIR", ""))
                    elif "::FILE" in match:
                        print(F.WHITE+match.replace("::FILE", ""))
            else:
                print(F.WHITE+rec)

#------------------------------------connect to shell host------------------------------------------------------------------------------------------

    def shell_client(self, ip, port): #18
        os = self.os
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        while True:
            sock.connect((ip, int(port)))

            auth_s = '0x3000'
            auth_r = self.sock_(sock, True, False)
            self.sock_(sock, auth_s, True)

            if auth_r == auth_s:
                log(f"[INFO] shell_client connected to host {ip}:{port}")
                break
            else: print(F.RED+'[x]Invalid Connection'); sock.close(); return 0

        print(F.BLUE+"[✓]Connected To Host")
        print(F.YELLOW+"[*]━━━━━━━━━━━━━━━━SERVER LOG━━━━━━━━━━━━━━━━")
        
        while True:
            data = self.sock_(sock, True, False)
            if not data:
                print(f'{F.RED}[x]SERVER DISCONNECTED')
                log(f"[WARN] shell_client detected server disconnect {ip}:{port}")
                sock.close()
                break

            print(f"{F.GREEN}[*]Host Executed: {F.WHITE}{data}")
            log(f"[INFO] shell_client received host command: {data}")
            if data == "@exit":
                print (F.RED+"[*]Host Closed Shell")
                sock.close()
                break

            elif data.strip() == "ls":
                data = sub.getoutput("ls")
                entries = data.split()      # split by whitespace (each file/folder)
                tagged_entries = []
                
                for f in entries:
                    # make a full path so we can check type
                    full_path = os.path.join(os.getcwd(), f)

                    if os.path.isdir(full_path):
                        tagged_entries.append(f"{f}::DIR")
                    elif os.path.isfile(full_path) and os.access(full_path, os.X_OK):
                        tagged_entries.append(f"{f}::EXEC")
                    else:
                        tagged_entries.append(f"{f}::FILE")

                    # this is ready to send over socket
                    data = " ".join(tagged_entries)

            elif data.startswith('cd '):
                path = data[3:]
                path = self.get_file(path)
                try:
                    os.chdir(path)
                    data = os.getcwd()
                except:
                    data = "Invalid Directory"

            else:
                try:
                    decode_data = sub.run(
                        data,
                        shell=True,
                        stdout=sub.PIPE,
                        stderr=sub.STDOUT,
                        stdin=sub.DEVNULL,
                        timeout=0.5,
                        text=True
                    )
                    data = decode_data.stdout if decode_data.stdout else 'DONE'
                except:
                    data = 'unexpected'

            self.sock_(sock, data, True)

#----------------------------------encrypt a string --------------------------------------------------------------------------------------------

    def crypt(self): #19
        data = input(F.CYAN+"[%]Data: "+F.WHITE)
        data1 = data.replace(" ", "~").encode()
        cryp_hash = str(0000)
        rep = len(data)-1//len(cryp_hash)+1
        a4 = (cryp_hash*rep)[:len(data)].encode()
        new_data = bytes([i1^i2 for (i1,i2) in zip(data1 , a4)])
        dec_data = new_data.decode()
        rep1 = dec_data.replace("~", " ")
        print(F.CYAN+"[*]Data: "+F.BLUE+rep1)

#------------------------------phone number osint------------------------------------------------------------------------------------------------

    def check_phone(self, number): #20
        log(f"[INFO] check_phone() called number={number}")
        user_phone = number
        C = F.CYAN
        B = F.BLUE

        default_region = 'ID'

        parsed_num = phone.parse(user_phone, default_region)
        region_code = phone.region_code_for_number(parsed_num)
        jenis_provider = carrier.name_for_number(parsed_num, "en")
        location = geocoder.description_for_number(parsed_num, "id")
        is_valid_number = phone.is_valid_number(parsed_num)
        is_possible_number = phone.is_possible_number(parsed_num)
        formatted_number = phone.format_number(parsed_num, phone.PhoneNumberFormat.INTERNATIONAL)

        formated_num_mo = phone.format_number_for_mobile_dialing(parsed_num, default_region, with_formatting=True)

        number_type = phone.number_type(parsed_num)
        timezone1 = phone.timezone.time_zones_for_number(parsed_num)
        timezoneF = ', '.join(timezone1)
        
        num = 0
        r = 0
        for i in range(100):
            num += 0.2
            d = F.GREEN+'█'*int(num)
            r += 1
            tm.sleep(0.003)
            print(f'{B}[*]Loading Information: {d} : {C}{str(r)}%', end='\r', flush=True)

        print(f"\n\n{C}[*]Location             :{B}{location}")
        print(f"{C}[*]Region Code          :{B}{region_code}")
        print(f"{C}[*]Timezone             :{B}{timezoneF}")
        print(f"{C}[*]Operator             :{B}{jenis_provider}")
        print(f"{C}[*]Valid Number         :{B}{is_valid_number}")
        print(f"{C}[*]Possible Number      :{B}{is_possible_number}")
        print(f"{C}[*]International Format :{B}{formatted_number}")
        print(f"{C}[*]Mobile Format        :{B}{formated_num_mo}")
        print(f"{C}[*]Original Number      :{B}{parsed_num.national_number}")
        print(f"{C}[*]E.164 Format         :{B}{phone.format_number(parsed_num, phone.PhoneNumberFormat.E164)}")
        print(f"{C}[*]Country Code         :{B}{parsed_num.country_code}")
        print(f"{C}[*]Local Number         :{B}{parsed_num.national_number}")
        if number_type == phone.PhoneNumberType.MOBILE:
            print(f"{C}[*]Type                 :{B}This Is A Mobile number")
        elif number_type == phone.PhoneNumberType.FIXED_LINE:
            print(f"{C}[*]Type                 :{B}This Is A Fixed-Line Number")
        else:
            print(f"{C}[*]Type                 :{B}This Is Another Type Of Number")

#----------------------------------check weather information of a city/country--------------------------------------------------------------------------------------------

    def weather(self, city): #24
        try:
            giblish = "ddf55"+"8573"+"97f91b"+"75d8622f3"+"161d6f8b"
            base_url = "http://api.openweathermap.org/data/2.5/weather"
            params = {"q": city, "appid": giblish, "units": "metric"}
            response = r.get(base_url, params=params)
            data = response.json()
            if response.status_code == 200:
                main_weather = data["weather"][0]["description"]
                temperature = data["main"]["temp"]
                print(f"{F.BLUE}[*]Weather: {F.GREEN}{main_weather} \t {F.BLUE}[*]Temperature: {F.GREEN}{temperature}°C")
            else:
                print(F.RED+"[x]An Error Occured, Invalid City/Country")
        except r.exceptions.RequestException as e:
            print(F.RED+"[x]Error Connecting To Host")

#-------------------------------------search a file-----------------------------------------------------------------------------------------
   
    def search(self, directory, target_file):
        try:
            full_path = directory
            os = self.os
            items = os.scandir(directory)
            
            for item in items:
                if item.is_dir(follow_symlinks=False):
                    self.search(item.path, target_file)
                elif item.name == target_file:
                    print(f"{F.GREEN}[✓]File Found: {F.WHITE}{full_path}/{target_file}")
                    self.file_counter()
                else:
                    print(f"{F.CYAN}[*]Crawling Files: {F.GREEN}{self.search_counter()}", end='\r')
                    

        except PermissionError:
            print(f"{F.RED}[x]Permission Denied: {F.WHITE}{full_path}")
            self.search_counter()

        except FileNotFoundError:
            print(f"{F.RED}[x]No Such Path: {F.WHITE}{full_path}")

        except IOError:
            print(f"{F.RED}[x]I/O ERROR: {F.WHITE}{full_path}")
            self.search_counter()

#------------------------count matched files------------count searched files------------------------------------------------------------------------------------------
  
    def file_counter(self):
        self.count_f += 1
        return self.count_f

    def search_counter(self):
        self.count_s += 1
        return self.count_s

#---------------------------------------file search trigger ---------------------------------------------------------------------------------------
   
    def trigger_search(self, directory):

        folder = "/data/data/com.termux" if directory == "/termux" else directory

        target__file = input(f"{F.BLUE}[%]File To Search:{F.WHITE} ").replace("'", "")
        
        log(f"[INFO] trigger_search() called folder={folder} target_input={target__file}")
        if target__file:

            print("")
            self.search(folder, target__file)
            print(f"{F.CYAN}\n[*]File Occurence: {F.GREEN}{self.file_counter()-1}")
            self.count_f = 0
            self.count_s = 0

        else:
            print(F.RED+"[x]Error: Empty Input")

#---------------------------computer mac byte---------------------------------------------------------------------------------------------------

    def check_rand(self, mac):
        try:
            mac = mac.replace('-', ':').lower()
            first_byte = mac.split(':')[0]
            first_byte_int = int(first_byte, 16)

            return bool(first_byte_int & 0b00000010)
        except:
            return False

#-----------------------------check mac address-------------------------------------------------------------------------------------------------

    def mac_lookup(self, mac):
        log(f"[INFO] mac_lookup() looking up mac={mac}")
        if not self.check_rand(mac):
            url = f"https://api.macvendors.com/{mac}"
        
            response = r.get(url)
            if response.status_code == 200:
                print(f"{F.CYAN}[*]Device Manufacturer: {F.WHITE}{response.text}")
            else:
                print(F.RED+"[x]No Mac Record Found")
        else:
            print(F.RED+"[x]Mac Is Locally Assigned [Not Lookable]")

#-----------------------------lookup version-------------------------------------------------------------------------------------------------
  
    def version(self):
        home = os.environ["HOME"]
        file = f"{home}/Shell/__version__"
        open_file = open(file, 'r')
        log("[INFO] version() called")
        print(F.GREEN+'[*]VERSION:',F.CYAN+open_file.read().strip())
        open_file.close()

#-------------------------logs-----------------------------------------------------------------------------------------------------

    def open_log(self, mode):
        home = os.environ['HOME']
        file = f'{home}/Shell/UTILS/.logs'

        if mode == '-show':
            log(f"[INFO] open_log show logs requested")
            open_file = open(file, 'r')
            print(F.GREEN+'[*]----------------------------LOGS------------------------------')
            print(F.WHITE+open_file.read())
            open_file.close()

        elif mode == '-clear':
            log(f"[INFO] open_log clearing logs")
            open_file = open(file, 'w')
            print(F.GREEN+'[*]Cleared')
            open_file.close()

        else:
            print(F.RED+'[x]Invalid Mode')

#---------------------------change name---------------------------------------------------------------------------------------------------

    def change_name(self, name):
        global username
        name = name.replace(" ", "_")
        home = os.environ["HOME"]
        log(f"[INFO] change_name() requested new_name={name}")
        with open(f"{home}/Shell/UTILS/.config.json", "r") as file:
            data = json.load(file)
            
        if name == "default": name = sub.getoutput("whoami")
        else: pass

        data["username"] = name
        with open(f"{home}/Shell/UTILS/.config.json", "w") as file:
            json.dump(data, file, indent=4)
            print(f"{F.GREEN}[✓]Name Updated")
        username = name

#-------------------------check site for reachability-----------------------------------------------------------------------------------------------------

    def site_checker(self, domain):
        log(f"[INFO] site_checker() checking domain={domain}")
        output = check_site(domain)
        if not output:
            print(f"{F.RED}[!]Error Resolving Server Element")
        elif output == "null_internet":
            print(f"{F.RED}[x]Can't Reach Internet")
        elif output == "unreach":
            print(f"{F.RED}[x]Can't Reach Server")
        else:
            print(f"{F.GREEN}[*]Site is {F.CYAN}{output}")

#------------------------ip subnet calculator------------------------------------------------------------------------------------------------------

    def ip_calculate(self, ip, prefix):

        # Handle User Input 
        sample = '1234567890.'
        for i in ip:
            if i not in sample:print(F.RED+'[x]Invalid IP');return False
        octet_list = ip.split('.')
        if len(octet_list) > 4:print(F.RED+'[x]Invalid IP');return False
        for octet in octet_list:
            if int(octet) > 255:print(F.RED+'[x]Invalid IP');return False
        try:prefix = int(prefix)
        except:print(F.RED+'[x]Invalid Prefix');return False

        prefix = '32' if int(prefix) > 32 else str(prefix)
        prefix = '0' if int(prefix) < 0 else str(prefix)
        log(f"[INFO] ip_calculator() checking network={ip}/{prefix}")
        print(print_result(ip, prefix, F))

#------------------------------------relay for all tools------------------------------------------------------------------------------------------

shark = shark()
if __name__ == '__main__':
    shark.main()
    memory = compute()

    #start Future background processs
    #process = multiprocessing.Process(target=background)
    #process.start()

    while True:
        data = inpu()
        if data: pass
        else: continue
        try: data_strip = data.replace(' ','')
        except: continue 

        #resolve spaced file
        def cons_(num):
            return ' '.join(data.split()[num:])
            
        try:
            #data = inpu()
            if '@help'in data_strip and data.strip().startswith('@help'): 
                shark.help()
            elif "@get-i" in data_strip and data.strip().startswith('@get'): 
                shark.get_ip(data.split()[2])
            elif "@port-st" in data_strip and data.strip().startswith('@port'):
                run_port(data.split()[2], data.split()[3])
            elif "@bina-a" in data_strip and data.strip().startswith('@bina'): 
                shark.Bina_Alpha(cons_(2))
            elif "@alpha-b" in data_strip and data.strip().startswith('@alpha'): 
                shark.Alpha_Bina(cons_(2))
            elif "@num-b" in data_strip and data.strip().startswith('@num'): 
                shark.Num_Bina(data.split()[2], data.split()[3])
            elif "@bina-n" in data_strip and data.strip().startswith('@bina'): 
                shark.Bina_Num(data.split()[2], data.split()[3])
            elif "@ip-details" in data_strip and data.strip().startswith('@ip'):
                shark.get_device_ip()

#------------------------------------------------------------------------------------------------------------------------------

            elif "@open-server" in data_strip and data.strip().startswith('@open'): 
                shark.open_server()
            elif "@con-s" in data_strip and data.strip().startswith('@con'): 
                shark.connect_server(data.split()[2], data.split()[3])
            elif "@file" in data_strip and data.strip().startswith('@file'):
                    shark.file_sys(data.split()[1], cons_(2))
            elif "@send-w" in data_strip and data.strip().startswith('@send'):
                shark.send_mess(data.split()[2])
            elif "@send-file" in data_strip and data.strip().startswith('@send'): 
                shark.send_file()
            elif "@recv-f" in data_strip and data.strip().startswith('@recv'): 
                shark.recv_file(data.split()[2], data.split()[3])
            elif "@shell-host" in data_strip and data.strip().startswith('@shell'):
                shark.shell_host()

#------------------------------------------------------------------------------------------------------------------------------

            elif "@shell-c" in data_strip and data.strip().startswith('@shell'):
                shark.shell_client(data.split()[2], data.split()[3])
            elif "@crypt" in data_strip and data.strip().startswith('@crypt'): 
                shark.crypt()
            elif "@check-n" in data_strip and data.strip().startswith('@check'): 
                shark.check_phone(data.split()[2])
            elif "@check-w" in data_strip and data.strip().startswith('@check'): 
                shark.weather(data.split()[2])
            elif "@ip-s" in data_strip and data.strip().startswith('@ip'):
                shark.ip_osint(data.split()[2])
            elif "@sch-f" in data_strip and data.strip().startswith('@sch'):
                shark.trigger_search(cons_(2))
            elif "@sch-m" in data_strip and data.strip().startswith('@sch'):
                shark.mac_lookup(data.split()[2])
            elif "@solve-res" in data_strip and data.strip().startswith('@solve'):
                run_resist()

#------------------------------------------------------------------------------------------------------------------------------

            elif "@version" in data_strip and data.strip().startswith('@version'):
                shark.version()
            elif "@logs" in data_strip and data.strip().startswith('@logs'):
                shark.open_log(data.split()[1])
            elif "@shark" in data_strip and data.strip().startswith('@shark'):
                memory.update({data.split("=")[0].split()[1]: data.split("=")[1]})
            elif "@clone" in data_strip and data.strip().startswith('@clone'):
                if data.split()[2] == "file":
                    clone_alias(True)
                    print(F.RED+"[!]Cloned: Restart The Shell For Update To Take Effect")
                elif data.split()[2] == "mem":
                    memory.update(clone_alias(False))
            elif "@name" in data_strip and data.strip().startswith('@name'):
                shark.change_name(cons_(1))
            elif "@check-s" in data_strip and data.strip().startswith('@check'):
                shark.site_checker(data.split()[2])
            elif "@ip-c" in data_strip and data.strip().startswith('@ip'):
                shark.ip_calculate(data.split()[2], data.split()[3])
            elif "@exit" in data_strip and data.strip().startswith('@exit'):
                sys("clear")
                #process.terminate()
                quit(0)

#------------------------------------------------------------------------------------------------------------------------------

            elif data.lstrip().startswith('cd') and "cd" != data.strip():
                d_path = ' '.join(filter(None, data.split()))
                path = d_path[3:]
                matches = glob.glob(path)
                if matches:
                    if len(matches) == 1:
                        os.chdir(matches[0])
                    else:
                        print(F.RED+"[x]Multiple Entry Found")
                else:
                    print (f"cd:{path}: No Such File Or Directory")

            elif data.strip() == 'cd':
                os.chdir(os.path.expanduser("~"))

            elif '@update' in data_strip and data.strip().startswith('@update'):
                print(trigger_software_update())

#------------------------------------------------------------------------------------------------------------------------------
            
            else:
                for alias in memory.keys():
                    if data.split()[0] == alias:
                        data = data.split()[0].replace(alias, memory[alias].strip()) +' '+' '.join(data.split()[1:])
                sub.run(data, shell=True)

        except FileNotFoundError:
            print(F.RED+"[x]File Not Found")
        except IsADirectoryError:
            print(F.RED+"[x]Not A File")

#------------------------------------------------------------------------------------------------------------------------------

        except ValueError:
            print(F.RED+"[x]Invalid Value")
        except PermissionError:
            print(F.RED+"[x]Permission Error")
        except KeyboardInterrupt:
            continue
        except IndexError:
            print(F.RED+"[x]Invalid Argument")
        except Exception as e:
            print(f'{F.RED}[x]Error: {e}')

#------------------------------------------------------------------------------------------------------------------------------
# end line 1489