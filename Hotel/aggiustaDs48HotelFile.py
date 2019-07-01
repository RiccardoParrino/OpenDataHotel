import json
from geopy.geocoders import Nominatim
import sys

import os
path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)) )

filename = path + "/Hotel/ds48_turismotempolibero_strutture-ricettive-alberghiere_2015.json"
finalFileName = path + "/Hotel/FinalFlatDs48HotelFile.geojson"

geolocator = Nominatim(user_agent="1O3B0hu2EPPisdXJvpDFzDM6WOt3xWQQ")

nativeFile = json.load( open( filename, "r" ) );
definitiveFile = []
temp = {}

def locate ( indirizzo ):
    try:
        location = geolocator.geocode(indirizzo)
        return location
    except:
        return "problem"

counter = 0

for element in nativeFile:
    if ( "Insegna" in element ):
        denominazione = element["Insegna"]
        latitude = 0;
        longitude = 0;
        if ( "Indirizzo" in element ):
            indirizzo = element["Indirizzo"]
            arr = indirizzo.split();
            tipo = arr[0]
            tipo = tipo.replace( "PLE", "PIAZZALE" )
            tipo = tipo.replace( "ALZ", "ALZATA" )
            tipo = tipo.replace( "CSO", "CORSO" )
            tipo = tipo.replace( "LGO", "LAGO" )
            tipo = tipo.replace( "GLL", "GALLERIA" )
            tipo = tipo.replace( "VLE", "VIALE" )
            tipo = tipo.replace( "PZA", "PIAZZA" )
            arr[0] = tipo
            indirizzo = ' '.join(arr)
            errore = 1
            while( errore == 1 ):
                location = locate(indirizzo)
                if ( location == "problem" ):
                    errore = 1
                else:
                    errore = 0
                
            #print( indirizzo )
            if ( str(location) == "None" ):
                latitude = 0
                longitude = 0
            else:
                counter = counter + 1
                #print(counter)
                latitude = location.latitude
                longitude = location.longitude
        else:
            indirizzo = ""
        
        if ( "Categoria" in element ):
            classificazione = element["Categoria"]
        else:
            classificazione = ""
        
        if ( "Tipologia" in element ):
            categoria = element["Tipologia"]
        else:
            categoria = ""
        
        if ( "Numero camere" in element ):
            camere = element["Numero camere"]
        else:
            camere = -1
        
        temp.update( { "DENOMINAZIONE_STRUTTURA":denominazione } )
        temp.update( { "CATEGORIA":categoria } )
        temp.update( { "CLASSIFICAZIONE":classificazione } )
        temp.update( { "CAMERE":camere } );
        temp.update( { "INDIRIZZO":indirizzo } );
        temp.update( { "CAP":""} );
        temp.update( { "TEL":""} );
        temp.update( { "FAX":""} );
        temp.update( { "EMAIL":""} );
        temp.update( { "WEB":""} );
        temp.update( { "LAT":latitude } )
        temp.update( { "LONG":longitude } )
        definitiveFile.append( temp );
        temp = {}

with open(finalFileName, 'w') as outfile:  
    json.dump(definitiveFile, outfile)
        
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            