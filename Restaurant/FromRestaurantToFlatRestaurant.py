import json
from getUri import urify
import os.path
import os
path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)) )
inputFile = open( path + "/Restaurant/Restaurant.geojson", "r" );
nativeFile = json.load( inputFile );
definitiveFile = []
temp = {}
counters = {}

for feature in nativeFile["features"]:
    if ( "name" in feature["properties"] ):
        
        latitude = 0;
        longitude = 0;
        nome = feature["properties"]["name"];
        website = ""
        cap = ""
        indirizzo = ""
        cuisine = ""
        
        if ( "name:it" in feature["properties"] ):
            nome = feature["properties"]["name:it"];
        if ( "name" in feature["properties"] ):
            nome = feature["properties"]["name"];
        if ( "website" in feature["properties"] ):
            website = feature["properties"]["website"]
        if ( "contact:website" in feature["properties"] ):
            website = feature["properties"]["contact:website"]
        if ( "addr:place" in feature["properties"] ):
            indirizzo = feature["properties"]["addr:place"]
        if ( "addr:country" in feature["properties"] ):
            indirizzo = feature["properties"]["addr:country"]
        if ( "addr:city" in feature["properties"] ):
            indirizzo = feature["properties"]["addr:city"]
        if ( "addr:street" in feature["properties"] ):
            indirizzo = feature["properties"]["addr:street"]
        if ( "addr:postcode" in feature["properties"] ):
            cap = feature["properties"]["addr:postcode"];
        if ( "cuisine" in feature["properties"] ):
            cuisine = feature["properties"]["cuisine"];
        
        if ( str(nome) == "" ):
            nome = "void"
        if ( str(website) == "" ):
            website = "void"
        if ( str(cap) == "" ):
            cap = "void"
        if ( str(indirizzo) == "" ):
            indirizzo = "void"
        if ( str(cuisine) == "" ):
            cuisine = "void"
        
        uri = urify( "restaurant",nome );
        
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
        temp.update( { "cap":cap } )
        temp.update( { "indirizzo":indirizzo } )
        temp.update( { "cucina":cuisine } )
        temp.update( { "lat":latitude } )
        temp.update( { "long":longitude } );
        temp.update( { "URI":uri } )
        definitiveFile.append( temp );
        temp = {}
    

with open(path + '/Restaurant/UncleanedRestaurant.geojson', 'w') as outfile:  
    json.dump(definitiveFile, outfile)
