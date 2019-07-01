import json
from getUri import urify
import os
path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)) )
inputFile = open( path + "/Park/Park.geojson", "r" );
nativeFile = json.load( inputFile );
definitiveFile = []
temp = {}
counters = {}

for feature in nativeFile["features"]:
    if ( "name" in feature["properties"] ):
        latitude = 0;
        longitude = 0;
        nome = feature["properties"]["name"];
        
        #if ( "coordinates" in feature["geometry"] ):
        if ( not(feature["geometry"] is None) ):
            latitude = feature["geometry"]["coordinates"][1];
            longitude = feature["geometry"]["coordinates"][0];

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
            