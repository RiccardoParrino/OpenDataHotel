import overpass
import json
import os

path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)) )
api = overpass.API()
api = overpass.API(endpoint="https://overpass-turbo.eu")
api = overpass.API(timeout=25)
response = api.get("""nwr(around:10000,45.4637901,9.1895511)["amenity"="car_rental"];out center;""")

with open(path+"/CarRental/CarRental.geojson", 'w') as outfile:
    json.dump(response, outfile)