# import urllib.request
# import re

# url= "https://raw.githubusercontent.com/damayant/Python/master/api/sample.txt"
# file_content=''
# try:
#     with urllib.request.urlopen(url) as response:
#         file_content=response.read().decode('utf-8')
#         print(file_content)
# except Exception as e:
#     print(e)

# def clean_data(content):
#     arr=content.split('\n')
#     for i in range(len(arr)):
#         arr[i]=re.sub(r'[^a-zA-Z0-9\s]', '', arr[i]).strip(' ')

#     print(arr)

# clean_data(file_content)






















import requests
base_url_one='https://raw.githubusercontent.com/damayant/Python/master/api/sample.txt'
base_url='https://jsonplaceholder.typicode.com/posts'
def get_data(url):
    response = requests.get(url,timeout=5)
    response.raise_for_status()
    content_type=response.headers.get('Content-Type','')
    if 'application/json' in content_type:
        return response.json()
    else:
        return response.text

print(get_data(base_url))
print(get_data(base_url_one))