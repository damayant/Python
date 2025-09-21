import urllib.request

url= "https://raw.githubusercontent.com/damayant/Python/master/api/sample.txt"

try:
    with urllib.request.urlopen(url) as response:
        file_content=response.read()
        print(file_content.decode('utf-8'))
except urllib.URLError as e:
    print(e)