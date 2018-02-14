# Swagger Codegen Assignment: Implemeted a API to Identify crime prone areas near a GPS location
## Usage of Files and Data Structures using rest services hid-sp18-409 
* Pandas (open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language) will be used to manipulate the crime dataset availble on https://catalog.data.gov/dataset/crimes-2001-to-present-398a4
* Based on the GPS location of the user nearby crimes will be returned.

## Executing instructions
* git clone the project.
* change the directory to server folder
* run the swagger server with following commands
* pip install -r requirements.txt
* python setup.py install
* python -m swagger_server

## API informations
* End Point : /crimes
* http://localhost:8080/v1/crimes?latitude=41.891398861&longitude=-87.744384567
	* The Crimes endpoint returns information about the crimes previously happened at a given location or nearby locations.
	* latitude and longitude should be passed with the request
	* The response includes lists of crimes in the proper display order

### Sample json response for GET request on http://localhost:8080/v1/crimes?latitude=41.891398861&longitude=-87.744384567

```json
{
    "arrested": "false",
    "beat_code": "1111",
    "block": "047XX W OHIO ST",
    "case_number": "HY189866",
    "community_area_code": "25",
    "crime_code": "041A",
    "crime_id": "10000092",
    "date": "03/18/2015 07:44:00 PM",
    "district_code": "011",
    "domestic": "false",
    "fbi_code": "04B",
    "gps_location": "(41.891398861, -87.744384567)",
    "latitude": "41.891398861",
    "location_cat": "STREET",
    "longitude": "-87.744384567",
    "primary_description": "BATTERY",
    "secondary_description": "AGGRAVATED: HANDGUN",
    "updated_on": "02/10/2018 03:50:01 PM",
    "ward_code": "28",
    "x_coordinate": "1144606",
    "y_coordinate": "1903566",
    "year": "2015"
  },
  {
    "arrested": "true",
    "beat_code": "1111",
    "block": "047XX W HURON ST",
    "case_number": "HY198490",
    "community_area_code": "25",
    "crime_code": "2016",
    "crime_id": "10008845",
    "date": "03/25/2015 07:45:00 PM",
    "district_code": "011",
    "domestic": "false",
    "fbi_code": "18",
    "gps_location": "(41.893187629, -87.744291004)",
    "latitude": "41.893187629",
    "location_cat": "SIDEWALK",
    "longitude": "-87.744291004",
    "primary_description": "NARCOTICS",
    "secondary_description": "MANU/DELIVER:PCP",
    "updated_on": "02/10/2018 03:50:01 PM",
    "ward_code": "28",
    "x_coordinate": "1144627",
    "y_coordinate": "1904218",
    "year": "2015"
  },
  {
    "arrested": "false",
    "beat_code": "1113",
    "block": "047XX W LAKE ST",
    "case_number": "HY198527",
    "community_area_code": "25",
    "crime_code": "0320",
    "crime_id": "10008900",
    "date": "03/25/2015 06:30:00 PM",
    "district_code": "011",
    "domestic": "false",
    "fbi_code": "03",
    "gps_location": "(41.886530554, -87.74438154)",
    "latitude": "41.886530554",
    "location_cat": "CTA GARAGE / OTHER PROPERTY",
    "longitude": "-87.74438154",
    "primary_description": "ROBBERY",
    "secondary_description": "STRONGARM - NO WEAPON",
    "updated_on": "02/10/2018 03:50:01 PM",
    "ward_code": "28",
    "x_coordinate": "1144619",
    "y_coordinate": "1901792",
    "year": "2015"
  },
  {
    "arrested": "true",
    "beat_code": "1113",
    "block": "047XX W FULTON ST",
    "case_number": "HY199349",
    "community_area_code": "25",
    "crime_code": "0486",
    "crime_id": "10010006",
    "date": "03/26/2015 03:55:00 PM",
    "district_code": "011",
    "domestic": "true",
    "fbi_code": "08B",
    "gps_location": "(41.885369529, -87.74434079)",
    "latitude": "41.885369529",
    "location_cat": "PARKING LOT/GARAGE(NON.RESID.)",
    "longitude": "-87.74434079",
    "primary_description": "BATTERY",
    "secondary_description": "DOMESTIC BATTERY SIMPLE",
    "updated_on": "02/10/2018 03:50:01 PM",
    "ward_code": "28",
    "x_coordinate": "1144633",
    "y_coordinate": "1901369",
    "year": "2015"
  },
  {
    "arrested": "false",
    "beat_code": "1111",
    "block": "047XX W OHIO ST",
    "case_number": "HY200226",
    "community_area_code": "25",
    "crime_code": "1154",
    "crime_id": "10011190",
    "date": "12/27/2014 09:00:00 AM",
    "district_code": "011",
    "domestic": "false",
    "fbi_code": "11",
    "gps_location": "(41.891402786, -87.744079693)",
    "latitude": "41.891402786",
    "location_cat": "RESIDENCE",
    "longitude": "-87.744079693",
    "primary_description": "DECEPTIVE PRACTICE",
    "secondary_description": "FINANCIAL IDENTITY THEFT $300 AND UNDER",
    "updated_on": "02/10/2018 03:50:01 PM",
    "ward_code": "28",
    "x_coordinate": "1144689",
    "y_coordinate": "1903568",
    "year": "2014"
  },
  {
    "arrested": "true",
    "beat_code": "1111",
    "block": "047XX W OHIO ST",
    "case_number": "HY198362",
    "community_area_code": "25",
    "crime_code": "2026",
    "crime_id": "10008745",
    "date": "03/25/2015 06:50:00 PM",
    "district_code": "011",
    "domestic": "false",
    "fbi_code": "18",
    "gps_location": "(41.891405304, -87.744035597)",
    "latitude": "41.891405304",
    "location_cat": "SIDEWALK",
    "longitude": "-87.744035597",
    "primary_description": "NARCOTICS",
    "secondary_description": "POSS: PCP",
    "updated_on": "02/10/2018 03:50:01 PM",
    "ward_code": "28",
    "x_coordinate": "1144701",
    "y_coordinate": "1903569",
    "year": "2015"
  },
  {
    "arrested": "true",
    "beat_code": "1113",
    "block": "047XX W WASHINGTON BLVD",
    "case_number": "HY198699",
    "community_area_code": "25",
    "crime_code": "1811",
    "crime_id": "10009039",
    "date": "03/26/2015 12:10:00 AM",
    "district_code": "011",
    "domestic": "false",
    "fbi_code": "18",
    "gps_location": "(41.881828579, -87.744171339)",
    "latitude": "41.881828579",
    "location_cat": "STREET",
    "longitude": "-87.744171339",
    "primary_description": "NARCOTICS",
    "secondary_description": "POSS: CANNABIS 30GMS OR LESS",
    "updated_on": "02/10/2018 03:50:01 PM",
    "ward_code": "28",
    "x_coordinate": "1144688",
    "y_coordinate": "1900079",
    "year": "2015"
  }
```
