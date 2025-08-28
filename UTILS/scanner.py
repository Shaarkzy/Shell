#------------------------------------------------------------------------------------------------------------------------------

import asyncio
import subprocess
import re
import os
from colorama import Fore
import time

#------------------------------------------------------------------------------------------------------------------------------

def ping(ip):

    output = subprocess.getoutput(f'ping -w 1 {ip} ')
    try:
        re_search = re.search(r'time=([\d.]+)', output)
        ping = float(re_search.group(1))/1000
        return ping
    except: return "null"



#------------------------------------------------------------------------------------------------------------------------------


async def scan_port(ip: str, port: int, leng: int, ping: int):

    x, y, k, m, n = int(leng/500), ping, 48.4, 1, 1.767
    timeout = k * (x**m) * (y**n)
    timeout = timeout if timeout >= 1 else 1

    semaphore = asyncio.Semaphore(500) 
    async with semaphore:
        try:
            conn = asyncio.open_connection(ip, port)
            reader, writer = await asyncio.wait_for(conn, timeout=timeout)
            writer.close()
            await writer.wait_closed()
            return port, True
        except Exception:
            return port, False

#------------------------------------------------------------------------------------------------------------------------------


async def scan(ip: str, ports: list):

    timeout = ping(ip)
    total_opened = 0
    total_closed = 0
    total = 0
    if timeout == "null": print(Fore.RED+"\n[x]Host Unreachable"); pass
    else:
        leng = len(ports)
        x, y, k, m, n = int(leng/500), timeout, 48.4, 1, 1.767
        interval = k * (x**m) * (y**n)
        interval = round(interval, 2) if interval >= 1 else 1.01
        print(f'\n{Fore.YELLOW}[!]STARTED: SCANNING {Fore.GREEN}{leng} {Fore.YELLOW}Ports : ETS {Fore.GREEN}{interval}{Fore.YELLOW} seconds\n')
        start_time = time.time()
        tasks = [scan_port(ip, port, leng, timeout) for port in ports]
        results = await asyncio.gather(*tasks)
    
        for port, status in results:
            if status:
                total_opened += 1
                print(f"{Fore.BLUE}[✓]Port: {Fore.GREEN}{port} Opened")
            else:
                total_closed += 1
                pass
            total += 1
        end_time = time.time()
        elapsed = f'{round((end_time - start_time), 2)}{Fore.YELLOW} seconds'

        print(f'\n{Fore.YELLOW}[*]SCANNED {Fore.GREEN}{total}{Fore.YELLOW} Ports in {Fore.GREEN}{elapsed}')
        print(f"{Fore.BLUE}[*]Total Port Opened For {ip}: {Fore.CYAN}{total_opened}")
        print(f"{Fore.BLUE}[*]Total Port Closed For {ip}: {Fore.CYAN}{total_closed}")


#------------------------------------------------------------------------------------------------------------------------------


def ex_text_ports():

    home = os.environ["HOME"]
    file = f"{home}/Shell/UTILS/.ports"
    open_file = open(file, "r")
    
    lines = open_file.readlines()
    length = len(lines)
    open_file.close()

    count = 0
    ports = []
    for i in range(length):
        data = lines[count]
        count += 1

        split_data = data.split(",")
        count_1 = 0

        for port in split_data:
            if "-" in port:
                split_port = port.split("-")
                start = split_port[0]
                end = split_port[1]

                for n_port in range(int(start), int(end)+1):
                    ports.append(n_port)
            else:
                ports.append(port)


    ex_ports = []
    for p in ports:
        try:
            if str(p).strip() != "":
                ex_ports.append(int(str(p).strip()))
        except ValueError:
            pass

    return ex_ports


#------------------------------------------------------------------------------------------------------------------------------


def run_port(ip: str, port_range):

    if port_range == "default":
        asyncio.run(scan(ip, ex_text_ports()))
    else:
        ex_ports = []
        ports = port_range.split("-")
        start = ports[0]
        end = ports[1]

        for port in range(int(start), int(end)+1):
            ex_ports.append(int(port))

        asyncio.run(scan(ip, ex_ports))


#------------------------------------------------------------------------------------------------------------------------------
#end line 143
