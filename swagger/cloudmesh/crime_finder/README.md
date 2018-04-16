# Swagger Codegen Assignment: Implemented a API to Identify crime prone areas near a GPS location
  
## Usage of Files and Data Structures using rest services hid-sp18-409

* Pandas (open source, BSD-licensed library providing
  high-performance, easy-to-use data structures and data analysis
  tools for the Python programming language) is used to
  manipulate the crime dataset available on
  <https://catalog.data.gov/dataset/crimes-2001-to-present-398a4>

* This crime dataset contains nearly 600,000(1.5GB) crime details
  across USA.

* For the sake of demonstration I have only used 10,000 crime details
  (<https://drive.google.com/a/kadupitiya.lk/uc?authuser=1&id=1AGjD-MWfqprIpX6wz-zC6mM8kxMr7ron&export=download>).

* Based on the GPS location of the user nearby crimes will be
  returned.
  
* Data files are downloaded from a URL provided in the config.yml file.

* Basic authentication is used for /data APIs.

* User roles and passwords are managed through credentials.yml file.

* Crime services are kept open without any authentication.

* Five API endpoints are provided.

  * ```data```
  
  * ```data/fetch```
  
  * ```crimes```
  
  * ```crimes/search```
  
  * ```crimes/filter```

## Instructions for docker installation

* git clone the project.
  * Alternatively you can also download the docker image from the docker hub. Then you dont need to do docker build.
  
  * ```docker pull kadupitiya/swagger```

* you should install docker.

* change the directory to **swagger/cloudmesh/crime_finder** folder.

* Build the docker image incuding the program using following make command
  
  * ```make docker-build```

* Start the service using following make command
  
  * ```make docker-start```

* Test the service using following curl commands
  
  ### Data Services 
  
  * ```curl -H "Authorization: Basic YWRtaW46MTIz" -H "Content-Type:application/json" -X GET http://localhost:8080/cloudmesh/crime_finder/data```
  
  * ```curl -H "Authorization: Basic YWRtaW46MTIz" -H "Content-Type:application/json" -X GET http://localhost:8080/cloudmesh/crime_finder/data/fetch```     
  
  ### Crime Services 
  
  * ```curl http://127.0.0.1:8080/cloudmesh/crime_finder/crimes?latitude=41.891398861&longitude=-87.744384567```
  
  * ```curl http://127.0.0.1:8080/cloudmesh/crime_finder/crimes/search?crime_id=10007143```
  
  * ```curl http://127.0.0.1:8080/cloudmesh/crime_finder/crimes?latitude=41.981398861&longitude=-87.754384567&primary_type=NARCOTICS```    

* Get the container ID using following command
  
  * ```docker ps```

* Stop the service using following commands
  
  * ```make docker-stop```

* Optional starting mechanism (interactive mode)
  
  * ```docker run --rm -it kadupitiya/swagger bash```
  
  * ```make start``` 
  
  * ```make stop```
	
## Instructions for ubuntu without docker

* you should be running this program in python 3 environment.

* you should have default-jre installed.

* git clone the project.

* change the directory to swagger folder

* create the swagger server with following command
  
  * ```make service```

* run the swagger server with following command
  
  * ```make start```

* Install the client program using following command
  
  * ```make client```

* test the program using following command
  
  * ```make test```
  
  * ```make test-data```
  
  * ```make test-data-fetch```

* stop the service using following command
  
  * ```make stop```

* clean the server and client codes using following command
  
  * ```make clean```

## API informations : Data Services

### End Point : data/fetch
  
  * This data fetch endpoint upload the csv datafile to the server using predeifned url
 
  * Sample curl request
	  * ```curl -H "Authorization: Basic YWRtaW46MTIz" -H "Content-Type:application/json" -X GET http://localhost:8080/cloudmesh/crime_finder/data/fetch```
  
  * Sample json response for GET request 
	```
	{
	  "message": "Data fetch successfull",
	  "status": true
	}

	```

### End Point : /data
  
  * The data endpoint returns a data object conataining information about dataset files
  
  * Sample curl request
	  * ```curl -H "Authorization: Basic YWRtaW46MTIz" -H "Content-Type:application/json" -X GET http://localhost:8080/cloudmesh/crime_finder/data```
 
  * Sample json response for GET request
	```
	{
	  "base_path": "data",
	  "filename": "data/crimedata_small.csv",
	  "filename_short": "data/crimedata_small.csv",
	  "url": "https://goo.gl/f2Ta3D"
	}

	```

## API informations : Crime Services

* End Point : /crimes
  
  * The Crimes endpoint returns information about the crimes
    previously happened at a given location or nearby locations.
  
  * latitude and longitude should be passed with the request
  
  * The response includes lists of crimes in the proper display order
  * Nearby distance is defined in the program and currently defaulted
    to 0.1 Miles(528 foot).
  
  * Sample curl request
	  * ```curl http://127.0.0.1:8080/cloudmesh/crime_finder/crimes?latitude=41.891398861&longitude=-87.744384567```
  
  * Sample json response for GET request
	
	```
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
		    .
		    .
		    .
		    .,
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
### End Point : /crimes/search
  
  * The crimes search endpoint returns information about a particular
    crime for a given crime_id.
  
  * The response includes a crime object in the proper display order
  
  * Sample curl request
	  * ```curl http://127.0.0.1:8080/cloudmesh/crime_finder/crimes/search?crime_id=10007143```
  
  * Sample json response for GET request
	
	```
		{
		  "arrested": "false",
		  "beat_code": "2522",
		  "block": "047XX W ARMITAGE AVE",
		  "case_number": "HY196370",
		  "community_area_code": "19",
		  "crime_code": "0820",
		  "crime_id": "10007143",
		  "date": "03/22/2015 12:00:00 PM",
		  "district_code": "025",
		  "domestic": "false",
		  "fbi_code": "06",
		  "gps_location": "(41.916951295, -87.744546501)",
		  "latitude": "41.916951295",
		  "location_cat": "STREET",
		  "longitude": "-87.744546501",
		  "primary_description": "THEFT",
		  "secondary_description": "$500 AND UNDER",
		  "updated_on": "02/10/2018 03:50:01 PM",
		  "ward_code": "31",
		  "x_coordinate": "1144498",
		  "y_coordinate": "1912877",
		  "year": "2015"
		}
	```

### End Point : /crimes/filter
  
  * The crimes endpoint returns information about the crimes
    previously happened at a given location or nearby locations
    filtered with crime type.
  
  * latitude, longitude and primary_type should be passed with the
    request.
  
  * The response includes lists of crimes in the proper display order
  
  * Nearby distance is defined in the program and currently defaulted
    to 0.1 Miles(528 foot).
  
  * Returned list only contained requested type of crimes.
  
  * Sample curl request
	  * ```curl http://127.0.0.1:8080/cloudmesh/crime_finder/crimes?latitude=41.981398861&longitude=-87.754384567&primary_type=NARCOTICS```
  
  * Sample json response for GET request
	
	```
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
		  .
		  .
		  .
		  .,
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
