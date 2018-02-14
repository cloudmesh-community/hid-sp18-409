# swagger_client.CrimesApi

All URIs are relative to *https://localhost:8080/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**crimes_get**](CrimesApi.md#crimes_get) | **GET** /crimes | Crimes


# **crimes_get**
> list[Crime] crimes_get(latitude, longitude)

Crimes

The Crimes endpoint returns information about the crimes previously happened at a given location or nearby locations. The response includes lists of crimes in the proper display order.

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
api_instance = swagger_client.CrimesApi(swagger_client.ApiClient(configuration))
latitude = 1.2 # float | Latitude component of location.
longitude = 1.2 # float | Longitude component of location.

try:
    # Crimes
    api_response = api_instance.crimes_get(latitude, longitude)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CrimesApi->crimes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **latitude** | **float**| Latitude component of location. | 
 **longitude** | **float**| Longitude component of location. | 

### Return type

[**list[Crime]**](Crime.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

