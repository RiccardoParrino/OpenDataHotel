import json
from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import RDF, RDFS, FOAF, OWL, XSD, DC, DCTERMS
import os
path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)) )
valutationFile = json.load( open( path + "/Turtles/HotelValue.json", "r" ) );
g = Graph();
cmo = Namespace("http://www.comune.milano.it/ontology/");
schema = Namespace("https://schema.org/")
g.bind("cmo",cmo);
g.bind("schema", schema);
g.bind("schema", schema);
g.parse(path + "/Turtles/hotel.ttl", format="turtle")

for element in valutationFile:
    g.add( [ URIRef( element["URI"] ), cmo.hasValutation, Literal(element["value"], datatype=XSD.string) ] );

g.serialize(destination=path + '/Turtles/hotel.ttl', format='turtle')
