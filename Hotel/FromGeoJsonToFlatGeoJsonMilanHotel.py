import json 
import sys

#filename = sys.argv[1]
#finalFileName = sys.argv[2]

import os
path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)) )

filename = path + "/Hotel/MilanHotel.geojson"
finalFileName = path + "/Hotel/FlatMilanHotel.geojson"

definitiveFile = []
inputFile = open( filename, "r" );
nativeFile = json.load( inputFile );
temp = {}

for feature in nativeFile["features"]:
    temp.update( feature["properties"] )
    temp.update( {"long" : feature["geometry"]["coordinates"][0]} )
    temp.update( {"lat" : feature["geometry"]["coordinates"][1]} )
    definitiveFile.append( temp );
    temp = {};

with open(finalFileName, 'w') as outfile:  
    json.dump(definitiveFile, outfile)
    
inputFile.close();
