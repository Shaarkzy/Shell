#------------------------------------------------------------------------------------------------------------------------------


import requests
import re
from bs4 import BeautifulSoup 


#------------------------------------------------------------------------------------------------------------------------------

def check_site(domain):
    base_url = "https://www.isitdownrightnow.com/check.php"
    check_url = f"{base_url}?domain={domain}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Referer": "https://www.isitdownrightnow.com/"
    }
    try:
        response = requests.get(check_url, headers=headers)
    except:
        return "null_internet"
    
    
    
    if response.status_code == 200:
        text = response.text.lower().replace('</div>', ' ')
        match = re.search(f'{re.escape(domain.lower())} is (up|down)', text)
        if match:
            status = match.group(1).upper()
            return status
        else:
            return False
    else:
        return "unreach"
        
#------------------------------------------------------------------------------------------------------------------------------
# end line 36