#!/usr/bin/env python3


#------------------------------------------------------------------------------------------------------------------------------


# import all libraries
from UTILS.BOOT_SETUP.util_boot import *
from UTILS.BOOT_SETUP.util_boot import trigger_software_update
from UTILS.resistor import *
from UTILS.alias import *


#------------------------------------------------------------------------------------------------------------------------------

#clear screen after loading libraries
sys("clear")

#------------------------------------------------------------------------------------------------------------------------------

        
    
# input function
def inpu():
    #get working directories
    try:
        print("\n")
        subt = sub.getoutput("whoami")
        direc = os.getcwd()
        new_path = "/".join(direc.split(os.sep)[-3:])
        new_path = F.CYAN+new_path+F.YELLOW
        
        #initiate input method
        s = F.CYAN+"§"
        data = input(F.YELLOW+f"{F.YELLOW}╭─({F.CYAN}{subt}{F.YELLOW}@{F.CYAN}Shell{F.YELLOW})——[{new_path}]\n│\n{F.YELLOW}╰─{s} "+ F.WHITE)
        readline.add_history(data)
        return data
    except:
        return 1


#------------------------------------------------------------------------------------------------------------------------------


# initialize the class
class shark:
    def __init__(self):
        self.soc = socket
        self.os = os
        self.count = 0



        
    # load the welcome screen on start
    def main(self):
        data = f"""
                {F.CYAN}  ╭────────────────────────╮
                │ │ {F.YELLOW}WELCOME·TO·SHARK-SHELL{F.CYAN} |─╮
                ╰─│  {F.GREEN}For Help: Run {F.WHITE}@help{F.CYAN}   │ │
                  ╰────────────────────────╯
                    """
        print (data)



#------------------------------------------------------------------------------------------------------------------------------
    

    # function for list of tools
    def help(self): #1
        home = os.environ["HOME"]
        data = open(f"{home}/Shell/UTILS/.shell_help", "r").read()
        print(eval(f"f'''{data}'''"))





#------------------------------------------------------------------------------------------------------------------------------



    # getting ip address of a site
    def get_ip(self, host): #2
        try:
            data = self.soc.gethostbyname(host)
            print (F.CYAN+f"[✓]{host}: {F.BLUE}{data}")
        except:
            print (F.RED+"[x]Error, Maybe Invalid Host Or No Internet Connection")



#------------------------------------------------------------------------------------------------------------------------------



    # multiple port scanning using ping interval as timeout
    def port_scan(self, ip): #3
        data = sub.getoutput(f'ping -w 1 {ip} ')

        try:
            re_search = re.search(r'(time=)(\d+)', data)
            interval = int(re_search.group(2))/1000
            print (F.CYAN+"[*]Start Scanning In Time Interval: "+F.YELLOW+str(interval))

            total_port = 0
            port = -1
            for i in range(65354):
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    port += 1
                    sock.settimeout(interval)
                    check =  sock.connect_ex((ip, port))
                    if check == 0:
                        total_port += 1
                        print (F.BLUE+f"[✓]Port {port} Opened For {ip}")
                        sock.close()
                    else:
                        pass
                        sock.close()
                except:
                    break
            print (F.GREEN+f"[*]Total Port Opened for {ip} is : {total_port}")
            sock.close()
        except:
            print(F.RED+"[x]Server Not Reachable")



#------------------------------------------------------------------------------------------------------------------------------
    


   # single port scan
    def port_scan_sin(self, ip, port): #4
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            check = sock.connect_ex((ip, int(port)))
            if check == 0:
                print (F.BLUE+f"[✓]Port: {port} Opened")
                sock.close()
            else:
                print (F.BLUE+f"[x]Port: {port} Closed")
                sock.close()

        except:
            print (F.RED+"[x]An Error Occured, Internet Issue")
            sock.close()



#------------------------------------------------------------------------------------------------------------------------------



    # gather information about an ip address
    def ip_osint(self, ip):
        try:
            res = r.get(f"https://ipinfo.io/{ip}", timeout=5)
            fetch = res.json()
            for i in fetch.keys():
                if i != "readme":
                    print(f"{F.CYAN}[*]{i}:-->{F.GREEN}{fetch[i]}")
                else:
                    continue
        except:
            print(F.RED+"[x]Error Connecting To Server")



#------------------------------------------------------------------------------------------------------------------------------



   # converting binary to number
    def Bina_Num(self, binary, base): #5
        print (F.GREEN+"[%]Output"+F.BLUE)
        print (F.BLUE+str(int(binary, int(base))))


#------------------------------------------------------------------------------------------------------------------------------




    # converting number to binary
    def Num_Bina(self, num, base): #6
        num = int(num)
        base = int(base)
        print (F.GREEN+"[*]Output"+F.BLUE)
        print (F.BLUE+bin(num) [base: ])


#------------------------------------------------------------------------------------------------------------------------------



    #repair binary files with invalid byte
    def repair(self, file):
        try:
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



#------------------------------------------------------------------------------------------------------------------------------



    # convert alphabet to binary
    def Alpha_Bina(self, file):
        file = self.get_file(file)
        open_file = open(file, "r")
        data = open_file.read()
        open_file.close()
        save_data = ' '.join(format(ord(c), '08b') for c in data)
        s_file = file+".sbin"
        open_file = open(s_file, "w")
        open_file.write(save_data)
        print(F.CYAN+"[*]File Converted Successfully")
        open_file.close()


#------------------------------------------------------------------------------------------------------------------------------



    # convert binary to alphabet
    def Bina_Alpha(self, file):
        file = self.get_file(file)
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



#------------------------------------------------------------------------------------------------------------------------------


                    
            
    # get private ip address of a device
    def get_private_addr(self):
        interfaces = n.interfaces()
        for interface in interfaces:
            try:
                addresses = n.ifaddresses(interface)
                if n.AF_INET in addresses:
                    for addr in addresses[n.AF_INET]:
                        ip = addr['addr']
                        if ip.startswith('10.') or ip.startswith('172.') or ip.startswith('192.168.'):
                            return ip
            except ValueError:
                continue
        return "127.0.0.1"


#------------------------------------------------------------------------------------------------------------------------------


   

   # get device network details and interfaces
    def get_device_ip(self):
        try:
            response = r.get('https://api.ipify.org?format=json', timeout=2)
            ip_data = response.json()
            print(F.CYAN+"[*]Interface: - Public Address -")
            print(F.WHITE+"-- addr: ",ip_data['ip'])
            print("—"*50)
        except r.RequestException:
            print(F.CYAN+"[*]Interface: - Public Address -")
            print(F.WHITE+"-- addr: ", "Network Not Reachable")
            print("—"*50)
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
            print("—"*50)


#------------------------------------------------------------------------------------------------------------------------------    



   
    # get device cpu information
    def cpu_info(self): #10
        print (F.BLUE+"[*]Cpu Details: ctrl+c To Exit")

        while True:

            cpu_p = F.GREEN+str(p.cpu_percent())+'%'
            cpu_us =F.GREEN+str(p.cpu_count(logical=False))
            cpu_l = F.GREEN+str(p.cpu_count(logical=True))

            ram = p.virtual_memory()
            disk = p.disk_partitions()[0]
            d_usage = p.disk_usage(disk.mountpoint)

            total_ram = F.BLUE+str((ram.total // (1024 ** 2))//1024)

            ram_used = F.BLUE+str((ram.used // (1024 ** 2)) // 1024)

            cu = F.CYAN+'Cpu Usage'
            co = F.CYAN+'Cpu Cores'
            cl = F.CYAN+'Logical Cores'
            ra = F.CYAN+'Ram:'


            print (f'{cu}:{cpu_p} | {co}:{cpu_us} | {cl}:{cpu_l} | A-{ra}:{ram_used}/{total_ram}Gb', end='\r', flush=True)
            tm.sleep(0.5)



#------------------------------------------------------------------------------------------------------------------------------



   # open server for wifi chat room
    def open_server(self): #11
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(100)
        #sock = socket.socket()
        print (F.CYAN+"[Note]: Only Support Wlan")
        print(F.CYAN+"......: To Close Chat: @bye")

        tm.sleep(1)
        a1, a2, a3 = str(rd.randint(1,6)), str(rd.randint(1,6)), str(rd.randint(1,5))
        ip = self.get_private_addr()
        port = a3+a2+a1+a2+a3
        print (F.BLUE+"[✓]Server Started")
        tm.sleep(1)
        print (F.GREEN+f"[*]Ip: {ip}  [*]Port: {port}")
    
        sock.bind(("0.0.0.0", int(port)))
        sock.listen(5)
        c, addr = sock.accept()

        while True:
            sen = input(F.CYAN+"[%]Send-Message: "+F.WHITE)
            c.send(sen.encode())
            print (F.BLUE+"[✓]Message Sent")
            print (F.GREEN+"[*]Waiting For Incoming Message")
            if sen == "@bye":
                tm.sleep(1)
                print (F.RED+"[*]Closing Chat")
                c.close()
                break
            rec = c.recv(20480).decode()
            print (F.CYAN+"[*]Received-Message: ",F.WHITE+rec)
            if rec == "@bye":
                tm.sleep(1)
                print (F.RED+"[*]User Closed Chat")
                c.close()
                break


#------------------------------------------------------------------------------------------------------------------------------



    # connect to wifi chat room server
    def connect_server(self, ip, port): #12
         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         sock.connect((ip, int(port)))
            
         print (F.BLUE+"[✓]Connected To Server")
         print (F.CYAN+"[Note]: Only Support Wlan")
         print(F.CYAN+"......:  To Close Chat: @bye")
         tm.sleep(1)
         while True:
             print(F.GREEN+"[*]Waiting For Incoming Message")
             rec = sock.recv(20480).decode()
             print (F.CYAN+"[*]Recieved-Message: "+F.WHITE+rec)
             if rec == "@bye":
                 tm.sleep(1)
                 print(F.RED+"[*]User Closed Chat")
                 sock.close()
                 break
             sen = input(F.CYAN+"[%]Send-Message: "+F.WHITE)
             sock.send(sen.encode())
             print (F.BLUE+"[✓]Message Sent")
             if sen == "@bye":
                 print (F.RED+"[*]Closing Chat")
                 tm.sleep(1)
                 sock.close()
                 break


#------------------------------------------------------------------------------------------------------------------------------




    # generate key for encryption
    def key(self, num):
        data = str(uuid.uuid4()).replace(':', '')[:num].replace('-', 'f')
        return data


#------------------------------------------------------------------------------------------------------------------------------

        
     
    # get file size and format   
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


#------------------------------------------------------------------------------------------------------------------------------


        
    # glob for file search
    def get_file(self, file):
        path = file
        matches = glob.glob(path)
        if matches:
            if len(matches) == 1:
                check = matches[0]
                return check.replace("'", "")
            else:
                print(F.RED+"[x] Multiple Entry Found")
                return False
        else:
            check = file
            return check.replace("'", "")


#------------------------------------------------------------------------------------------------------------------------------      




   # file utilities
    def file_sys(self, option, file): #13
        if option == "-c":
            if exists(file) == False:
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
                data = input(F.YELLOW+"[%]Enter Data: "+F.WHITE)
                open_file = open(file, "a")
                open_file.write(data)
                open_file.close()
                print (F.BLUE+"[✓]Done".upper())
            else:
                print (F.RED+"[x]File Doesn't Exist".uppper())


        elif option == "-d":
            os = self.os
            file = self.get_file(file)
            if not file:
                return False
            if exists(file):
                os.remove(file)
                print (F.BLUE+"[✓]File Deleted ".upper())
            else:
                print (F.RED+"[x]File Doesn't Exist".upper())


        elif option == "-v":
            file = self.get_file(file)
            print(file)
            if not file:
                return False
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
                    
            else:
                print (F.RED+"[x]No Such File Or Directory")
                
                
        elif option == "-r":
            file = self.get_file(file)
            if not file:
                return False
            os = self.os

            if exists(file):
                print(F.BLUE+"[*]File.Content:"+F.WHITE+"")
                try:
                    open_file = open(file, "r")
                    buffer = 1024
                    while True:
                        data = open_file.read(buffer)
                        print(data, end="")
                        if not data:
                            break
                    
                except:
                    open_file = open(file, 'rb')
                    buffer = 1024
                    while True:
                        data = open_file.read(buffer)
                        print(data, end="")
                        if not data:
                            break
            else:
                print (F.RED+"[x]File Doesn't Exist")


        elif option == "-ed":
            os = self.os
            file = self.get_file(file)
            if not file:
                return False
            if exists(file) and os.path.isfile(file):
                reg = file.endswith(".enc")
                if reg == True:
                    print (F.GREEN+"[*]File Is In Encrypted Format!!\n[*]Wish To Decrypt")
                    opt = input(F.YELLOW+"[?]Y/N: "+F.WHITE).upper()
                    if opt == "Y":
                        #decryption here
                        print(F.BLUE+"[Note]: Key Must Be EITHER 16, 24 Or 32 Bytes Character\n[*]Meaning Your Key Should Be ↑Above↑ Bytes Character Long")
                        key = input(F.CYAN+"[%]KEY: "+F.WHITE)
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

                        else:
                            print (F.RED+"[x]Invalid Key Byte Size Or No key Detected")

                    elif opt == "N":
                        print (F.BLUE+"[✓]File Was Maintained")

                    else:
                        print (F.RED+"[x]Error, Invalid Input")

                elif reg == False:
                    print (F.GREEN+"[*]File Is In Decrypted Format!!\n[*]Wish To Encrypt")
                    opt = input(F.YELLOW+"[?]Y/N: "+F.WHITE).upper()
                    if opt == "Y":
                        #encryption here
                        print(F.BLUE+"[*]Note: Key Must Be Either 16, 24 OR 32 Bytes Character\n[*]Meaning Your Key Should Be ↑Above↑ Bytes Character Long")
                        option = input(F.CYAN+"[?]Generate Key [Y/N]: ").upper()
                        if option == "Y":
                            num = int(input(F.YELLOW+'[%]Key Length: '))
                            keyD = self.key(num)
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

                            tm.sleep(0.6)
                            key_file = open("key.txt", "a")
                            cur_dir = os.getcwd()
                            data = "[Filnename= "+file+" :Key= "+keyD+" ]\n"
                            key_file.write(data)
                            print(f"{F.CYAN}[*]Key Saved On {F.YELLOW}{cur_dir}/{F.WHITE}key.txt")
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


#------------------------------------------------------------------------------------------------------------------------------          




    # send message to a whatsapp contact
    def send_mess(self, number): #14
        message = input(F.YELLOW+"[%]Message: "+F.WHITE).replace(" ", "%20")
        sys(f'xdg-open https://wa.me/{number}?text={message}')
        print (F.BLUE+"[*]Opening Whatsapp....")


        
#------------------------------------------------------------------------------------------------------------------------------



   # send file via wifi or localhost
    def send_file(self): #15
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(100)
        a1, a2, a3 = str(rd.randint(1,6)), str(rd.randint(1,6)), str(rd.randint(1,5))
        port = a3+a2+a1+a2+a3
        sock.bind(('0.0.0.0', int(port)))
        print (F.BLUE+"[✓]Server Started")
        ip = self.get_private_addr()
        print(F.GREEN+f'[*]Ip: {ip} [*]Port: {port}'+F.CYAN)

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

            c, addr = sock.accept()
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
            else:
                print(F.CYAN+"[x]Reciever Aborted")
                c.close()
        else:
            print(F.RED+"[x]Error: Empty Input")


#------------------------------------------------------------------------------------------------------------------------------






   # recieve file via wifi or localhost
    def recv_file(self, ip, port): #16
        c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        c_socket.connect((ip, int(port)))
        print(F.CYAN+"[✓]Connected To Server")
        #tm.sleep(1)
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
                                c_socket.close()
                            new_file.write(bytes(rec))
                            progress_bar.update(len(rec))
                c_socket.close()
                print (F.BLUE+"[✓]File Downloaded")
            elif choice == "N":
                c_socket.send("...".encode())
                print(F.CYAN+"[*]Aborted")
                c_socket.close()
            else:
                c_socket.send("...".encode())
                print(F.RED+"[x]Invalid Input")
                c_socket.close()
        else:
            c_socket.send("...".encode())
            print(F.RED+"[x]Error: Empty Input")
            c_socket.close()


#------------------------------------------------------------------------------------------------------------------------------




    # open server for shell
    def shell_host(self): #17
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(100)
        tm.sleep(1)
        a1, a2, a3 = str(rd.randint(1,6)), str(rd.randint(1,6)), str(rd.randint(1,5))
        ip = self.get_private_addr()
        port = a3+a2+a1+a2+a3
        print(F.CYAN+"[Note]: Input <exit> To Close Session")
        print (F.BLUE+"[✓]Shell Host Started")
        tm.sleep(1)
        print (F.GREEN+f"[*]Ip: {ip}  [*]Port: {port}")

        sock.bind(("0.0.0.0", int(port)))
        sock.listen(5)
        c, addr = sock.accept()
        print (F.GREEN+"[✓]Client Connected")

        while True:
            data = input(F.CYAN+"\n[shell]•••→ "+F.WHITE)
            if data == "exit":
                c.send(data.encode())
                print(F.RED+"[*]Closing Shell")
                tm.sleep(1)
                c.close()
                break
            c.send(data.encode())
            rec = c.recv(51200).decode()
            print(F.WHITE+rec)



#------------------------------------------------------------------------------------------------------------------------------




   # connect to shell host
    def shell_client(self, ip, port): #18
        os = self.os
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, int(port)))
        print(F.BLUE+"[✓]Connected To User")
        tm.sleep(1)
        print(F.CYAN+"[*]Shell Activity In Progress")
        
        while True:
            data = sock.recv(1024).decode()
            if data == "exit":
                print (F.RED+"[*]Closing Shell")
                tm.sleep(1)
                sock.close()
                break
            elif data.startswith('cd '):
                path = data[3:]
                try:
                    os.chdir(path)
                    path = os.getcwd()
                    sock.send(f'~{path}'.encode())
                except:
                    sock.send("Invalid Directory".encode())
            else:
                decode_data = sub.getoutput(data)
                sock.send(f'|{decode_data}'.encode())


#------------------------------------------------------------------------------------------------------------------------------




    # encrypt a string 
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



#------------------------------------------------------------------------------------------------------------------------------




   # phone number osint
    def check_phone(self, number): #20
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




#------------------------------------------------------------------------------------------------------------------------------




    """vulnerability scanner
    def scan_vul(self, target): #21
        api_key = input(F.YELLOW+"[%]Api-Key : "+F.WHITE)
        secret_key = input(F.YELLOW+"[%]Secret-Key: "+F.WHITE)
        access_key = input(F.YELLOW+"[%]Access-Key: "+F.WHITE)

        api_url = 'https://cloud.tenable.com/api/v2/policies'
        headers = {
                'Content-Type': 'application/json',
                'X-ApiKeys': f'accessKey={access_key};secretKey={secret_key}'
                }

        try:
            response = r.get(api_url, headers)
            if response.status_code == 200:
                policies = response.json()

                for policy in policies['policies']:
                    policy_id = policy['policy_id']

                load = TenableIO(api_key=api_key, secret_key=secret_key)
                scan = load.scans.create("My Scan", targets=[target], policy_id=policy_id)
                scan.launch()

                while scan.status() != 'completed':
                    pass

                results = scan.results()
                print("\n")
                for vul in results['vulnerabilities']:
                    print(f"{F.BLUE}[*]Vulnerabilty: {F.GREEN}{vul['plugin_name']}\t{F.BLUE}[*]Severity: {F.GREEN}{vul['severity']}")
            
            else:
                data = response.text
                data = json.loads(data)
                print("\n")
                for keys in data.keys():
                    print(f"{F.RED}[x]{keys}: {data[keys]}")
        except requests.exceptions.RequestException as e:
            print(F.RE+"[x]Error Connecting To Host")"""


#------------------------------------------------------------------------------------------------------------------------------





   # check weather information of a city/country
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



#------------------------------------------------------------------------------------------------------------------------------




            
    # search a file        
    def search(self, directory, target_file):
        try:
            full_path = directory
            os = self.os
            items = os.listdir(directory)
            for item in items:
                full_path = os.path.join(directory, item)
                if os.path.isdir(full_path):
                    self.search(full_path, target_file)
            
                elif os.path.isfile(full_path) and item == target_file:
                    print(f"{F.GREEN}[✓]File Found: {F.WHITE}{full_path}")
                    self.search_counter()

        except FileNotFoundError:
            print(f"{F.RED}[x]Invalid Directory: {F.WHITE}{directory}")

        except NotADirectoryError:
            print(f"{F.RED}[x]Not A Directory: {F.WHITE}{full_path}")

        except PermissionError:
            print(f"{F.RED}[x]Permission Denied: {F.WHITE}{full_path}")


#------------------------------------------------------------------------------------------------------------------------------



    
    # search counter       
    def search_counter(self):
        self.count+= 1
        return self.count


#------------------------------------------------------------------------------------------------------------------------------



        
            
    # file search trigger        
    def trigger_search(self, directory):

        folder = "/data/data/com.termux" if directory == "/termux" else directory

        target__file = input(f"{F.BLUE}[%]File To Search:{F.WHITE} ").replace("'", "")
        
        if target__file:
            print("")
            self.search(folder, target__file)
            print(f"{F.CYAN}\n[*]File Occurence:{F.GREEN} {self.search_counter()-1}")
            self.count = 0
        else:
            print(F.RED+"[x]Error: Empty Input")



#------------------------------------------------------------------------------------------------------------------------------



    def check_rand(self, mac):
        try:
            mac = mac.replace('-', ':').lower()
            first_byte = mac.split(':')[0]
            first_byte_int = int(first_byte, 16)

            return bool(first_byte_int & 0b00000010)
        except:
            return False




#------------------------------------------------------------------------------------------------------------------------------
            
            
    def mac_lookup(self, mac):
        if not self.check_rand(mac):
            url = f"https://api.macvendors.com/{mac}"
        
            response = r.get(url)
            if response.status_code == 200:
                print(f"{F.CYAN}[*]Device Manufacturer: {F.WHITE}{response.text}")
            else:
                print(F.RED+"[x]No Mac Record Found")
        else:
            print(F.RED+"[x]Mac Is Locally Assigned [Not Lookable]")



#------------------------------------------------------------------------------------------------------------------------------
  


    def version(self):
        home = os.environ["HOME"]
        folder = f"{home}/Shell/__version__"
        open_file = open(folder, 'r')
        print(F.CYAN+open_file.read().strip())
        open_file.close()



#------------------------------------------------------------------------------------------------------------------------------



# relay for all tools
shark = shark()
if __name__ == '__main__':
    shark.main()
    memory = compute()
    while True:

#------------------------------------------------------------------------------------------------------------------------------

        data = inpu()

        def cons_(num):
            return ' '.join(data.split()[num:])
            
        try:
            #data = inpu()
            if '@help'in data:
                shark.help()
            elif "@get -i" in data: 
                shark.get_ip(data.split()[2])
            elif "@port -sm" in data:
                shark.port_scan(data.split()[2])
            elif "@port -sn" in data: 
                shark.port_scan_sin(data.split()[2], data.split()[3])
            elif "@bina -a" in data: 
                shark.Bina_Alpha(cons_(2))
            elif "@alpha -b" in data: 
                shark.Alpha_Bina(cons_(2))
            elif "@num -b" in data: 
                shark.Num_Bina(data.split()[2], data.split()[3])
            elif "@bina -n" in data: 
                shark.Bina_Num(data.split()[2], data.split()[3])
            elif "@ip -details" in data:
                shark.get_device_ip()

#------------------------------------------------------------------------------------------------------------------------------

            elif "@cpu" in data: 
                shark.cpu_info()
            elif "@open -server" in data: 
                shark.open_server()
            elif "@con -s" in data: 
                shark.connect_server(data.split()[2], data.split()[3])
            elif "@file" in data:
                    shark.file_sys(data.split()[1], cons_(2))
            elif "@send -w" in data:
                shark.send_mess(data.split()[2])
            elif "@send -file" in data: 
                shark.send_file()
            elif "@recv -f" in data: 
                shark.recv_file(data.split()[2], data.split()[3])
            elif data == "@shell -host":
                shark.shell_host()

#------------------------------------------------------------------------------------------------------------------------------

            elif "@shell -c" in data:
                shark.shell_client(data.split()[2], data.split()[3])
            elif "@crypt" in data: 
                shark.crypt()
            elif "@check -n" in data: 
                shark.check_phone(data.split()[2])
            elif "@check -w" in data: 
                shark.weather(data.split()[2])
            elif "@ip -s" in data:
                shark.ip_osint(data.split()[2])
            elif "@sch -f" in data:
                shark.trigger_search(cons_(2))
            elif "@sch -m" in data:
                shark.mac_lookup(data.split()[2])
            elif "@solve -res" in data:
                run()

#------------------------------------------------------------------------------------------------------------------------------

            elif "@version" in data:
                shark.version()
            elif "@shark" in data:
                memory.update({data.split("=")[0].split()[1]: data.split("=")[1]})
            elif "@clone" in data:
                if data.split()[2] == "file":
                    clone_alias(True)
                    print(F.RED+"[!]Cloned: Restart The Shell For Update To Take Effect")
                elif data.split()[2] == "mem":
                    memory.update(clone_alias(False))

            elif "@exit" in data: 
                print (F.RED+"[✓]Exiting Program...")
                break

#------------------------------------------------------------------------------------------------------------------------------

            elif data.lstrip().startswith('cd') and "cd" != data.strip():
                d_path = ' '.join(filter(None, data.split()))
                path = d_path[3:]
                matches = glob.glob(path)
                if matches:
                    if len(matches) == 1:
                        os.chdir(matches[0])
                    else:
                        print(F.RED+"[x] Multiple Entry Found")
                else:
                    print (f"cd:{path}: No Such File Or Directory")
            elif data.strip() == 'cd':
                os.chdir(os.path.expanduser("~"))
            elif data == "@update":
                print(trigger_software_update())

#------------------------------------------------------------------------------------------------------------------------------

            else:
                for alias in memory.keys():
                    if data.split()[0] == alias:
                        data = data.split()[0].replace(alias, memory[alias].strip()) +' '+' '.join(data.split()[1:])
                sys(data)

        except FileNotFoundError as er:
            print(F.RED+"[x]",er)
        except IsADirectoryError as er:
            print(F.RED+"[x]",er)

#------------------------------------------------------------------------------------------------------------------------------

        except ValueError as er:
            print(F.RED+"[x]",er)
        except PermissionError as er:
            print(F.RED+"[x]",er)
        except socket.error as er:
            print(F.RED+"[x]",er)
        except socket.timeout as er:
            print(F.RED+"[x]",er)
        except socket.gaierror as er:
            print(F.RED+"[x]",er)
        except NameError as er:
            print(F.RED+"[x]",er)
        except UnboundLocalError as er:
            print(F.RED+"[x]",er)
        except KeyboardInterrupt:
            pass
        except IndexError as er:
            print(F.RED+"[x]",er)
        except:
            print(F.RED+"[x]An Error Occured")


#------------------------------------------------------------------------------------------------------------------------------
# end line 1359
