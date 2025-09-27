#------------------------------------------------------------------------------------------------------------------------------

import asyncio
import os
import re
import shutil
import time
from typing import List, Optional, Tuple
from colorama import Fore


#------------------------------------------------------------------------------------------------------------------------------



CONCURRENCY = 500
MIN_TIMEOUT = 0.8
MAX_TIMEOUT = 10.0
BASE_OVERHEAD = 0.6 
SCALE_DIVISOR = 1000.0
PRIORITY_PORTS = [80, 443, 22, 21, 25, 53, 8080, 8443]


#------------------------------------------------------------------------------------------------------------------------------

async def async_ping(host: str, cmd_timeout: float = 2.0) -> Optional[float]:

    ping_path = shutil.which("ping")
    if not ping_path:
        return None

    candidates = [
        [ping_path, "-c", "1", "-W", "1", host],
        [ping_path, "-c", "1", "-w", "1", host],
    ]
    for cmd in candidates:
        try:
            proc = await asyncio.create_subprocess_exec(
                *cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
            )
            stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout=cmd_timeout)
            out = (stdout or b"").decode(errors="ignore") + (stderr or b"").decode(errors="ignore")
            m = re.search(r"time=([\d\.]+)\s*ms", out, re.IGNORECASE)
            if m:
                return float(m.group(1)) / 1000.0
            m2 = re.search(r"time=([\d\.]+)", out, re.IGNORECASE)
            if m2:
                val = float(m2.group(1))
                return val / 1000.0 if val > 5 else val
        except asyncio.TimeoutError:
            continue
        except Exception:
            continue
    return None


#------------------------------------------------------------------------------------------------------------------------------

async def tcp_rtt_estimate(host: str, port: int = 80, timeout: float = 1.0) -> Optional[float]:

    loop = asyncio.get_event_loop()
    t0 = loop.time()
    try:
        conn = asyncio.open_connection(host, port)
        reader, writer = await asyncio.wait_for(conn, timeout=timeout)
        elapsed = loop.time() - t0
        writer.close()
        await writer.wait_closed()
        return elapsed
    except Exception:
        return None

#------------------------------------------------------------------------------------------------------------------------------



def compute_timeout_from_rtt(rtt: Optional[float], n_ports: int) -> float:

    rtt_val = rtt if (rtt is not None and rtt > 0) else 0.15
    scale = 1.0 + min(8.0, (n_ports / SCALE_DIVISOR))
    timeout = rtt_val * scale + BASE_OVERHEAD
    if timeout < MIN_TIMEOUT:
        timeout = MIN_TIMEOUT
    if timeout > MAX_TIMEOUT:
        timeout = MAX_TIMEOUT
    return timeout


#------------------------------------------------------------------------------------------------------------------------------



async def scan_port(host: str, port: int, semaphore: asyncio.Semaphore, timeout: float) -> Tuple[int, bool]:

    async with semaphore:
        try:
            conn = asyncio.open_connection(host, port)
            reader, writer = await asyncio.wait_for(conn, timeout=timeout)
            writer.close()
            await writer.wait_closed()
            return port, True
        except Exception:
            return port, False


#------------------------------------------------------------------------------------------------------------------------------



async def scan(host: str, ports: List[int], concurrency: int = CONCURRENCY):
    ports = sorted(set(ports))
    n_ports = len(ports)

    ping_rtt = await async_ping(host)
    if ping_rtt is None:
        ping_rtt = await tcp_rtt_estimate(host, port=80, timeout=1.0)
    if ping_rtt is None:
        ping_rtt = 0.15 

    timeout = compute_timeout_from_rtt(ping_rtt, n_ports)
    semaphore = asyncio.Semaphore(concurrency)

    print(f"\n{Fore.YELLOW}[!]STARTED: SCANNING {Fore.GREEN}{n_ports}{Fore.YELLOW} ports for {Fore.GREEN}{host}")
    print(f"{Fore.YELLOW}[!]RTT estimate: {Fore.GREEN}{ping_rtt:.3f}s{Fore.YELLOW} -> per-connection timeout: {Fore.GREEN}{timeout:.2f}s\n")
    start = time.time()

    priority = [p for p in PRIORITY_PORTS if p in ports]
    remaining = [p for p in ports if p not in priority]

    open_ports = []

    async def run_batch(port_list: List[int], batch_name: str = "batch"):
        if not port_list:
            return []
        tasks = [asyncio.create_task(scan_port(host, p, semaphore, timeout)) for p in port_list]
        results = await asyncio.gather(*tasks)
        found = []
        for p, ok in results:
            if ok:
                found.append(p)
                print(f"{Fore.BLUE}[✓]Port: {Fore.GREEN}{p} Open")
        return found



#------------------------------------------------------------------------------------------------------------------------------


    if priority:
        found = await run_batch(priority, "priority")
        open_ports.extend(found)

    if remaining:
        found = await run_batch(remaining, "main")
        open_ports.extend(found)

    elapsed = round(time.time() - start, 2)
    print(f"\n{Fore.YELLOW}[*]SCANNED {Fore.GREEN}{n_ports}{Fore.YELLOW} ports in {Fore.GREEN}{elapsed}{Fore.YELLOW} seconds")
    print(f"{Fore.BLUE}[*]Total Port Opened For {host}: {Fore.CYAN}{len(open_ports)}")
    print(f"{Fore.BLUE}[*]Total Port Closed For {host}: {Fore.CYAN}{n_ports - len(open_ports)}")

    return open_ports


#------------------------------------------------------------------------------------------------------------------------------




def load_ports_from_file(file_path: str) -> List[int]:
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



def run_port(host: str, port_range: str = "default"):
    if port_range == "default":
        file_path = f"{os.environ['HOME']}/Shell/UTILS/.ports"
        ports = load_ports_from_file(file_path)
    else:
        if "," in port_range:
            tokens = [tok.strip() for tok in port_range.split(",")]
            ports = []
            for tok in tokens:
                if "-" in tok:
                    a, b = tok.split("-", 1)
                    ports.extend(range(int(a), int(b) + 1))
                else:
                    ports.append(int(tok))
        elif "-" in port_range:
            a, b = port_range.split("-", 1)
            ports = list(range(int(a), int(b) + 1))
        else:
            ports = [int(port_range)]

    if not ports:
        print(Fore.RED + "[x]No ports to scan.")
        return

    try:
        asyncio.run(scan(host, ports))
    except KeyboardInterrupt:
        print(Fore.RED + "\n[!]Scan interrupted by user.")

#------------------------------------------------------------------------------------------------------------------------------
#end line 219
