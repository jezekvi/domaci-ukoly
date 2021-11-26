import csv
from os import read

YEAR_INDEX = 2

def get_rows(ctecka):
    bag = []
    for x in range(7):
        try:
            row = next(ctecka)
        except StopIteration:
            break 
        bag.append (row)
    return bag

def get_rows_year(ctecka_year, previous_day):
    bag_year = []
    if previous_day is not None:
        bag_year.append (previous_day)
    try:
        row_year = next(ctecka_year)
    except StopIteration:
        return [], None
    current_year = row_year[YEAR_INDEX]  

    while current_year == row_year[YEAR_INDEX]:
        bag_year.append (row_year)
        try:
            row_year = next(ctecka_year)
        except StopIteration:
            break
    return (bag_year, row_year)

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
        a = rows[0][0:5] 
        a.append(round(result,4))
    
        writer.writerow(a)

with open('vstup.csv', 'r')  as inputfile, open('vystup_rok.csv', 'w', newline ='')  as outputfile_year:
    reader = csv.reader(inputfile)
    writer = csv.writer(outputfile_year)
    last_day_of_year = None
    while True:
        rows_year, last_day_of_year= get_rows_year(reader, last_day_of_year)
        if len(rows_year) == 0:
            break
        result_year = average(rows_year)
        b = rows_year[0][0:5]
        b.append(round(result_year,4))

        writer.writerow(b)
