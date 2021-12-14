import json
from typing import DefaultDict
import requests

adict = json.loads('{"key":12}')
print(adict["key"])

URL = "https://mapa.pid.cz/getData.php"

r = requests.get(URL)

print(r.status_code)
print(r.encoding)
print(r.text[:100])

data = r.json()

print(type(data))
print(data.keys())
print(type(data['trips']))
print(data['trips']['389/2'])

vehicles = data['trips'].values() 
print(vehicles)   

#vehicles, route, počet na route

linky = {}
for a in vehicles:
    linky[a['route']] = linky.setdefault(a['route'],0) + 1
print(linky)