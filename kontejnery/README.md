# Domácí úkol 3 - vzdálenost ke kontejnerům na tříděný odpad

## Základní informace
Program funguje na pricipu počítání přímých vzdáleností mezi adresami a kontejnery na tříděný odpad. Skript není interaktivní a nevyžaduje žádný zásah od uživatele. 

## Vstupní data
Vstupem do programu jsou dva soubory, a to `adresy.geojson` a `kontejnery.geojson`. V případě, že program nenalezne vstupní soubory nebo budou soubory nekorektní, program skončí chybou:
```
Vstupni soubor je nekorektni
```
Pokud je soubor validní JSON, ale nevalidní GeoJSON, nebo chybí nějaký atribut, tak v této verzi program spadne.

## Průběh algoritmu
Po načtení vstupních souborů program nejříve vybere pouze veřejně přístupné kontejnery. Následně pomocí transformační rovnice převede polohové souřadnice adres ze souřadnicového systému WGS-84 do S-JTSK. Díky tomu sjednotí souřadnicové systémy obou vstupních souborů. Následně program vypočítá vzdálenosti všech adres ke všem veřejně dostupným kontejnerům. Nejkratší vzdálenosti ze všech adres následně využije k výpočtu průměrné vzdálenosti. Ze seznamu nejkratších vzdáleností vypočítá také medián a vybere největší hodnotu pro zjištění nejvzdálenější adresy od kontejneru.  

## Výstup
Program po dokončení výpočtů vypíše tabulku:
```
Nacteno 708 adresnich bodu
Nacteno 5813 kontejneru na trideny odpad
Prumerna vzdalenost ke kontejneru je 82 m.
Median vzdalenosti ke kontejnerum je 72 m.
Nejdale ke kontejneru je z adresy Zelenkova 3c a to 361 m.
```
Kromě základních informací o počtu načtených bodů poskytne uživateli informace o průměrné vzdálenosti ke kontejnerům. Dále vypíše medián vzdáleností a také adresu od které je to k nejbližšímu kontejneru nejdále. 

Pokud alespoň pro jednu adresu platí, že nejbližší kontejner je vzdálený více než 10000 metrů, tak program skončí chybovou hláškou:
```
Chyba, nejkratsi vzdalenost kontejneru od nektere z adres je vetsi nez 10000 m.
```
