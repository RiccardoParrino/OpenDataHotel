from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import RDF, RDFS, FOAF, OWL, XSD, DC, DCTERMS
import json 
from linking import link
import os
path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)) )
data = json.load( open( path+"/DatiPerElaborazione/Restaurant.geojson", "r" ) );
g = Graph();

cmo = Namespace("http://www.comune.milano.it/ontology/");
schema = Namespace("https://schema.org/")
g.bind("cmo",cmo);
g.bind("schema", schema);


for element in data:
    uri = element["URI"];
    g.add( [URIRef(uri), RDF.type, schema.Restaurant ] )
    g.add( [URIRef(uri), RDFS.label, Literal( element["nome"] ) ] )
    g.add( [URIRef(uri), cmo.localBusinessWebsite, Literal( element["website"] ) ] )
    g.add( [URIRef(uri), cmo.localBusinessPostalCode, Literal( element["cap"] ) ] )
    g.add( [URIRef(uri), schema.address, Literal( element["indirizzo"] ) ] )
    g.add( [URIRef(uri), schema.servesCuisine, Literal( element["cucina"] ) ] )
    g.add( [URIRef(uri), cmo.latitude, Literal( element["lat"], datatype=XSD.float ) ] )
    g.add( [URIRef(uri), cmo.longitude, Literal( element["long"], datatype=XSD.float ) ] )
    
g.serialize(destination=path+'/Turtles/restaurant.ttl', format='turtle')
    