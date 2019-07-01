from geopy.geocoders import Nominatim
import json
from getUri import urify
import os
path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)) )
inputFile = open( path + "/CarRental/CarRental.geojson", "r" );
nativeFile = json.load( inputFile );
definitiveFile = []
temp = {}
counters = {}
geolocator = Nominatim(user_agent="1O3B0hu2EPPisdXJvpDFzDM6WOt3xWQQ")

for feature in nativeFile["features"]:
    if ( "name" in feature["properties"] ):
        
        latitude = 0;
        longitude = 0;
        nome = "";
        indirizzo = "";
        
        latitude = feature["geometry"]["coordinates"][1]
        longitude = feature["geometry"]["coordinates"][0]
        location = geolocator.reverse(str(latitude)+","+str(longitude))
        indirizzo = location.raw["display_name"]
        arr = location.raw["display_name"].split(",");
        if ( feature["properties"]["name"] != arr[0] ):
            nome = feature["properties"]["name"] + ", " + indirizzo;
        else:
            arr.pop(0);
            indirizzo = ", ".join( arr );
            nome = feature["properties"]["name"] + ", " + indirizzo;
            nome = nome.strip();
            nome = nome.replace("  "," ")
        
        uri = urify( "bikeRental", feature["properties"]["name"] + " " + indirizzo );
        
        if ( uri in counters.keys() ):
            value = counters.get( uri );
            value = value+1;
            counters.update( { uri : value } )
            uri = uri + str("_") + str(value);
        else:
            counters.update( { uri : 0 } )
        
        temp.update( { "nome":nome } )
        temp.update( { "operatore":feature["properties"]["name"] } )
        temp.update( { "indirizzo":location.raw["display_name"] } )
        temp.update( { "lat":latitude } )
        temp.update( { "long":longitude } );
        temp.update( { "URI":uri } )
        definitiveFile.append( temp );
        temp = {}

with open(path + '/CarRental/UncleanedCarRental.geojson', 'w') as outfile:  
    json.dump(definitiveFile, outfile)
