import urllib.request
import json



url = 'http://developer.myntra.com/search/data/shoes'
urldata = urllib.request.urlopen(url)
same_url = urldata.geturl()
print(same_url)
info = urldata.info()
print(info)

"""
loadjson = json.loads(urldata)

"""


