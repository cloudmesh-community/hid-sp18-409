# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 20:29:18 2018

@author: jc
"""

from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = swagger_client.CrimesApi()
try:
    latitude=41.891398861
    longitude=-87.744384567
    api_response = api_instance.crimes_get(latitude,longitude)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->cpu_get: %s\n" % e)