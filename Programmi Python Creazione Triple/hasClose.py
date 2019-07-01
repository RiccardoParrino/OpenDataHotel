from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import RDF, RDFS, FOAF, OWL, XSD, DC, DCTERMS
import json 
import geopy.distance
import os
path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)) )
class triple:
    def __init__( self, uri, latitude, longitude ):
        self.uri = uri
        self.latitude = latitude
        self.longitude = longitude

dataHotel = json.load( open( path+"/DatiPerElaborazione/Hotel.geojson", "r" ) );

g = Graph();
cmo = Namespace("http://www.comune.milano.it/ontology/");
schema = Namespace("https://schema.org/")
g.bind("cmo",cmo);
g.bind("schema", schema);
g.parse(path+"/Turtles/hotel.ttl", format="turtle")

hotelList = []
tripleList = []

fileSet = {"Monument","ParkPublic","Bar","Pub","FastFood","Parking","Restaurant","BusStation","SubwayStation","RailwayStation","CarRental","BikeRental","CarSharing"}

for hotel in dataHotel:
    hotelList.append( triple( hotel["URI"], hotel["LAT"], hotel["LONG"] ) )

for file in fileSet :
    tripleList = []
    dataStruct = json.load( open( path+"/DatiPerElaborazione/" + file + ".geojson", "r" ) );
    
    for element in dataStruct:
        tripleList.append( triple( element["URI"], element["lat"], element["long"] ) )
        
    for element in hotelList:
        positionHotel = [ element.latitude, element.longitude ];
        uriHotel = element.uri
        for structure in tripleList:
            positionStructure = [ structure.latitude, structure.longitude ]
            uriStruct = structure.uri
            if ( geopy.distance.distance(positionHotel, positionStructure ).m <= 100 ):
                g.add( [ URIRef( uriHotel ), cmo.hasClose, URIRef( uriStruct ) ] );
        

g.serialize(destination=path+'/Turtles/hotel.ttl', format='turtle')

