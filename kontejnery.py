import json
from pyproj import Transformer

def je_kont_verejny (kontejner):
    a = kontejner['properties']['PRISTUP']
    if a == "volně":
        return True 
    else:
        return False
    
def nacteni_souradnic (feature):
    return feature['geometry']['coordinates']

def transform_feature_to_sjtsk (feature):
    wgs2sjtsk = Transformer.from_crs(4326,5514)
    feature['geometry']['coordinates'] = wgs2sjtsk.transform(*nacteni_souradnic(feature))
    return feature


with open('adresy.geojson', 'r', encoding='utf-8')  as input_adresy, open('kontejnery.geojson', 'r', encoding='utf-8')  as input_kontejnery:
    adresy = json.load(input_adresy)
    kontejnery = json.load(input_kontejnery)
  
verejne_kontejnery = filter(je_kont_verejny, kontejnery['features'])

print(transform_feature_to_sjtsk(adresy['features'][0]))


"""
print("Nacteno",len(adresy["features"]),"adresnich bodu")
print("Nacteno",len(kontejnery["features"]),"kontejneru na trideny odpad")

print(adresy['features'][0]['geometry']['coordinates'][0])



wgs2sjtsk = Transformer.from_crs(4326,5514)
prevod = wgs2sjtsk.transform()
print(prevod)

"""