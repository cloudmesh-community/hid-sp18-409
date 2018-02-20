# swagger_client.SearchCrimesApi

All URIs are relative to *http://localhost:8080/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**crimes_search_get**](SearchCrimesApi.md#crimes_search_get) | **GET** /crimes/search | Search for a crime


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
api_instance = swagger_client.SearchCrimesApi(swagger_client.ApiClient(configuration))
crime_id = 'crime_id_example' # str | Unique identifier representing a specific crime according to chicago police.

try:
    # Search for a crime
    api_response = api_instance.crimes_search_get(crime_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchCrimesApi->crimes_search_get: %s\n" % e)
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

