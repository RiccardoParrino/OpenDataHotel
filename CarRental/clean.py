import json
import os
import editdistance
from getUri import urify

class stringa:
    def __init__ ( self, argument ):
        self.stringa = argument;
    
    def __eq__( self, other ):
        if ( isinstance( other, stringa ) and editdistance.eval( self.stringa, other.stringa ) < 5 ):
            return True;
        else:
            return False;
    
    def __hash__ ( self ):
        return 1

def getMostLikelyWord ( stringSet, word ):
    minimumDistance = 9223372036854775807
    bestWord = ""
    for element in stringSet:
        distance = editdistance.eval( word, element.stringa )
        if ( distance < minimumDistance ):
            minimumDistance= distance
            bestWord = element.stringa
    return bestWord

path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)) )
inputFile = open( path + "/CarRental/UncleanedCarRental.geojson", "r" );
nativeFile = json.load( inputFile );
finalFileName = path + "/DatiPerElaborazione/CarRental.geojson"
definitiveFile = []
temp = {}
counters = {}
stringSet = set()

for element in nativeFile:
    stringSet.add( stringa( element["nome"] ) )

for element in nativeFile:
    element["nome"] = getMostLikelyWord( stringSet, element["nome"] );
    
    uri = urify( "bikeRental", element["nome"] );
    
    if ( uri in counters.keys() ):
        value = counters.get( uri );
        value = value+1;
        counters.update( { uri : value } )
        uri = uri + str("_") + str(value);
    else:
        counters.update( { uri : 0 } )
    
    element["URI"] = uri
    definitiveFile.append( element );
    temp = {}

with open(finalFileName, 'w') as outfile:  
    json.dump(definitiveFile, outfile)