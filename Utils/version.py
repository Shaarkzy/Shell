
#------------------------------------------------------------------------------------------------------------------------------

try:
    import requests as req
    from requests.exceptions import RequestException
    import os
    import base64
    import socket
    import subprocess as sub
except Exception as e:
    print(f'[x]Error: {e}')
    quit(0)

#------------------------------------------------------------------------------------------------------------------------------

github_raw_version = "https://api.github.com/repos/Shaarkzy/Shell/contents/__version__?ref=main"

home = os.environ["HOME"]
local_raw_version = f"{home}/Shell/Data/__version__"

#------------------------------------------------------------------------------------------------------------------------------

def is_connected(host="8.8.8.8", port=53, timeout=0.5):

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        sock.connect((host, port))
        sock.close()
        return True

    except socket.error:
        return False

#------------------------------------------------------------------------------------------------------------------------------

def get_github():
    if is_connected():
        try:
            response = req.get(github_raw_version, timeout=3)
            if response.status_code == 200: 
                file_cont = response.json()
                content = base64.b64decode(file_cont['content']).decode('utf-8')
                return content.strip()
            else:
                return False
        except RequestException:
            return False
    else:
        return False

#------------------------------------------------------------------------------------------------------------------------------

def compute(data):
    try:
        if data == False:
            return False
        sp = data.split(".")
        _, year, month, day, hr, mi = sp

        year = int(year) * 365 * 86400
        month = int(month) * 30 * 86400
        day = int(day) * 24 * 3600
        hr = int(hr) * 60 * 60
        mi = int(mi) * 60

        computed = year + month + day + hr + mi
        return computed
    except Exception as e:
        print(f'[x]Error: {e}')
        quit(0)

#------------------------------------------------------------------------------------------------------------------------------

def get_local():
    open_file = open(local_raw_version, "r")
    return open_file.read().strip()


def check():
    git_val = compute(get_github())
    local_val = compute(get_local())

    
    if git_val != False:
        if git_val <= local_val:
            return False
        else:
            return get_github()
    else:
        return 'null_internet'

#------------------------------------------------------------------------------------------------------------------------------
#end line 94