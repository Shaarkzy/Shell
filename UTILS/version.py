
#------------------------------------------------------------------------------------------------------------------------------

try:
    import requests as req
    from requests.exceptions import RequestException
    import os
    from .check_os import detect_os
    import base64
    import socket
    import subprocess as sub
except ImportError:
    pass
    quit(0)

#------------------------------------------------------------------------------------------------------------------------------

github_raw_version = "https://api.github.com/repos/Shaarkzy/Shell/contents/__version__?ref=main"

if detect_os():
    local_raw_version = '/data/data/com.termux/files/home/Shell/__version__'
else:
    user = sub.getoutput('whoami')
    local_raw_version = "/root/Shell/__version__" if os.geteuid() == 0 else f'/home/{user}/Shell/__version__' 


#------------------------------------------------------------------------------------------------------------------------------



def is_connected(host="8.8.8.8", port=53, timeout=3):

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



def get_local():
    open_file = open(local_raw_version, "r")
    return open_file.read().strip()


try:
    def check():
        check_git = get_github()
        check_local = get_local()

    
        if check_git != False:
            if check_git == check_local:
                return False
            else:
                return check_git
        else:
            return 'null_internet'

except:
    quit(0)


#------------------------------------------------------------------------------------------------------------------------------
#end line 93

