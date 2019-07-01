python "./CarSharing/downloadCarSharing.py"

curl -l http://dati.comune.milano.it/dataset/802a1d1f-4203-44c9-b9f5-dd8aa1f6bc3c/resource/7a07abfb-6a0d-458d-9a91-e6eb5b1ba703/download/ferrovie_stazioni_milano.geojson > "./RailwayStation/RailwayStation.geojson"

curl -l http://dati.comune.milano.it/dataset/b7344a8f-0ef5-424b-a902-f7f06e32dd67/resource/dd6a770a-b321-44f0-b58c-9725d84409bb/download/tpl_metrofermate.geojson > "./SubwayStation/SubwayStation.geojson"

curl -l http://dati.comune.milano.it/dataset/ac494f5d-acd3-4fd3-8cfc-ed24f5c3d923/resource/7d21bd77-3ad1-4235-9a40-8a8cdfeb65a0/download/tpl_fermate.geojson > "./Bus/BusStation.geojson"

python "./Pub/downloadPub.py"

python "./FastFood/downloadFastFood.py"

python "./Bar/downloadBar.py"

python "./Restaurant/downloadRestaurant.py"

python "./Park/downloadPark.py"

python "./Parking/downloadParking.py"

python "./CarRental/downloadCarRental.py"

python "./BikeRental/downloadBikeRental.py"

curl -l https://dati.lombardia.it/api/views/2p47-g7cn/rows.csv?accessType=DOWNLOAD > "./Hotel/hotel_milano_2018.csv"
curl -l http://dati.comune.milano.it/dataset/fd725151-da06-4973-b4a9-6c41717e7db0/resource/d5edc7e1-557e-42ee-9123-5a0b30da6387/download/ds48_turismotempolibero_strutture-ricettive-alberghiere_2015.json > "./Hotel/ds48_turismotempolibero_strutture-ricettive-alberghiere_2015.json"
python "./Hotel/downloadMilanHotel.py"

curl -l https://www.dati.lombardia.it/resource/jrbq-nyaa.csv?COMUNE=Milano > "./Monument/Beni_culturali_Bella_Lombardia.csv"

curl -l dati.comune.milano.it/dataset/8920bbea-fe1a-4061-8c6e-0746d95316c1/resource/7cba11e7-c236-49a7-aef4-4db6329eec5d/download/parchi.geojson > "./Park/Park.geojson"

python "./Hotel/FromCsvToJson.py"

python "./Hotel/FromFlatHotelMilano2018ToFinalHotelMilano2018.py" 

python "./Hotel/aggiustaDs48HotelFile.py" 

python "./Hotel/FromGeoJsonToFlatGeoJsonMilanHotel.py" 

python "./Hotel/FromFlatMilanHotelToFinalFlatMilanHotel.py" 

python "./Hotel/createFinalHotel.py" 

python "./Hotel/clean.py"

python "./Monument/FromCsvToJson.py" 

python "./Monument/FromCleanedMonumentToFinalFlatMonument.py"

python "./Monument/clean.py"

python "./CarRental/FromCarRentalToFlatCarRental.py"

python "./CarRental/clean.py"

python "./BikeRental/FromBikeRentalToFlatBikeRental.py"

python "./BikeRental/clean.py"

python "./CarSharing/FromCarSharingToFlatCarSharing.py"

python "./CarSharing/clean.py"

python "./RailwayStation/FromRailwayStationToFinalRailwayStation.py"

python "./RailwayStation/clean.py"

python "./SubwayStation/FromeSubwayStationToFinalSubwayStation.py"

python "./SubwayStation/clean.py"

python "./Park/FromParkPublicToFinalParkPublic.py"

python "./Park/clean.py"

python "./Bus/FromBusStationToFlatBusStation.py"

python "./Bus/clean.py"

python "./Pub/FromPubToFlatPub.py"

python "./Pub/clean.py"

python "./FastFood/FromFastFoodToFlatFastFood.py"

python "./FastFood/clean.py"

python "./Parking/FromParkingToFlatParking.py"

python "./Parking/clean.py"

python "./Restaurant/FromRestaurantToFlatRestaurant.py"

python "./Restaurant/clean.py"

python "./Bar/FromBarToFlatBar.py"

python "./Bar/clean.py"

python "./Programmi Python Creazione Triple/ParkingTriple.py"

python "./Programmi Python Creazione Triple/PubTriple.py"

python "./Programmi Python Creazione Triple/FastFoodTriple.py"

python "./Programmi Python Creazione Triple/ParkPublicTriple.py"

python "./Programmi Python Creazione Triple/CarSharingTriple.py"

python "./Programmi Python Creazione Triple/CarRentalTriple.py"

python "./Programmi Python Creazione Triple/BikeRentalTriple.py"

python "./Programmi Python Creazione Triple/HotelTriple.py"

python "./Programmi Python Creazione Triple/RailwayTriple.py"

python "./Programmi Python Creazione Triple/SubwayTriple.py"

python "./Programmi Python Creazione Triple/MonumentTriple.py"

python "./Programmi Python Creazione Triple/RestaurantTriple.py"

python "./Programmi Python Creazione Triple/BarTriple.py"

python "./Programmi Python Creazione Triple/BusTriple.py"

python "./Programmi Python Creazione Triple/hasClose.py"

python "./Programmi Python Creazione Triple/hasValutation.py"

python "./Programmi Python Creazione Triple/AddValutation.py"