import csv
from os import read

def get_rows(ctecka):
    bag = []
    for x in range(7):
        try:
            row = next(ctecka)
        except StopIteration:
            break 
        bag.append (row)
    return bag

def average(seznam):
    sum = 0
    for x in seznam:
        sum = sum + float(x[-1])
    return sum/len(seznam)


   
with open('vstup.csv', 'r')  as inputfile, open('vystup_7dni.csv', 'w', newline ='')  as outputfile:
   reader = csv.reader(inputfile)
   writer = csv.writer(outputfile)
   while True:
        rows = get_rows(reader)
        if len(rows) == 0:
            break
        result = average(rows)
        b = rows[0][0:5] 
        b.append(round(result,4))
    
        writer.writerow(b)

