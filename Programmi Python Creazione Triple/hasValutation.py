import json
import geopy.distance
from scipy.stats import multivariate_normal
import os
import csv
path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)) )
file = open( path + "/report.txt", "w" )
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
    dataStruct = json.load( open( filename, "r" ) );
    structList = []
    
    for element in dataStruct:
        structList.append( triple( element["URI"], element["lat"], element["long"] ) )

    for dataHotel in hotelList:
        for struct in structList:
            #if( geopy.distance.distance( [dataHotel.latitude,dataHotel.longitude], [ struct.latitude, struct.longitude ] ).m <= 100 ):
            dist = geopy.distance.distance( [dataHotel.latitude,dataHotel.longitude], [ struct.latitude, struct.longitude ] ).m
            if( dataHotel.uri == "http://comune.milano.it/resource/hotel/flora" and dist <= 500 ):
                   file.write( dataHotel.uri + " " + struct.uri );
            if( dataHotel.uri == "http://comune.milano.it/resource/hotel/una_hotel_century" and dist <= 500 ):
                   file.write( dataHotel.uri + " " + struct.uri );
            if( dataHotel.uri == "http://comune.milano.it/resource/hotel/hotel_execelsior_gallia" and dist <= 500 ):
                   file.write( dataHotel.uri + " " + struct.uri );
            if ( dist <= 1 ):
                dataHotel.value += coeff * mvar.pdf([ struct.latitude, struct.longitude ])                   
            else:
                dataHotel.value += coeff * mvar.pdf([ struct.latitude, struct.longitude ]) / dist
    
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
definitiveFile = []
temp = {}

hotelList = []
for quadrupla in dataHotel:
    hotelList.append( hotel( quadrupla["URI"], quadrupla["LAT"], quadrupla["LONG"], 0, quadrupla["CLASSIFICAZIONE"] ) )

#fileDict = {"Monument":13,"ParkPublic":6,"Bar":8,"Pub":9,"FastFood":7,"Parking":1,"Restaurant":12,"BusStation":10,"SubwayStation":11,"RailwayStation":5,"CarRental":2,"BikeRental":3,"CarSharing":4}
fileDict = {"Monument":20,"Restaurant":12,"SubwayStation":11}

valutation = open (path+'/Turtles/HotelValue.csv', "w");
fieldnames = {"Hotel" : "" ,"Valutazione" : 0}
writer = csv.DictWriter( valutation, fieldnames=fieldnames , lineterminator='\n' );
writer.writeheader();

for key in fileDict.keys():
    hotelList = valuta( hotelList, path + "/DatiPerElaborazione/" + key + ".geojson", fileDict[key] )

for element in hotelList:
    temp.update( { "URI":element.uri } )
    stars = getDigitFromString( element.starRating );
    value =  (float(element.value))/43

    row = fieldnames.copy()
    row["Hotel"] = element.uri
    row["Valutazione"] = value
    writer.writerow( row );
    
    temp.update( { "value":value } )
    
    definitiveFile.append( temp );
    temp = {}

with open(path + '/Turtles/HotelValue.json', 'w') as outfile:  
    json.dump(definitiveFile, outfile)

valutation.close()
file.close()

