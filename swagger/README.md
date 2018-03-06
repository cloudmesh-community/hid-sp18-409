# Swagger Codegen Assignment: Implemented a API to Identify crime prone areas near a GPS location
## Usage of Files and Data Structures using rest services hid-sp18-409 
* Pandas (open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language) will be used to manipulate the crime dataset available on https://catalog.data.gov/dataset/crimes-2001-to-present-398a4
* This crime dataset contains nearly 600,000(1.5GB) crime details across USA.
* For the sake of demonstration I have only used 10,000 crime details.
* Based on the GPS location of the user nearby crimes will be returned.

## Executing instructions
* you should be running this program in python 3 environment.
* git clone the project.
* change the directory to swaggerCodegen folder
* create the swagger server with following command
	* ```make service```
* run the swagger server with following command
	* ```make start```
* Install the client program using following command
	* ```make client```
* test the program using following command
	* ```make test```
* stop the service using following command
	* ```make stop```
* clean the server and client codes using following command
	* ```make clean```

## API informations and Results
* End Point : /crimes
* http://localhost:8080/v1/crimes?latitude=41.981398861&longitude=-87.754384567
	* The Crimes endpoint returns information about the crimes previously happened at a given location or nearby locations.
	* latitude and longitude should be passed with the request
	* The response includes lists of crimes in the proper display order
	* Nearby distance is defined in the program and currently defaulted to 0.1 Miles(528 foot).

### Sample json response for GET request on http://localhost:8080/v1/crimes?latitude=41.891398861&longitude=-87.744384567

```json
[
    {
        "arrested": "false",
        "beat_code": "1623",
        "block": "050XX W ARGYLE ST",
        "case_number": "HY198498",
        "community_area_code": "11",
        "crime_code": "0620",
        "crime_id": "10009166",
        "date": "03/25/2015 07:00:00 AM",
        "district_code": "016",
        "domestic": "false",
        "fbi_code": "05",
        "gps_location": "(41.971606007, -87.753880329)",
        "latitude": "41.971606007",
        "location_cat": "APARTMENT",
        "longitude": "-87.753880329",
        "primary_description": "BURGLARY",
        "secondary_description": "UNLAWFUL ENTRY",
        "updated_on": "02/10/2018 03:50:01 PM",
        "ward_code": "45",
        "x_coordinate": "1141823",
        "y_coordinate": "1932776",
        "year": "2015"
    },
    {
        "arrested": "false",
        "beat_code": "1621",
        "block": "060XX N CALDWELL AVE",
        "case_number": "HY195283",
        "community_area_code": "12",
        "crime_code": "1320",
        "crime_id": "10005335",
        "date": "03/11/2015 08:00:00 AM",
        "district_code": "016",
        "domestic": "false",
        "fbi_code": "14",
        "gps_location": "(41.991792049, -87.754907507)",
        "latitude": "41.991792049",
        "location_cat": "STREET",
        "longitude": "-87.754907507",
        "primary_description": "CRIMINAL DAMAGE",
        "secondary_description": "TO VEHICLE",
        "updated_on": "02/10/2018 03:50:01 PM",
        "ward_code": "45",
        "x_coordinate": "1141494",
        "y_coordinate": "1940130",
        "year": "2015"
    },
    {
        "arrested": "false",
        "beat_code": "1623",
        "block": "044XX N MILWAUKEE AVE",
        "case_number": "HY190143",
        "community_area_code": "15",
        "crime_code": "1310",
        "crime_id": "10000180",
        "date": "03/19/2015 04:29:00 AM",
        "district_code": "016",
        "domestic": "false",
        "fbi_code": "14",
        "gps_location": "(41.96085819, -87.754672619)",
        "latitude": "41.96085819",
        "location_cat": "COMMERCIAL / BUSINESS OFFICE",
        "longitude": "-87.754672619",
        "primary_description": "CRIMINAL DAMAGE",
        "secondary_description": "TO PROPERTY",
        "updated_on": "02/10/2018 03:50:01 PM",
        "ward_code": "45",
        "x_coordinate": "1141634",
        "y_coordinate": "1928858",
        "year": "2015"
    },
    {
        "arrested": "false",
        "beat_code": "1623",
        "block": "044XX N MILWAUKEE AVE",
        "case_number": "HY202063",
        "community_area_code": "15",
        "crime_code": "0320",
        "crime_id": "10012406",
        "date": "03/28/2015 07:30:00 PM",
        "district_code": "016",
        "domestic": "false",
        "fbi_code": "03",
        "gps_location": "(41.961001513, -87.754796331)",
        "latitude": "41.961001513",
        "location_cat": "APARTMENT",
        "longitude": "-87.754796331",
        "primary_description": "ROBBERY",
        "secondary_description": "STRONGARM - NO WEAPON",
        "updated_on": "02/10/2018 03:50:01 PM",
        "ward_code": "45",
        "x_coordinate": "1141600",
        "y_coordinate": "1928910",
        "year": "2015"
    },
    {
        "arrested": "true",
        "beat_code": "1623",
        "block": "044XX N MILWAUKEE AVE",
        "case_number": "HY197427",
        "community_area_code": "15",
        "crime_code": "1811",
        "crime_id": "10007602",
        "date": "03/25/2015 01:33:00 AM",
        "district_code": "016",
        "domestic": "false",
        "fbi_code": "18",
        "gps_location": "(41.961029065, -87.754818142)",
        "latitude": "41.961029065",
        "location_cat": "OTHER",
        "longitude": "-87.754818142",
        "primary_description": "NARCOTICS",
        "secondary_description": "POSS: CANNABIS 30GMS OR LESS",
        "updated_on": "02/10/2018 03:50:01 PM",
        "ward_code": "45",
        "x_coordinate": "1141594",
        "y_coordinate": "1928920",
        "year": "2015"
    },
    {
        "arrested": "false",
        "beat_code": "1623",
        "block": "051XX W LAWRENCE AVE",
        "case_number": "HY194086",
        "community_area_code": "11",
        "crime_code": "0820",
        "crime_id": "10004227",
        "date": "03/22/2015 02:00:00 AM",
        "district_code": "016",
        "domestic": "false",
        "fbi_code": "06",
        "gps_location": "(41.967935332, -87.755182208)",
        "latitude": "41.967935332",
        "location_cat": "STREET",
        "longitude": "-87.755182208",
        "primary_description": "THEFT",
        "secondary_description": "$500 AND UNDER",
        "updated_on": "02/10/2018 03:50:01 PM",
        "ward_code": "45",
        "x_coordinate": "1141478",
        "y_coordinate": "1931436",
        "year": "2015"
    },
    {
        "arrested": "true",
        "beat_code": "1624",
        "block": "050XX W MONTROSE AVE",
        "case_number": "HY195394",
        "community_area_code": "15",
        "crime_code": "1811",
        "crime_id": "10005445",
        "date": "03/23/2015 01:06:00 PM",
        "district_code": "016",
        "domestic": "false",
        "fbi_code": "18",
        "gps_location": "(41.960639162, -87.753685563)",
        "latitude": "41.960639162",
        "location_cat": "ALLEY",
        "longitude": "-87.753685563",
        "primary_description": "NARCOTICS",
        "secondary_description": "POSS: CANNABIS 30GMS OR LESS",
        "updated_on": "02/10/2018 03:50:01 PM",
        "ward_code": "45",
        "x_coordinate": "1141903",
        "y_coordinate": "1928780",
        "year": "2015"
    }
]
```
