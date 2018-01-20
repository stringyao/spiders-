import requests
import re
from bs4 import BeautifulSoup
import datetime

def get_security_codes():
    
    security_codes_url = "http://quote.eastmoney.com/stocklist.html#sh"
    
    response = requests.get(security_codes_url)
    
    content = BeautifulSoup(response.content.decode('gbk'), "html.parser")
    
    contents = content.find_all('li')
    
    codes = []
    
    for string in contents:
        if "(" in string.text:
            codes.append(re.findall(r'\d+', string.text))
    
    security_codes = []
    pools = ['0', '6', '3']
    
    for code in codes:
        
        if len(code) == 1:
            if code[0][:1] in pools:
                security_codes.append(code[0])
                
    return security_codes
