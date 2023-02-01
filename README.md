# favicon-hash
Get the hash of a favicon so you can search for it in Shodan.io

```bash
$ python3 favicon-hash.py https://www.google.com/favicon.ico

The favicon hash is: 708578229
Search in Shodan: https://shodan.io/search?query=http.favicon.hash:708578229
```
