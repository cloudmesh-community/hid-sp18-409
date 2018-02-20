# swagger_client.FilterCrimesApi

All URIs are relative to *http://localhost:8080/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**crimes_filter_get**](FilterCrimesApi.md#crimes_filter_get) | **GET** /crimes/filter | crimeList based on primary_type


# **crimes_filter_get**
> list[Crime] crimes_filter_get(latitude, longitude, primary_type)

crimeList based on primary_type

The crimes/filter endpoint returns information about the crimes previously happened at a given location or nearby locations based on user's GPS coordinates and a primary_type (Example- BATTERY).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['server_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['server_token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.FilterCrimesApi(swagger_client.ApiClient(configuration))
latitude = 1.2 # float | Latitude component of location.
longitude = 1.2 # float | Longitude component of location.
primary_type = 'primary_type_example' # str | primary_type of a crime.

try:
    # crimeList based on primary_type
    api_response = api_instance.crimes_filter_get(latitude, longitude, primary_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilterCrimesApi->crimes_filter_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **latitude** | **float**| Latitude component of location. | 
 **longitude** | **float**| Longitude component of location. | 
 **primary_type** | **str**| primary_type of a crime. | 

### Return type

[**list[Crime]**](Crime.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

