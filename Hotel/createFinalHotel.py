from linking import get_cosine
import json
from getUri import urify
import sys
import geopy.distance as dist

import os
path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)) )

filename = path + "/Hotel/MilanHotel.geojson"
finalFileName = path + "/Hotel/MilanHotel.geojson"

filename1 = path + "/Hotel/FinalFlatMilanHotel.geojson"
filename2 = path + "/Hotel/FinalFlatHotelMilano2018.geojson"
filename3 = path + "/Hotel/FinalFlatDs48HotelFile.geojson"
finalFileName = path + "/Hotel/UncleanedHotel.geojson"

class Hotel:
    
    def __init__( self, latitude, longitude, categoria, classificazione, camere, cap, web, email, tel, fax, denominazione, indirizzo ):
        self.latitude = latitude
        self.longitude = longitude
        self.categoria = categoria
        self.classificazione = classificazione
        self.camere = camere
        self.cap = cap
        self.web = web
        self.email = email
        self.tel = tel
        self.fax = fax
        self.denominazione = denominazione
        self.indirizzo = indirizzo
    
    def __eq__( self, other ):
#        if ( isinstance( other, Hotel ) and dist.distance( [ self.latitude, self.longitude ],[ other.latitude, other.longitude ] ).m < 50 and get_cosine( self.denominazione, other.denominazione ) >= 0.75 ):
        if ( isinstance( other, Hotel ) and get_cosine( self.denominazione, other.denominazione ) >= 0.65 ):
        #if ( isinstance( other, Hotel ) and get_cosine( self.denominazione, other.denominazione ) >= 0.75 ):
            return True
        else:
            return False
        
    def __hash__( self ):
        return 0

def find ( hotelSet, hotel ):
    for currentHotel in hotelSet:
        if ( hotel.__eq__(currentHotel) ):
            return currentHotel

hotel2 = json.load( open( filename2, "r" ) );
hotel1 = json.load( open( filename1, "r" ) );
hotel3 = json.load( open( filename3, "r" ) );

nameSet = set();
hotelSet = set();

for element in hotel1:
    currentHotel = Hotel( element["LAT"], element["LONG"], element["CATEGORIA"], element["CLASSIFICAZIONE"], element["CAMERE"], element["CAP"], element["WEB"], element["EMAIL"], element["TEL"], element["FAX"], element["DENOMINAZIONE_STRUTTURA"], element["INDIRIZZO"] )    
    hotelSet.add( currentHotel )
        
for element in hotel2:
    currentHotel = Hotel( element["LAT"], element["LONG"], element["CATEGORIA"], element["CLASSIFICAZIONE"], element["CAMERE"], element["CAP"], element["WEB"], element["EMAIL"], element["TEL"], element["FAX"], element["DENOMINAZIONE_STRUTTURA"], element["INDIRIZZO"] )    
    if ( currentHotel in hotelSet ):

        oldHotel = find( hotelSet,currentHotel )
        if ( oldHotel.latitude == 0 ):
            oldHotel.latitude = currentHotel.latitude
        if ( oldHotel.longitude == 0 ):
            oldHotel.longitude = currentHotel.longitude
        if ( oldHotel.categoria == "" ):
            oldHotel.categoria = currentHotel.categoria
        if ( oldHotel.classificazione == "" ):
            oldHotel.classificazione = currentHotel.classificazione
        if ( oldHotel.camere == 0 ):
            oldHotel.camere = currentHotel.camere
        if ( oldHotel.cap == "" ):
            oldHotel.cap = currentHotel.cap
        if ( oldHotel.web == "" ):
            oldHotel.web = currentHotel.web
        if ( oldHotel.email == "" ):
            oldHotel.email = currentHotel.email
        if ( oldHotel.tel == "" ):
            oldHotel.tel = currentHotel.tel
        if ( oldHotel.fax == "" ):
            oldHotel.fax = currentHotel.fax
        if ( oldHotel.denominazione == "" ):
            oldHotel.denominazione = currentHotel.denominazione
        if ( oldHotel.indirizzo == "" ):
            oldHotel.indirizzo = currentHotel.indirizzo
            
        print ( currentHotel.denominazione + "||" + find( hotelSet,currentHotel ).denominazione )
    else:
        hotelSet.add( currentHotel )

for element in hotel3:
    currentHotel = Hotel( element["LAT"], element["LONG"], element["CATEGORIA"], element["CLASSIFICAZIONE"], element["CAMERE"], element["CAP"], element["WEB"], element["EMAIL"], element["TEL"], element["FAX"], element["DENOMINAZIONE_STRUTTURA"], element["INDIRIZZO"] )    
    if ( currentHotel in hotelSet ):

        oldHotel = find( hotelSet,currentHotel )
        if ( oldHotel.latitude == 0 ):
            oldHotel.latitude = currentHotel.latitude
        if ( oldHotel.longitude == 0 ):
            oldHotel.longitude = currentHotel.longitude
        if ( oldHotel.categoria == "" ):
            oldHotel.categoria = currentHotel.categoria
        if ( oldHotel.classificazione == "" ):
            oldHotel.classificazione = currentHotel.classificazione
        if ( oldHotel.camere == 0 ):
            oldHotel.camere = currentHotel.camere
        if ( oldHotel.cap == "" ):
            oldHotel.cap = currentHotel.cap
        if ( oldHotel.web == "" ):
            oldHotel.web = currentHotel.web
        if ( oldHotel.email == "" ):
            oldHotel.email = currentHotel.email
        if ( oldHotel.tel == "" ):
            oldHotel.tel = currentHotel.tel
        if ( oldHotel.fax == "" ):
            oldHotel.fax = currentHotel.fax
        if ( oldHotel.denominazione == "" ):
            oldHotel.denominazione = currentHotel.denominazione
        if ( oldHotel.indirizzo == "" ):
            oldHotel.indirizzo = currentHotel.indirizzo
            
        print ( currentHotel.denominazione + "||" + find( hotelSet,currentHotel ).denominazione )
    else:
        hotelSet.add( currentHotel )

temp = {}
definitiveFile = []

for hotel in hotelSet:
    temp.update( { "DENOMINAZIONE_STRUTTURA":hotel.denominazione } )
    temp.update( { "CATEGORIA":hotel.categoria } )
    temp.update( { "CLASSIFICAZIONE":hotel.classificazione } )
    temp.update( { "CAMERE":hotel.camere } );
    temp.update( { "INDIRIZZO":hotel.indirizzo } );
    temp.update( { "CAP":hotel.cap} );
    temp.update( { "TEL":hotel.tel} );
    temp.update( { "FAX":hotel.fax} );
    temp.update( { "EMAIL":hotel.email} );
    temp.update( { "WEB":hotel.web} );
    temp.update( { "LAT":hotel.latitude } )
    temp.update( { "LONG":hotel.longitude } )
    temp.update( { "URI":urify( "hotel", hotel.denominazione ) } )
    #temp.update( { "COMUNE":"Milano" } )
    definitiveFile.append( temp );
    temp = {}

with open(finalFileName, 'w') as outfile:  
    json.dump(definitiveFile, outfile)

            
            
            
            
            
            
            
            
            
            