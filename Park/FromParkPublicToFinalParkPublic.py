import json
from getUri import urify
import os
path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)) )
inputFile = open( path + "/Park/Park.geojson", "r" );
nativeFile = json.load( inputFile );
definitiveFile = []
temp = {}
counters = {}
distinctPark = set()
for feature in nativeFile["features"]:
    if ( "PARCO" in feature["properties"] ):
        latitude = 0;
        longitude = 0;
        nome = feature["properties"]["PARCO"];
        if ( nome in distinctPark ):
            continue
        else:
            distinctPark.add( nome )
        #if ( "coordinates" in feature["geometry"] ):
        if ( ("coordinates" in feature["geometry"]) and not(feature["geometry"] is None) ):
            latitude = feature["geometry"]["coordinates"][0][0][1];
            longitude = feature["geometry"]["coordinates"][0][0][0];
        
        if ( type(latitude) == list ):
            temp2 = latitude[1];
            longitude = latitude[0]
            latitude = temp2

        uri = urify( "publicPark",nome );
        
        if ( uri in counters.keys() ):
            value = counters.get( uri );
            value = value+1;
            counters.update( { uri : value } )
            uri = uri + str("_") + str(value);
        else:
            counters.update( { uri : 0 } )

        temp.update( { "nome":nome } )
        temp.update( { "lat":latitude } )
        temp.update( { "long":longitude } );
        temp.update( { "URI":uri } )
        definitiveFile.append( temp );
        temp = {}
    

with open(path + '/Park/UncleanedParkPublic.geojson', 'w') as outfile:  
    json.dump(definitiveFile, outfile)
            