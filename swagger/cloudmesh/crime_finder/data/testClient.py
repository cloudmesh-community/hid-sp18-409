# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 20:29:18 2018

@author: jc
"""

from __future__ import print_function
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
######################################################################
# create an instance of the API class
######################################################################
api_instance = swagger_client.CrimesApi()

######################################################################
#test case 1: Api:  /crimes
######################################################################
print('test case 1: Api:  /crimes')
try:
    latitude=41.891398861
    longitude=-87.744384567
    api_response = api_instance.crimes_get(latitude,longitude)
    pprint(api_response)
except ApiException as e:
    print("Exception occured calling DefaultApi->cpu_get: %s\n" % e)
    
######################################################################    
#test case 2: Api:  /crimes/search
######################################################################
print('test case 2: Api:  /crimes/search')
try:
    crime_id='10007143'
    api_response = api_instance.crimes_search_get(crime_id)
    pprint(api_response)
except ApiException as e:
    print("Exception occured calling DefaultApi->cpu_get: %s\n" % e)

######################################################################
#test case 3: Api:  /crimes/filter 
######################################################################
print('test case 3: Api:  /crimes/filter')
try:
    latitude=41.891398861
    longitude=-87.744384567
    primary_type='BATTERY'
    api_response = api_instance.crimes_filter_get(latitude,longitude,primary_type)
    pprint(api_response)
except ApiException as e:
    print("Exception occured calling DefaultApi->cpu_get: %s\n" % e)
