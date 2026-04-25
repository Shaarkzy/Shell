
#------------------------------------------------------------------------------------------------------------------------------

import asyncio
import os
import time
from colorama import Fore

#------------------------------------------------------------------------------------------------------------------------------

count = 0
def counter():
    global count
    count += 1
    return count

#------------------------------------------------------------------------------------------------------------------------------

async def check_port(sem, ip, port, timeout=5.0):
    async with sem:
        try:
            reader, writer = await asyncio.wait_for(
                asyncio.open_connection(ip, port),
                timeout=timeout
            )
            print(f"{Fore.BLUE}[*]OPENED: {Fore.CYAN}{port}")
            counter()

            writer.close()
            await writer.wait_closed()
        except (ConnectionRefusedError, OSError, asyncio.TimeoutError):
            pass

#------------------------------------------------------------------------------------------------------------------------------

async def scan_ports(ip, ports, concurrency=10000):
    global count
    sem = asyncio.Semaphore(concurrency)
    n_ports = len(ports)
    print(f"{Fore.GREEN}[*]Scanning {Fore.YELLOW}{n_ports} {Fore.GREEN}ports")

    tasks = [
        asyncio.create_task(check_port(sem, ip, port))
        for port in ports
    ]
    
    await asyncio.gather(*tasks)

    print(f"{Fore.GREEN}[*]Total Port Opened For {ip}: {Fore.CYAN}{count}")
    print(f"{Fore.GREEN}[*]Total Port Closed For {ip}: {Fore.RED}{n_ports - count}")
    count = 0

#------------------------------------------------------------------------------------------------------------------------------

def load_ports_from_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Ports file not found: {file_path}")
    with open(file_path, "r") as f:
        content = f.read()
    tokens = [t.strip() for t in content.replace("\n", ",").split(",") if t.strip()]
    ports = []
    for t in tokens:
        if "-" in t:
            a, b = t.split("-", 1)
            ports.extend(range(int(a), int(b) + 1))
        else:
            ports.append(int(t))
    return sorted(set(ports))

#------------------------------------------------------------------------------------------------------------------------------

def run_port(host, port_range):
    if port_range == "default":
        file_path = f"{os.environ['HOME']}/Shell/Data/ports"
        ports = load_ports_from_file(file_path)
    else:
        if "," in port_range:
            tokens = [tok.strip() for tok in port_range.split(",")]
            ports = []
            for tok in tokens:
                if "-" in tok:
                    a, b = tok.split("-", 1)
                    b = '65535' if int(b) > 65535 else b
                    ports.extend(range(int(a), int(b) + 1))
                else:
                    ports.append(int(tok))
        elif "-" in port_range:
            a, b = port_range.split("-", 1)
            b = '65535' if int(b) > 65535 else b
            ports = list(range(int(a), int(b) + 1))
        else:
            ports = [int(port_range)]

    if not ports:
        print(Fore.RED + "[x]No ports to scan.")
        return

    try:
        start = time.perf_counter()
        asyncio.run(scan_ports(host, ports))
        end = time.perf_counter()
        elapsed = end - start
        print(f"{Fore.WHITE}[*]Elapsed Time: {Fore.YELLOW}{elapsed:.3f} {Fore.WHITE}seconds")
    except KeyboardInterrupt:
        print(Fore.RED + "\n[!]Scan interrupted by user.")

#------------------------------------------------------------------------------------------------------------------------------
#end line 107