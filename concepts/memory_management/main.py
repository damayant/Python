import requests
import re 
from collections import Counter 

def process_large_stream(url):
    total_words,line_count=0,0
    clean_regex=re.compile(r'[^a-zA-Z0-9\s]')

    with requests.get(url,stream=True) as response:
        response.raise_for_status()
        buffer=b''
        for chunk in response.iter_content(chunk_size=1024):
            if not chunk:
                break 
            buffer += chunk 
            *lines,buffer=buffer.splitlines()
            for line_bytes in lines:
                line=line_bytes.decode('utf-8')
                clean_line=clean_regex.sub('',line)
                clean_line=clean_line.lower()
                words_in_line=clean_line.split()
                line_word_count=len(words_in_line)
                total_words+= line_word_count
                line_count+=1
            

process_large_stream('https://www.gutenberg.org/files/2701/2701-0.txt')