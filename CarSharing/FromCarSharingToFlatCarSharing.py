from geopy.geocoders import Nominatim
import json
from getUri import urify
import os
path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)) )
inputFile = open( path + "/CarSharing/CarSharing.geojson", "r" );
nativeFile = json.load( inputFile );
definitiveFile = []
temp = {}
counters = {}
geolocator = Nominatim(user_agent="python")

for feature in nativeFile["features"]:
    if ( "operator" in feature["properties"] ):
        
        latitude = 0;
        longitude = 0;
        nome = "";
        operatore = feature["properties"]["operator"];
        indirizzo = "";
        
        latitude = feature["geometry"]["coordinates"][1]
        longitude = feature["geometry"]["coordinates"][0]
        location = geolocator.reverse(str(latitude)+","+str(longitude))
        indirizzo = location.raw["display_name"]
        nome = operatore + ", " + indirizzo;
        arr = location.raw["display_name"].split(",");
        if ( feature["properties"]["operator"] != arr[0] ):
            nome = feature["properties"]["operator"] + ", " + indirizzo;
        else:
            arr.pop(0);
            indirizzo = ", ".join( arr );
            nome = feature["properties"]["operator"] + ", " + indirizzo;
            nome = nome.strip();
            nome = nome.replace("  "," ")
        
        uri = urify( "carSharing", operatore + " " + indirizzo );
        
        if ( uri in counters.keys() ):
            value = counters.get( uri );
            value = value+1;
            counters.update( { uri : value } )
            uri = uri + str("_") + str(value);
        else:
            counters.update( { uri : 0 } )
        
        temp.update( { "nome":nome } )
        temp.update( { "operatore":operatore } )
        temp.update( { "indirizzo":location.raw["display_name"] } )
        temp.update( { "lat":latitude } )
        temp.update( { "long":longitude } );
        temp.update( { "URI":uri } )
        definitiveFile.append( temp );
        temp = {}
    

with open(path + '/CarSharing/UncleanedCarSharing.geojson', 'w') as outfile:  
    json.dump(definitiveFile, outfile)
