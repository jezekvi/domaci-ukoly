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

def nejblizsi_kontejner (verejne_kontejnery, adresa):
    aktualni_min = 100000000
    souradnice_adresy = nacteni_souradnic(adresa)
    for kontejner in verejne_kontejnery:
        souradnice_kontejneru = nacteni_souradnic(kontejner)
        vzdalenost_adresy_od_kontejneru = vzdalenost(souradnice_adresy, souradnice_kontejneru)
        
        if vzdalenost_adresy_od_kontejneru < aktualni_min:
            aktualni_min = vzdalenost_adresy_od_kontejneru
    return aktualni_min


with open('adresy.geojson', 'r', encoding='utf-8')  as input_adresy, open('kontejnery.geojson', 'r', encoding='utf-8')  as input_kontejnery:
    adresy = json.load(input_adresy)
    kontejnery = json.load(input_kontejnery)
  
verejne_kontejnery = list(filter(je_kont_verejny, kontejnery['features']))
adresy_sjtsk = list(map(transformace_do_sjtsk, adresy['features']))

aktualni_max = [0, None]
seznam_vzdalenosti = []
for adresa in adresy_sjtsk:
    vzdalenost_kontejneru_od_adresy = nejblizsi_kontejner(verejne_kontejnery, adresa)
    seznam_vzdalenosti.append(vzdalenost_kontejneru_od_adresy)
    
    if vzdalenost_kontejneru_od_adresy > aktualni_max[0]:
            aktualni_max = [vzdalenost_kontejneru_od_adresy, adresa]

pocet = len(seznam_vzdalenosti)
suma = sum(seznam_vzdalenosti)
vysledek = suma/pocet

print(aktualni_max)

print("Nacteno",len(adresy["features"]),"adresnich bodu")
print("Nacteno",len(kontejnery["features"]),"kontejneru na trideny odpad")
print("Prumerna vzdalenost ke kontejneru je", round(vysledek), "m.")
print(f"Nejdale ke kontejneru je z adresy {aktualni_max[1]['properties']['addr:street']} {aktualni_max[1]['properties']['addr:streetnumber']} a to je {round(aktualni_max[0])} m.")
