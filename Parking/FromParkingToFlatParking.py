import json
from getUri import urify
import os
path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)) )
inputFile = open( path+"/Parking/Parking.geojson", "r" );
nativeFile = json.load( inputFile );
definitiveFile = []
temp = {}
counters = {}

for feature in nativeFile["features"]:
    if ( "name" in feature["properties"] ):
        
        latitude = 0;
        longitude = 0;
        nome = "";
        indirizzo = ""
        charge = ""
        capacity = ""
        tipo = ""

        if ( "short_name" in feature["properties"] ):
            nome = feature["properties"]["short_name"];
        if ( "name:en" in feature["properties"] ):
            nome = feature["properties"]["name:en"];   
        if ( "name:it" in feature["properties"] ):
            nome = feature["properties"]["name:it"];
        if ( "name" in feature["properties"] ):
            nome = feature["properties"]["name"];
        if ( "addr:country" in feature["properties"] ):
            indirizzo = feature["properties"]["addr:country"]
        if ( "addr:city" in feature["properties"] ):
            indirizzo = feature["properties"]["addr:city"]
        if ( "addr:street" in feature["properties"] ):
            indirizzo = feature["properties"]["addr:street"]
        if ( "addr:postcode" in feature["properties"] ):
            cap = feature["properties"]["addr:postcode"];
        if ( "capacity" in feature["properties"] ):
            capacity = feature["properties"]["capacity"];
        if ( "charge" in feature["properties"] ):
            charge = feature["properties"]["charge"];
        if ( "parking" in feature["properties"] ):
            tipo = feature["properties"]["parking"];
            
        
        if ( str(nome) == "" ):
            nome = "void"
        if ( str(capacity) == "" ):
            capacity = -1
        if ( str(tipo) == "" ):
            tipo = "void"
        if ( str(charge) == "" ):
            charge = -1
        if ( str(indirizzo) == "" ):
            indirizzo = "void"
        
        uri = urify( "parking",nome );
        
        if ( uri in counters.keys() ):
            value = counters.get( uri );
            value = value+1;
            counters.update( { uri : value } )
            uri = uri + str("_") + str(value);
        else:
            counters.update( { uri : 0 } )
        
        latitude = feature["geometry"]["coordinates"][1]
        longitude = feature["geometry"]["coordinates"][0]

        temp.update( { "nome":nome } )
        temp.update( { "indirizzo":indirizzo } )
        temp.update( { "capacity":capacity } )
        temp.update( { "charge":charge } )
        temp.update( { "tipo":tipo } )
        temp.update( { "lat":latitude } )
        temp.update( { "long":longitude } );
        temp.update( { "URI":uri } )
        definitiveFile.append( temp );
        temp = {}
    

with open(path+'/Parking/UncleanedParking.geojson', 'w') as outfile:  
    json.dump(definitiveFile, outfile)