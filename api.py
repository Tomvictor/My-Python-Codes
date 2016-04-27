import urllib.request
import json



url = 'http://developer.myntra.com/search/data/shoes'
res = urllib.request.urlopen(url)

same_url = res.geturl()
info = res.info()
code = res.getcode()

print(same_url)
print(code)


str_data = res.readall().decode('utf-8')
json_data = json.loads(str_data)
temp = json_data['data']['results']['products']

for item in temp:
    print(item['product'])

print(temp)

