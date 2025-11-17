# https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem?isFullScreen=true
import re 
def func(s):
    try:
        username,website=s.split("@")
        web,extension=website.split(".")
    except ValueError:
        return False
    
    username_pattern = r'^[a-zA-Z0-9_-]+$'
    web_pattern=r'^[a-zA-Z0-9]+$'
    extension_pattern=r'[a-z]+$'

    if (re.match(username_pattern,username) 
        and re.match(web_pattern,web)
        and re.match(extension_pattern,extension)
        and 1<= len(extension)<=3):
        return True 
    return False

print(func("damayanti.ghosh@cgi.com"))