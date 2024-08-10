import hashlib

class Codec:
    def __init__(self):
        self.url_map={}
        self.base_url="http://tinyurl.com/"
    def encode(self,longUrl:str)->str:
        url_hash=hashlib.md5(longUrl.encode()).hexdigest()[:6]
        shortUrl=self.base_url+url_hash
        self.url_map[shortUrl]=longUrl
        return shortUrl
    def decode(self,shortUrl:str)->str:
        return self.url_map.get(shortUrl,"")
    