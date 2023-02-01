import sys
import mmh3
import requests
import codecs

if len(sys.argv) < 2:
        exit('You forgot to pass the favicon url. Eg. python3 favicon-hash.py https://www.google.com/favicon.ico')

response = requests.get(sys.argv[1])
favicon = codecs.encode(response.content,"base64")
hash = mmh3.hash(favicon)

print("☆☆☆☆☆")
print(f"The favicon hash is: {hash}")
print(f"Search in Shodan: https://shodan.io/search?query=http.favicon.hash:{hash}")
print("☆☆☆☆☆")
