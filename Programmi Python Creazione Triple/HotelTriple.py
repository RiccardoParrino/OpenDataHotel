from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import RDF, RDFS, FOAF, OWL, XSD, DC, DCTERMS
import json 
from linking import link
import os
path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)) )
data = json.load( open( path+"/DatiPerElaborazione/Hotel.geojson", "r" ) );
g = Graph();

cmo = Namespace("http://www.comune.milano.it/ontology/");
schema = Namespace("https://schema.org/")
g.bind("cmo",cmo);
g.bind("schema", schema);


for element in data:
    uri = element["URI"];
    g.add( [URIRef(uri), RDF.type, schema.Hotel ] )
    g.add( [URIRef(uri), RDFS.label, Literal( element["DENOMINAZIONE_STRUTTURA"] ) ] )
    g.add( [URIRef(uri), cmo.category, Literal( element["CATEGORIA"], lang='it' ) ] )
    g.add( [URIRef(uri), schema.starRating, Literal( element["CLASSIFICAZIONE"] ) ] )
    g.add( [URIRef(uri), schema.numberOfRooms, Literal( element["CAMERE"], datatype=XSD.string ) ] )
    g.add( [URIRef(uri), schema.address, Literal( element["INDIRIZZO"] ) ] )
    g.add( [URIRef(uri), cmo.localBusinessPostalCode, Literal( element["CAP"] ) ] )
    g.add( [URIRef(uri), schema.telephone, Literal( element["TEL"] ) ] )
    g.add( [URIRef(uri), schema.faxNumber, Literal( element["FAX"] ) ] )
    g.add( [URIRef(uri), schema.email, Literal( element["EMAIL"] ) ] )
    g.add( [URIRef(uri), cmo.localBusinessWebsite, Literal( element["WEB"] ) ] )
    g.add( [URIRef(uri), cmo.latitude, Literal( element["LAT"], datatype=XSD.string ) ] )
    g.add( [URIRef(uri), cmo.longitude, Literal( element["LONG"], datatype=XSD.string ) ] )
    
    uriToLink = link( element["DENOMINAZIONE_STRUTTURA"] )
    if ( uriToLink != "" ):
        g.add( [URIRef(uri), OWL.seeAlso, URIRef(uriToLink) ] )
    
g.serialize(destination=path+'/Turtles/hotel.ttl', format='turtle')
    