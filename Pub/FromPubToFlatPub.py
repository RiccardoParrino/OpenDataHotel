import json
from getUri import urify
import os
path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)) )
inputFile = open( path + "/Pub/Pub.geojson", "r" );
nativeFile = json.load( inputFile );
definitiveFile = []
temp = {}
counters = {}

for feature in nativeFile["features"]:
    if ( "name" in feature["properties"] ):
        
        latitude = 0;
        longitude = 0;
        nome = "";
        website = ""
        cap = ""
        indirizzo = ""
        email = ""
        
        if ( "name" in feature["properties"] ):
            nome = feature["properties"]["name"];
        if ( "website" in feature["properties"] ):
            website = feature["properties"]["website"]
        if ( "contact:website" in feature["properties"] ):
            website = feature["properties"]["contact:website"]
        if ( "email" in feature["properties"] ):
            mail = feature["properties"]["email"]
        if ( "contact:email" in feature["properties"] ):
            mail = feature["properties"]["contact:email"]
        if ( "addr:full" in feature["properties"] ):
            indirizzo = feature["properties"]["addr:full"]
        if ( "addr:country" in feature["properties"] ):
            indirizzo = feature["properties"]["addr:country"]
        if ( "addr:city" in feature["properties"] ):
            indirizzo = feature["properties"]["addr:city"]
        if ( "addr:street" in feature["properties"] ):
            indirizzo = feature["properties"]["addr:street"]
        if ( "postalcode" in feature["properties"] ):
            cap = feature["properties"]["postalcode"];
        if ( "addr:postcode" in feature["properties"] ):
            cap = feature["properties"]["addr:postcode"];
        
        if ( str(nome) == "" ):
            nome = "void"
        if ( str(website) == "" ):
            website = "void"
        if ( str(cap) == "" ):
            cap = "void"
        if ( str(indirizzo) == "" ):
            indirizzo = "void"
        if ( email == "" ):
            email = "void"
        
        uri = urify( "pub",nome );
        
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
        temp.update( { "website":website } )
        temp.update( { "email":email } )
        temp.update( { "cap":cap } )
        temp.update( { "indirizzo":indirizzo } )
        temp.update( { "lat":latitude } )
        temp.update( { "long":longitude } );
        temp.update( { "URI":uri } )
        definitiveFile.append( temp );
        temp = {}
    

with open(path + '/Pub/UncleanedPub.geojson', 'w') as outfile:  
    json.dump(definitiveFile, outfile)
