import csv  
import json 
import sys
import os

path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)) )
filename = path + "/Monument/Beni_culturali_Bella_Lombardia.csv"
finalFileName = path + "/Monument/CleanedMonument.geojson"

with open(filename, "r") as f:
    reader = csv.reader(f, delimiter = ",")
    header = reader.__next__()

f = open(filename, 'r' )  
reader = csv.DictReader( f, fieldnames = ( header ) );
reader.__next__()
out = json.dumps( [ row for row in reader ] )  
f = open( finalFileName, 'w')
f.write(out)  

