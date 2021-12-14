import json

def je_kont_verejny (kontejner):
    a = kontejner['properties']['PRISTUP']
    if a == "volně":
        return True 
    else:
        return False


with open('adresy.geojson', 'r', encoding='utf-8')  as input_adresy, open('kontejnery.geojson', 'r', encoding='utf-8')  as input_kontejnery:
    adresy = json.load(input_adresy)
    kontejnery = json.load(input_kontejnery)
  
verejne_kontejnery = filter(je_kont_verejny, kontejnery['features'])

for kontejner in verejne_kontejnery:
    print(kontejner['properties']['PRISTUP'])

print(len(kontejnery["features"]))
print(len(adresy["features"]))