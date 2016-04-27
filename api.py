import urllib.request
import json



url = 'http://developer.myntra.com/search/data/shoes'
res = urllib.request.urlopen(url)

same_url = res.geturl()
print(same_url)

str_data = res.readall().decode('utf-8')
json_data = json.loads(str_data)
temp = json_data['data']['results']['products']

for item in temp:
    print(item['price'])

print(temp)

