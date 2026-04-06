
#------------------------binary implemenetations and manipulation---------------------------------

def netmask_(prefix) -> str: #24 -> 11111111111111111111111100000000
    default = 0b11111111111111111111111111111111
    netmask_bit = default << (32 - int(prefix)) & 0xFFFFFFFF
    return format(netmask_bit, '032b')

#----------------------------------------------------------------------------------------------------

def wildcard_(prefix) -> str: #24 -> 00000000000000000000000011111111
    default = 0b11111111111111111111111111111111
    wildcard_bit = default >> (int(prefix)) & 0xFFFFFFFF
    return format(wildcard_bit, '032b')

#----------------------------------------------------------------------------------------------------

def convert_dec_bin(dec_value) -> str: #255.255.255.255 -> 111111111.11111111.11111111.11111111
    bin_value = '.'.join(format(int(val), '08b') for val in dec_value.split('.'))
    return bin_value

#----------------------------------------------------------------------------------------------------

def convert_bin_dec(bin_value) -> str: #11111111.11111111.11111111.11111111 -> 255.255.255.255
    dec_value = '.'.join(str(int(val, 2) & 0xFF) for val in bin_value.split('.'))
    return dec_value

#----------------------------------------------------------------------------------------------------

def convert_octect_32bin(bin_value) -> str: #11111111.11111111.11111111.11111111 -> 11111111111111111111111111111111
    return bin_value.replace('.', '')

#----------------------------------------------------------------------------------------------------

def convert_32bin_octet(_32bin) -> str: #11111111111111111111111111111111 -> 11111111.11111111.11111111.11111111
    num = 0
    bin32 = []
    _32bin = _32bin.strip()
    for i in range(4):
        for j in range(8):bin32.append(_32bin[num]);num += 1
        if num < 32:bin32.append('.')
    return ''.join(bin32)

#----------------------------------------------------------------------------------------------------

def convert_int_bin(int_value, formatted) -> bin: #255, 08b -> 11111111
    return format(int_value, formatted)

#--------------------------------------outputs------------------------------------------------------

def print_result(ip_, prefix_, F) -> str: # output
    global ip
    global prefix
    ip = ip_
    prefix = prefix_
    data = f'''
{F.CYAN}[~] Address            : {F.WHITE}{ip_address()}
{F.CYAN}[~] Netmask            : {F.WHITE}{netmask()}
{F.CYAN}[~] Wildcard           : {F.WHITE}{wildcard()}
{F.CYAN}[~] Network            : {F.WHITE}{network()}
{F.CYAN}[~] Type               : {F.WHITE}{type_()}
{F.CYAN}[~] Class              : {F.WHITE}{class_()}
{F.CYAN}[~] Max Address        : {F.WHITE}{max_address()}
{F.CYAN}[~] Max Host           : {F.WHITE}{max_host()}
{F.CYAN}[~] First Usable Ip    : {F.WHITE}{first_ip()}
{F.CYAN}[~] Last Usable Ip     : {F.WHITE}{last_ip()}
{F.CYAN}[~] Broadcast Ip       : {F.WHITE}{broadcast()}
'''
    return data

#-----------------------------------network calculation----------------------------------------------
#                     Using network 10.10.10.10/24 for illustration

def ip_address() -> str: # 10.10.10.10
    global ip
    return ip

#----------------------------------------------------------------------------------------------------

def netmask() -> str: #255.255.255.0
    global prefix
    net_ = netmask_(prefix)
    octet_net = convert_32bin_octet(net_)
    dec_octet = convert_bin_dec(octet_net)
    return dec_octet

#----------------------------------------------------------------------------------------------------

def wildcard() -> str: #0.255.255.255
    global prefix
    wild_ = wildcard_(prefix)
    octet_wild = convert_32bin_octet(wild_)
    dec_octet = convert_bin_dec(octet_wild)
    return dec_octet

#----------------------------------------------------------------------------------------------------

def network() -> str: #10.10.10.10/24
    global prefix
    ip_ = ip_address()
    netmask_ = netmask()
    ip_bin = convert_octect_32bin(convert_dec_bin(ip_))
    netmask_bin = convert_octect_32bin(convert_dec_bin(netmask_))
    ip_int = int(ip_bin, 2)
    netmask_int = int(netmask_bin, 2)
    compute_ = convert_int_bin(ip_int & netmask_int, '032b')
    final_ = convert_bin_dec(convert_32bin_octet(compute_))+'/'+prefix
    return final_

#----------------------------------------------------------------------------------------------------
def type_() -> str: #private
    global ip
    parts = list(map(int, ip.split('.')))
    if parts[0] == 10:return "Private"
    if parts[0] == 172 and 16 <= parts[1] <= 31:return "Private"
    if parts[0] == 192 and parts[1] == 168:return "Private"
    return "Public"

#----------------------------------------------------------------------------------------------------

def class_() -> str: #A
    global ip
    try:
        first = int(ip.split('.')[0])
        if first == 127:return "Loopback"
        if first == 0:return "Reserved"
        if 1 <= first <= 126:return "A"
        if 128 <= first <= 191:return "B"
        if 192 <= first <= 223:return "C"
        if 224 <= first <= 239:return "D (multicast)"
        if 240 <= first <= 255:return "E (reserved)"
        return "Invalid"
    except:return "Invalid"

#----------------------------------------------------------------------------------------------------

def max_address() -> int: #256
    global prefix
    return 2**(32 - int(prefix))

#----------------------------------------------------------------------------------------------------

def max_host() -> int: #254
    global prefix
    if prefix == '32': return 1
    if prefix == '31': return 2
    max_h = (2**(32 - int(prefix))) - 2
    return max_h

#----------------------------------------------------------------------------------------------------

def first_ip() -> str: #10.10.10.1
    ip_ = ip_address()
    netmask_ = netmask()
    ip_bin = convert_octect_32bin(convert_dec_bin(ip_))
    netmask_bin = convert_octect_32bin(convert_dec_bin(netmask_))
    ip_int = int(ip_bin, 2)
    netmask_int = int(netmask_bin, 2)
    x = 0 if prefix == "32" or prefix == '31' else 1
    compute_ = convert_int_bin((ip_int & netmask_int) + x, '032b')
    return convert_bin_dec(convert_32bin_octet(compute_))

#----------------------------------------------------------------------------------------------------

def last_ip() -> str: #10.10.10.254
    ip_ = ip_address()
    wildcard_ = wildcard()
    ip_bin = convert_octect_32bin(convert_dec_bin(ip_))
    wildcard_bin = convert_octect_32bin(convert_dec_bin(wildcard_))
    ip_int = int(ip_bin, 2)
    wildcard_int = int(wildcard_bin, 2)
    x = 0 if prefix == "32" or prefix == '31' else 1
    compute_ = convert_int_bin((ip_int | wildcard_int) - x, '032b')
    return convert_bin_dec(convert_32bin_octet(compute_))

#----------------------------------------------------------------------------------------------------

def broadcast() -> str: #10.10.10.255
    ip_ = ip_address()
    wildcard_ = wildcard()
    ip_bin = convert_octect_32bin(convert_dec_bin(ip_))
    wildcard_bin = convert_octect_32bin(convert_dec_bin(wildcard_))
    ip_int = int(ip_bin, 2)
    wildcard_int = int(wildcard_bin, 2)
    compute_ = convert_int_bin((ip_int | wildcard_int), '032b')
    return convert_bin_dec(convert_32bin_octet(compute_))

#---------------------------------------------------------------------------------------------------- 
#end line 188