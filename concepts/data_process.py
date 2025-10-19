import urllib.request
import re


 #------------------------approach 1 ---------------------------------------#
url= "https://raw.githubusercontent.com/damayant/Python/master/api/sample.txt"
file_content=''
try:
    with urllib.request.urlopen(url) as response:
        file_content=response.read().decode('utf-8')
        print(file_content)
except Exception as e:
    print(e)

def clean_data(content):
    arr=content.split('\n')
    for i in range(len(arr)):
        arr[i]=re.sub(r'[^a-zA-Z0-9\s]', '', arr[i]).strip(' ')

    print(arr)

clean_data(file_content)
'''
1. urllib.request Approach
Pros:

Part of Python’s standard library (no external dependencies).
Explicit control over reading and decoding bytes.
Can be used for simple file/text downloads.
Cons:

More verbose and lower-level API.
No built-in support for JSON parsing.
Error handling is basic (just prints the exception).
Synchronous only (blocks the main thread).
Less flexible for handling headers, timeouts, and other HTTP features.
'''

 #------------------------approach 2 ---------------------------------------#
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

'''
Pros:

High-level, user-friendly API.
Built-in support for JSON responses.
Easy access to headers, status codes, and other HTTP features.
Better error handling (raise_for_status()).
More concise and readable.
Cons:

Requires external dependency (requests).
Still synchronous (blocks main thread).
Error handling could be more robust (e.g., custom exceptions, retries).
'''

 #------------------------approach 3 ---------------------------------------#

import requests
import logging

logging.basicConfig(
    filename="data_retrieval.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

def get_data(url, stream=False, chunk_size=1024):
    try:
        response = requests.get(url, timeout=10, stream=stream)
        response.raise_for_status()
        content_type = response.headers.get('Content-Type', '')
        if stream:
            # For large text files, process in chunks
            for chunk in response.iter_content(chunk_size=chunk_size):
                if chunk:
                    text_chunk = chunk.decode('utf-8')
                    logging.info(f"Chunk received: {len(text_chunk)} bytes")
                    yield text_chunk
        elif 'application/json' in content_type:
            return response.json()
        else:
            return response.text
    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed for {url}: {e}")
        return None

# Usage example for large text file
base_url_one = 'https://raw.githubusercontent.com/damayant/Python/master/api/sample.txt'
for chunk in get_data(base_url_one, stream=True):
    print(chunk)

# Usage example for JSON API
base_url = 'https://jsonplaceholder.typicode.com/posts'
result = get_data(base_url)
print(result)

'''
Design: Uses requests for flexibility, supports both text and JSON, and can stream large files.
Error Handling: Catches and logs all request exceptions, logs chunk sizes for monitoring.
Failsafe: Streams data in chunks, so memory usage stays low even for huge files.
Extensible: Can be adapted for async (with httpx or aiohttp) for non-blocking calls.
Logging: Stores errors and chunk info in a log file for debugging and audit.
Usage: Can be used for both small and large data, and for both text and JSON endpoints.
Summary:
The improved code combines the flexibility and features of requests, robust error handling, chunked streaming for large data, and logging for failsafe operation. It is suitable for production scenarios where reliability and scalability matter.

'''

# api best practices:https://chatgpt.com/share/68f526d9-5b94-800e-8242-78b13141cd5b


####--- final-------######
def get_data(base_url,timeout_limit,chunk_limit,stream=False):
    #create a session
    session= requests.Session()

    #create a try block
    try:
        #use context manager for ensuring connection is closed properly
        with session.get(url=base_url,timeout=timeout_limit,stream=stream) as response:
            #check if any error
            response.raise_for_status()
            #check content type
            content_type=response.headers.get('Content-Type','')
            if 'application/json' in content_type:
                return response.json()
            elif stream:
                #stream means usually large data so use iterator
                for chunk in response.iter_content(chunk_size=chunk_limit):
                    if chunk:
                        text_chunk=chunk.decode('utf-8',errors='ignore')
                        logging.info(f'chunk recieved:{len(text_chunk)} bytes')
                        yield text_chunk
            else:
                return response.text
    except requests.RequestException as e:
        logging.error(f'request failed for {base_url}:{e}')
        return None
    finally:
        session.close()
                        