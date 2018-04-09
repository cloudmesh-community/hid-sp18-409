import connexion
import six

from swagger_server.models.crime import Crime  # noqa: E501
from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.crime_list import CrimeList  # noqa: E501
from swagger_server import util

import swagger_server.controllers.util as utility

import pandas as pd
import numpy as np
import operator

# allowble Distance in miles 0.1 = 528 foot
allowbleDistance = 0.1
maxNumber = 10
crimeCountList = {}
plotByTime = ""
yearly = True

if utility.downloadData():
    dataFile = utility.getDataFilePath()
    crimeListFile = utility.getcrimeListPath()
else:
    import sys

    print('Initial download failed')
    sys.exit(1)

try:
    # static load, only happens in starting point of the server
    crimeData = pd.read_csv(dataFile, index_col='crime_id',
                            names=['crime_id', 'case_number', 'date', 'block', 'crime_code', 'primary_description',
                                   'secondary_description', 'location_cat', 'arrested', 'domestic', 'beat_code',
                                   'district_code', 'ward_code', 'community_area_code', 'fbi_code', 'x_coordinate',
                                   'y_coordinate', 'year', 'updated_on', 'latitude', 'longitude', 'gps_location'])
    # static load, only happens in starting point of the server
    crimeDataForTimeseries = pd.read_csv(dataFile, index_col='date',
                            names=['crime_id', 'case_number', 'date', 'block', 'crime_code', 'primary_description',
                                   'secondary_description', 'location_cat', 'arrested', 'domestic', 'beat_code',
                                   'district_code', 'ward_code', 'community_area_code', 'fbi_code', 'x_coordinate',
                                   'y_coordinate', 'year', 'updated_on', 'latitude', 'longitude', 'gps_location'])
								   
								   
    crimesListMeta = pd.read_csv(crimeListFile, header=None)
	
except FileNotFoundError:
    import sys
    import logging

    logging.error('Data files not found. Fetch the data first')
    sys.exit(1)


def crimes_get(latitude, longitude, radius):  # noqa: E501
    """Crimes

    The Crimes endpoint returns information about the crimes previously happened at a given location or nearby locations. The response includes lists of crimes in the proper display order. # noqa: E501

    :param latitude: Latitude component of location.
    :type latitude: float
    :param longitude: Longitude component of location.
    :type longitude: float

    :rtype: List[Crime]
    """
    global crimeData
    global allowbleDistance
    allowbleDistance = radius
    # search for non indexed item
    # selectedCrime=crimeData.loc[crimeData['case_number'] == 'HY189866']
    # search for indexed item
    # crime_id='10013788'
    # selectedCrime=crimeData.loc[crime_id]

    # fill NaN with 0 for json conversion
    crimeData = crimeData.fillna(0)

    crimeList = get_nearby_crime_sorted_ind(latitude, longitude, crimeData)

    return crimeList


def crimes_filter_get(latitude, longitude, primary_type, radius):  # noqa: E501
    """crimeList based on primary_type

    The crimes/filter endpoint returns information about the crimes previously happened at a given location or nearby locations based on user&#39;s GPS coordinates and a primary_type (Example- BATTERY). # noqa: E501

    :param latitude: Latitude component of location.
    :type latitude: float
    :param longitude: Longitude component of location.
    :type longitude: float
    :param primary_type: primary_type of a crime.
    :type primary_type: str

    :rtype: List[Crime]
    """
    # fill NaN with 0 for json conversion
    global crimeData
    global allowbleDistance
    allowbleDistance = radius
    crimeData = crimeData.fillna(0)

    crimeList = get_nearby_crime_sorted_ind(latitude, longitude, crimeData)

    selectedData = [crime for crime in crimeList if crime.primary_description == primary_type]

    return selectedData


def crimes_search_get(crime_id):  # noqa: E501
    """Search for a crime
    User can search for a perticluar crime with crime_id. # noqa: E501
    :param crime_id: Unique identifier representing a specific crime according to chicago police.
    :type crime_id: str
    :rtype: object
    """
    
    crimeObj = set_dataframe_toObject(crime_id,crimeData.loc[crime_id])
    
    return crimeObj

def crimes_list_get():  # noqa: E501
    """Get the basic crime list

    User can get metadata list using this API. # noqa: E501


    :rtype: object
    """
    crimeListFound = [CrimeList(row[0],int(row[1]),row[2]) for row_index,row in crimesListMeta.iterrows()]

    return crimeListFound
	

def crimes_byday_get(no_of_types):  # noqa: E501
    """Get the top x crimes by day

    User can get top x crimes by day using this API. # noqa: E501

    :param no_of_types: How many top crime categeries are required?
    :type no_of_types: int

    :rtype: str
    """
    global maxNumber
    global yearly
    global plotByTime
    yearly = False
    maxNumber = no_of_types
    countTimelyCrimes(sortedData)
    return 	plotByTime



def crimes_byyear_get(no_of_types):  # noqa: E501
    """Get the top x crimes by year

    User can get top x crimes by year using this API. # noqa: E501

    :param no_of_types: How many top crime categeries are required?
    :type no_of_types: int

    :rtype: str
    """
    global maxNumber
    global yearly
    global plotByTime
    yearly = True
    maxNumber = no_of_types
    countTimelyCrimes(sortedData)
    return 	plotByTime

def get_nearby_crime_sorted_ind(latitude, longitude, crimeData):
    """
    This function retuns nearby crime indexes
    """
    global allowbleDistance
    global sortedData
    lat = crimeData['latitude'].copy()
    long = crimeData['longitude'].copy()
    lat.pop('crime_id')
    long.pop('crime_id')

    km = haversine_np(lat.astype('float64'), long.astype('float64'), latitude, longitude)

    selectedData = dict((k, v) for k, v in km.items() if v <= allowbleDistance)

    sortedData = dict(sorted(selectedData.items(), key=operator.itemgetter(1)))

    crimeList = [set_dataframe_toObject(crimeID, crimeData.loc[crimeID]) for crimeID in sortedData.keys()]

    return crimeList



def set_dataframe_toObject(crime_id,selectedCrime):
    """
    convert pandas dataframe to python model object   
    """   
    return Crime(crime_id, selectedCrime['case_number'], selectedCrime['date'], selectedCrime['block'], 
      selectedCrime['crime_code'], selectedCrime['primary_description'], selectedCrime['secondary_description'],
      selectedCrime['location_cat'], selectedCrime['arrested'], selectedCrime['domestic'], selectedCrime['beat_code'], 
      selectedCrime['district_code'], selectedCrime['ward_code'], selectedCrime['community_area_code'], 
      selectedCrime['fbi_code'], selectedCrime['x_coordinate'], selectedCrime['y_coordinate'], selectedCrime['year'], 
      selectedCrime['updated_on'], selectedCrime['latitude'], selectedCrime['longitude'], selectedCrime['gps_location'])


def haversine_np(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)  

    """
    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = np.sin(dlat / 2.0) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2.0) ** 2

    c = 2 * np.arcsin(np.sqrt(a))
    miles = 3959 * c
    return miles

def resampler_for_year(input):
    """
    This function create the year object for plotting

    """
    global crimeCountList
    global maxNumber
    global plotByTime
    global yearly

    temp = crimeCountList.copy()
    indexedDates=input.index.values

    if(indexedDates.size>0):

        indexyear = str(indexedDates[0])

        if (yearly):
            indexyear = indexyear[0:4]
        else:
            indexyear = indexyear[0:10]

        for row_index, row in input.iteritems():
            temp[row] = temp[row] + 1
        # temp = sorted(temp.items(), key=lambda t: t[1], reverse=True)

        plotByTime = plotByTime + indexyear
        count = 0;

        for key, value in temp.items():
            if (count < maxNumber):
                plotByTime = plotByTime + "," + str(value)
                count = count + 1
            else:
                break

        plotByTime = plotByTime + "\n"

    return "done"

def countTimelyCrimes(sortedData):
    """
    This function does postprocessing for creating object for plotting

    """
    global plotByTime
    global yearly

    for row_index, row in crimesListMeta.iterrows():
        crimeCountList[row[0]] = 0

    data = crimeData.loc[sortedData.keys()]
    selectedData = crimeDataForTimeseries.loc[data['date']]
    selectedData = selectedData['primary_description']
    selectedData.index = pd.to_datetime(selectedData.index)
    count = 0
    plotByTime = "Time"
    for key, value in crimeCountList.items():
        if (count < maxNumber):
            plotByTime = plotByTime + "," + str(key).capitalize()
            count = count + 1
        else:
            break

    plotByTime = plotByTime + "\n"

    if(yearly):
        yearlyData = selectedData.resample('A').apply(resampler_for_year)
    else:
        dailyData = selectedData.resample('M').apply(resampler_for_year)

