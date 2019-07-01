import json
import geopy.distance
from scipy.stats import multivariate_normal
import os
import csv
path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)) )
file = open( path + "/report2.txt", "w" )
class hotel:
    def __init__( self, uri, latitude, longitude, value, starRating ):
        self.uri = uri
        self.latitude = latitude
        self.longitude = longitude
        self.value = value
        self.starRating = starRating
    
class triple:
    def __init__( self, uri, latitude, longitude ):
        self.uri = uri
        self.latitude = latitude
        self.longitude = longitude
      
def valuta ( hotelList, filename, coeff ):
    center = [45.464304, 9.189649]
    mvar = multivariate_normal(mean=center, cov=[[1,0],[0,1]])
    fileJson = open( filename, "r" )
    dataStruct = json.load( fileJson );
    structList = []
    print( filename )
    for element in dataStruct:
        structList.append( triple( element["URI"], element["lat"], element["long"] ) )

    for dataHotel in hotelList:
        for struct in structList:
            #if( geopy.distance.distance( [dataHotel.latitude,dataHotel.longitude], [ struct.latitude, struct.longitude ] ).m <= 100 ):
            #print(coeff * mvar.pdf([ struct.latitude, struct.longitude ]) / geopy.distance.distance( [dataHotel.latitude,dataHotel.longitude], [ struct.latitude, struct.longitude ] ).m)
            dist = geopy.distance.distance( [dataHotel.latitude,dataHotel.longitude], [ struct.latitude, struct.longitude ] ).m
            if ( dist <= 1000 ): 
                file.write( dataHotel.uri + " " + struct.uri + "\n");
            if ( dist <= 1 ):
                dataHotel.value += coeff * mvar.pdf([ struct.latitude, struct.longitude ])                   
            else:
                dataHotel.value += coeff * mvar.pdf([ struct.latitude, struct.longitude ]) / dist
    
    fileJson.close();
    return hotelList

def getDigitFromString ( classification ):
    counter = 0;
    stars = 0;
    classification = element.starRating
    while ( counter < len( classification ) ):
        if ( classification[counter].isdigit()  ):
            stars =  classification[counter];
        counter = counter + 1
    return stars


dataHotel = json.load( open( path + "/DatiPerElaborazione/Hotel.geojson", "r" ) );

hotelList = []
for quadrupla in dataHotel:
    if( quadrupla["URI"] == "http://comune.milano.it/resource/hotel/hotel_carlo_goldoni" or quadrupla["URI"] == "http://comune.milano.it/resource/hotel/grand_hotel_et_de_milan" or quadrupla["URI"] == "http://comune.milano.it/resource/hotel/hotel_brunelleschi" ):
        hotelList.append( hotel( quadrupla["URI"], quadrupla["LAT"], quadrupla["LONG"], 0, quadrupla["CLASSIFICAZIONE"] ) )

print( hotelList )

#fileDict = {"Monument":13,"ParkPublic":6,"Bar":8,"Pub":9,"FastFood":7,"Parking":1,"Restaurant":12,"BusStation":10,"SubwayStation":11,"RailwayStation":5,"CarRental":2,"BikeRental":3,"CarSharing":4}
fileDict = {"Monument":20,"Restaurant":12,"SubwayStation":11}

for key in fileDict.keys():
    hotelList = valuta( hotelList, path + "/DatiPerElaborazione/" + key + ".geojson", fileDict[key] )

for element in hotelList:
    stars = getDigitFromString( element.starRating );
    value =  (float(element.value))/43
    print( element.uri + " " + str(value) )
file.close()

