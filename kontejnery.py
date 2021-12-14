import json

with open('adresy.geojson', 'r')  as input_adresy, open('kontejnery.geojson', 'r')  as input_kontejnery:
    adresy = json.load(input_adresy)
    kontejnery = json.load(input_kontejnery)
  

