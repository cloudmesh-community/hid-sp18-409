# swagger_client.CrimesApi

All URIs are relative to *http://localhost:8080/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**crimes_filter_get**](CrimesApi.md#crimes_filter_get) | **GET** /crimes/filter | crimeList based on primary_type
[**crimes_get**](CrimesApi.md#crimes_get) | **GET** /crimes | Crimes
[**crimes_search_get**](CrimesApi.md#crimes_search_get) | **GET** /crimes/search | Search for a crime


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
api_instance = swagger_client.CrimesApi(swagger_client.ApiClient(configuration))
latitude = 1.2 # float | Latitude component of location.
longitude = 1.2 # float | Longitude component of location.
primary_type = 'primary_type_example' # str | primary_type of a crime.

try:
    # crimeList based on primary_type
    api_response = api_instance.crimes_filter_get(latitude, longitude, primary_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CrimesApi->crimes_filter_get: %s\n" % e)
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

# **crimes_search_get**
> object crimes_search_get(crime_id)

Search for a crime

User can search for a perticluar crime with crime_id.

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
crime_id = 'crime_id_example' # str | Unique identifier representing a specific crime according to chicago police.

try:
    # Search for a crime
    api_response = api_instance.crimes_search_get(crime_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CrimesApi->crimes_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crime_id** | **str**| Unique identifier representing a specific crime according to chicago police. | 

### Return type

**object**

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

