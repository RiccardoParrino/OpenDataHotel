import csv  
import json 
import sys
import os
path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)) )

filename = path + "/Hotel/hotel_milano_2018.csv"
finalFileName = path + "/Hotel/FlatHotelMilano2018.geojson"

with open(filename, "r") as f:
    reader = csv.reader(f, delimiter = ",")
    header = reader.__next__()

f = open(filename, 'r' )  
reader = csv.DictReader( f, fieldnames = ( header ) );
reader.__next__()
out = json.dumps( [ row for row in reader ] )  
f = open( finalFileName, 'w')
f.write(out)  
