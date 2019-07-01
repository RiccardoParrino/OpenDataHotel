import json
from getUri import urify
import os
path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)) )
inputFile = open( path + "/Bus/BusStation.geojson", "r" );
nativeFile = json.load( inputFile );
reportFile = open( path+"/Bus/report.txt","w" )
definitiveFile = []
temp = {}
counters = {}

for feature in nativeFile["features"]:
    if ( "ubicazione" in feature["properties"] ):
        #print("ciao")
        latitude = 0;
        longitude = 0;
        nome = feature["properties"]["ubicazione"];
        linee = "";
        reportFile.write( nome + "\n" );
        
        if ( "linee" in feature["properties"] ):
            if ( str( feature["properties"]["linee"] ) != "None" ):
                linee = feature["properties"]["linee"].split(",");
            else:
                linee = "Mancante"
        if ( "coordinates" in feature["geometry"] ):
            latitude = feature["geometry"]["coordinates"][1];
            longitude = feature["geometry"]["coordinates"][0];
        
        counter = 0;
        
        uri = urify( "busStation",nome );
        
        if ( uri in counters.keys() ):
            value = counters.get( uri );
            value = value+1;
            counters.update( { uri : value } )
            uri = uri + str("_") + str(value);
        else:
            counters.update( { uri : 0 } )
        
        while ( counter < len(linee) ):
            temp.update( { "nome":nome } )
            temp.update( { "linea":linee[counter] })
            temp.update( { "lat":latitude } )
            temp.update( { "long":longitude } );
            temp.update( { "URI":uri } )
            definitiveFile.append( temp );
            counter = counter + 1
            temp = {}
    

with open(path + '/Bus/UncleanedBusStation.geojson', 'w') as outfile:  
    json.dump(definitiveFile, outfile)

reportFile.close();