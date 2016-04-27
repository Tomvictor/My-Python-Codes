import urllib.request
import json



url = 'http://developer.myntra.com/search/data/shoes'
urldata = urllib.request.urlopen(url)

same_url = urldata.geturl()
info = urldata.info()
code = urldata.getcode()

print(same_url)
print(code)


"""
loadjson = json.loads(urldata)

"""

print(urldata.read(300))
