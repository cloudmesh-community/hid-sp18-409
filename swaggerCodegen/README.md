# Rest Eve Assignment: Advanced version

## Executing instructions
* git clone the project and make sure rest eve is installed and available in your environment.
* run the run.py file.

## API informations

* http://127.0.0.1:5000/getcomputerInfor
	* Custom endpoint added to retrieve back-end computer/server information
	* GET request to the URL will send the information to client

### Sample json response for GET request on http://127.0.0.1:5000/getcomputerInfor

```json
{
    "name": "Kadupitiya",
    "processorName": "Intel64 Family 6 Model 79 Stepping 1, GenuineIntel",
    "ram": [
        34277974016,
        16897966080,
        50.7,
        17380007936,
        16897966080
    ],
    "disk": [
        2000397791232,
        58897731584,
        1941500059648,
        2.9
    ],
    "version": "10.0.15063",
    "system": "Windows",
    "node": "bl-sice-bl25cm2",
    "machine": "AMD64",
    "cpu_percent": 5.7
}
```

* http://127.0.0.1:5000/complexComputer
	* Custom endpoint added to showcase manual MongoDB insert/find functionalities, exception handling and custom josn message sending.
	* POST request to the URL with a json object {'name','yourName'} will manually store a new computer in mongoDB database.
	

### Sample success response for POST request on http://127.0.0.1:5000/complexComputer

```json
{
    "status": true,
    "message": "Success",
    "data": {
        "name": "Freddy",
        "processorName": "Intel64 Family 6 Model 79 Stepping 1, GenuineIntel",
        "ram": [
            34277974016,
            17398476800,
            49.2,
            16879497216,
            17398476800
        ],
        "disk": [
            2000397791232,
            58897735680,
            1941500055552,
            2.9
        ],
        "version": "10.0.15063",
        "system": "Windows",
        "node": "bl-sice-bl25cm2",
        "machine": "AMD64",
        "cpu_percent": 6
    },
    "error": null
}
```
### Sample error message response for POST request on http://127.0.0.1:5000/complexComputer

```json
{
    "status": false,
    "message": "Error occured",
    "data": null,
    "error": "E11000 duplicate key error collection: computer_information.computer index: name_1 dup key: { : \"Malintha\" }"
}
```

* http://127.0.0.1:5000/computer 
	* Eve resource API endpoint for computer resource
	* 'GET', 'POST', 'DELETE' are enabled for resource endpoint in settings.py
	* 'GET', 'PATCH', 'PUT', 'DELETE' item methods are also enabled.
	* settings.py showcase how to add resources and item methods using eve

### Sample json response for GET request on http://127.0.0.1:5000/computer

```json
{
    "_items": [
        {
            "_id": "5a739dbfcc32740a548e4154",
            "name": "Kadupitiya",
            "processorName": "Intel64 Family 6 Model 79 Stepping 1, GenuineIntel",
            "ram": [
                34277974016,
                17259327488,
                49.6,
                17018646528,
                17259327488
            ],
            "disk": [
                2000397791232,
                58897727488,
                1941500063744,
                2.9
            ],
            "version": "10.0.15063",
            "system": "Windows",
            "node": "bl-sice-bl25cm2",
            "machine": "AMD64",
            "cpu_percent": 8.5,
            "_created": "Thu, 01 Jan 1970 00:00:00 GMT",
            "_updated": "Thu, 01 Jan 1970 00:00:00 GMT",
            "_etag": "16495df63c4cd4546955a5633af034e7046a3202",
            "_links": {
                "self": {
                    "title": "computer",
                    "href": "computer/5a739dbfcc32740a548e4154"
                }
            }
        },
        {
            "_id": "5a739dc8cc32740a548e4155",
            "name": "Malintha",
            "processorName": "Intel64 Family 6 Model 79 Stepping 1, GenuineIntel",
            "ram": [
                34277974016,
                17220771840,
                49.8,
                17057202176,
                17220771840
            ],
            "disk": [
                2000397791232,
                58897727488,
                1941500063744,
                2.9
            ],
            "version": "10.0.15063",
            "system": "Windows",
            "node": "bl-sice-bl25cm2",
            "machine": "AMD64",
            "cpu_percent": 6.9,
            "_created": "Thu, 01 Jan 1970 00:00:00 GMT",
            "_updated": "Thu, 01 Jan 1970 00:00:00 GMT",
            "_etag": "ee7edf0104997fc099a14d96e68c7b1e0f9e8d1a",
            "_links": {
                "self": {
                    "title": "computer",
                    "href": "computer/5a739dc8cc32740a548e4155"
                }
            }
        }
    ],
    "_links": {
        "parent": {
            "title": "home",
            "href": "/"
        },
        "self": {
            "title": "computer",
            "href": "computer"
        }
    },
    "_meta": {
        "page": 1,
        "max_results": 25,
        "total": 2
    }
}
```

	
	