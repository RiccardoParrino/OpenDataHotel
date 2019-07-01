import json
import sys

import os
path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)) )

filename = path + "/Hotel/FlatMilanHotel.geojson"
finalFileName = path + "/Hotel/FinalFlatMilanHotel2018.geojson"

inputFile = open( filename, "r" );
nativeFile = json.load( inputFile );
definitiveFile = []
temp = {}

for element in nativeFile:
    if ( "name" in element or "name:it" in element or "oldname" in element ):
        denominazione = element["name"]
        latitude = 0;
        longitude = 0;
        categoria = "";
        classificazione = "";
        camere = -1;
        cap = "";
        web = "";
        email = "";
        tel = "";
        fax = "";
        indirizzo = "";
        
        if ( "oldname" in element ):
            denominazione = element["oldname"]
        if ( "name:it" in element ):
            denominazione = element["name:it"]
        if ( "name" in element ):
            denominazione= element["name"]
        if ( "lat" in element ):
            latitude = element["lat"]
        if ( "long" in element ):
            longitude = element["long"]
        if ( "stars" in element ):
            classificazione = element["stars"]
        if ( "rooms" in element ):
            camere = element["rooms"]
        if ( "addr:postcode" in element ):
            cap = element["addr:postcode"]
        if ( "website" in element ):
            web = element["website"]
        if ( "website:it" in element ):
            web = element["website:it"]
        if ( "contact:website" in element ):
            web = element["contact:website"]
        if ( "email" in element ):
            email = element["email"]
        if ( "contact:email" in element ):
            email = element["contact:email"]
        if ( "phone_1" in element ):
            tel = element["phone_1"]
        if ( "contact:phone" in element ):
            tel = element["contact:phone"]
        if ( "fax" in element ):
            fax = element["fax"]
        if ( "contact:fax" in element ):
            fax = element["contact:fax"]
        if ( "addr:full" in element ):
            indirizzo = element["addr:full"]
        if ( "addr:city" in element ):
            indirizzo = element["addr:city"]
        if ( "addr:street" in element ):
            indirizzo = element["addr:street"]
         
        temp.update( { "DENOMINAZIONE_STRUTTURA":denominazione } )
        temp.update( { "CATEGORIA":categoria } )
        temp.update( { "CLASSIFICAZIONE":classificazione } )
        temp.update( { "CAMERE":camere } );
        temp.update( { "INDIRIZZO":indirizzo } );
        temp.update( { "CAP":cap} );
        temp.update( { "TEL":tel} );
        temp.update( { "FAX":fax} );
        temp.update( { "EMAIL":email} );
        temp.update( { "WEB":web} );
        temp.update( { "LAT":latitude } )
        temp.update( { "LONG":longitude } )
        definitiveFile.append( temp );
        temp = {}
    

with open(finalFileName, 'w') as outfile:  
    json.dump(definitiveFile, outfile)
