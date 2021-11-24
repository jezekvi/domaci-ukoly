import csv
from os import read

def get_rows(ctecka):
    bag = []
    for x in range(7):
        row = next(ctecka) 
        bag.append (row)
    return bag

def average(seznam):
    sum = 0
    for x in seznam:
        sum = sum + float(x[-1])
    return sum/len(seznam)
    
    
    
    
   
with open('vstup.csv', 'r')  as inputfile:
   reader = csv.reader(inputfile)
   rows = get_rows(reader)
   average(rows)




