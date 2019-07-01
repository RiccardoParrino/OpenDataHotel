import json
from getUri import urify
import os
from geopy.geocoders import Nominatim
path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)) )
inputFile = open( path + "/Monument/CleanedMonument.geojson", "r" );

geolocator = Nominatim(user_agent="1O3B0hu2EPPisdXJvpDFzDM6WOt3xWQQ")
nativeFile = json.load( inputFile );
definitiveFile = []
temp = {}
counters = {}

for feature in nativeFile:
    if ( ("comune" in feature) and (feature["comune"].lower() == "milano")  ):
        latitude = feature["wgs84_x"];
        longitude = feature["wgs84_y"];
        nome = feature["denominazione"];
        autore = feature["autore"];
        definizione = feature["definizione"];
        abstract = feature["abstract"];
       
        if ( str(definizione) != "None" ):
            definizione = definizione.capitalize();
        else:
            definizione = "void"
        
        if ( str(abstract) != "None" ):
            abstract = abstract;
        else:
            abstract = "void"
        
        if ( str(autore) != "None" and str(autore) != "null" ):
            autore = autore;
        else:
            autore = "void"
        
        if ( latitude == "" or longitude == "" and feature["indirizzo"] != "" ):
#            indirizzo = feature["indirizzo"]
#            indirizzo = indirizzo.replace( ",", " " );
#            location = geolocator.geocode(indirizzo)
#            latitude = location.latitude
#            longitude = location.longitude
#        else:
            latitude = 0
            longitude = 0
        
        uri = urify( "monument",nome );
        
        if ( uri in counters.keys() ):
            value = counters.get( uri );
            value = value+1;
            counters.update( { uri : value } )
            uri = uri + str("_") + str(value);
        else:
            counters.update( { uri : 0 } )
        
        temp.update( { "nome":nome } )
        temp.update( { "autore":autore } )
        temp.update( { "definizione":definizione } )
        temp.update( { "abstract":abstract } )
        temp.update( { "lat":latitude } )
        temp.update( { "long":longitude } );
        temp.update( { "URI":uri } )
        definitiveFile.append( temp );
        temp = {}
    

with open(path + '/Monument/UncleanedEditDistanceMonument.geojson', 'w') as outfile:  
    json.dump(definitiveFile, outfile)
            