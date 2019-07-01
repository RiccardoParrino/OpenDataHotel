import json 
import sys

import os
path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)) )

filename = path + "/Hotel/FlatHotelMilano2018.geojson"
finalFileName = path + "/Hotel/FinalFlatHotelMilano2018.geojson"

inputFile = open(filename, "r" );
nativeFile = json.load( inputFile );
definitiveFile = []
temp = {}

for element in nativeFile:
    if ( element["DENOMINAZIONE_STRUTTURA"] != "" ):
        denominazione = element["DENOMINAZIONE_STRUTTURA"]
        latitude = element["geo_x"];
        longitude = element["geo_y"];
        categoria = element["CATEGORIA"];
        classificazione = element["CLASSIFICAZIONE"];
        camere = element["CAMERE"];
        cap = element["CAP"];
        web = element["WEB"];
        email = element["EMAIL"];
        tel = element["TEL"];
        fax = element["FAX"];
        indirizzo = element["INDIRIZZO"];
        
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
