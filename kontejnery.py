from functools import reduce
import json
from pyproj import Transformer
from math import sqrt
wgs2sjtsk = Transformer.from_crs(4326,5514, always_xy=True)


def je_kont_verejny (kontejner):
    a = kontejner['properties']['PRISTUP']
    if a == "volně":
        return True 
    else:
        return False
    
def nacteni_souradnic (feature):
    return feature['geometry']['coordinates']

def transformace_do_sjtsk (feature):
    feature['geometry']['coordinates'] = wgs2sjtsk.transform(*nacteni_souradnic(feature))
    return feature

def vzdalenost (souradnice_1, souradnice_2):
    delta_y = souradnice_1[0] - souradnice_2[0]
    delta_x = souradnice_1[1] - souradnice_2[1]
    return sqrt( (delta_y * delta_y) + (delta_x * delta_x) )


with open('adresy.geojson', 'r', encoding='utf-8')  as input_adresy, open('kontejnery.geojson', 'r', encoding='utf-8')  as input_kontejnery:
    adresy = json.load(input_adresy)
    kontejnery = json.load(input_kontejnery)
  
verejne_kontejnery = list(filter(je_kont_verejny, kontejnery['features']))
adresy_sjtsk = list(map(transformace_do_sjtsk, adresy['features']))


souradnice_adresy = nacteni_souradnic(adresy_sjtsk[0])
souradnice_kontejnery = nacteni_souradnic(verejne_kontejnery[0])

print(vzdalenost(souradnice_adresy, souradnice_kontejnery))


"""
print("Nacteno",len(adresy["features"]),"adresnich bodu")
print("Nacteno",len(kontejnery["features"]),"kontejneru na trideny odpad")
"""