import json
from getUri import urify
import os
path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)) )
inputFile = open( path + "/RailwayStation/RailwayStation.geojson", "r" );
nativeFile = json.load( inputFile );
definitiveFile = []
temp = {}
counters = {}

for feature in nativeFile["features"]:
    if ( "nome" in feature["properties"] ):
        latitude = 0;
        longitude = 0;
        nome = feature["properties"]["nome"];
        gestore = "";
        
        if ( "gestore" in feature["properties"] ):
            gestore = feature["properties"]["gestore"];
        if ( "coordinates" in feature["geometry"] ):
            latitude = feature["geometry"]["coordinates"][1];
            longitude = feature["geometry"]["coordinates"][0];
        
        uri = urify( "railwayStation",nome );
        
        if ( uri in counters.keys() ):
            value = counters.get( uri );
            value = value+1;
            counters.update( { uri : value } )
            uri = uri + str("_") + str(value);
        else:
            counters.update( { uri : 0 } )
        
        temp.update( { "nome":nome } )
        temp.update( { "gestore":gestore } )
        temp.update( { "lat":latitude } )
        temp.update( { "long":longitude } );
        temp.update( { "URI":uri } )
        definitiveFile.append( temp );
        temp = {}
    

with open(path + '/RailwayStation/UncleanedRailwayStation.geojson', 'w') as outfile:  
    json.dump(definitiveFile, outfile)
            