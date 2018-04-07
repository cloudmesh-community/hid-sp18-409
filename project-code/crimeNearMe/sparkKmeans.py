import pandas as pd
import numpy as np
from pyspark import SparkContext
from pyspark.mllib.clustering import KMeans, KMeansModel
import shutil
import random

conf="data/crime_list.csv"
conf2="data/crimedata_small.csv"

crime_list = {}

sc = SparkContext(appName="KMeansExample")  # SparkContext

def loadCrimeNames():
    with open(conf, encoding='ascii', errors='ignore') as f:
        for line in f:
            line = line.rstrip()
            fields = line.split(',')
            crime_list[fields[0]] = (fields[1], fields[2])
    return crime_list


def get_time_in_sec(time_str):
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

def selectDataForClusting():
    crimeDataObj = pd.read_csv(conf2, index_col='crime_id',
                            names=['crime_id', 'case_number', 'date', 'block', 'crime_code', 'primary_description',
                                   'secondary_description', 'location_cat', 'arrested', 'domestic', 'beat_code',
                                   'district_code', 'ward_code', 'community_area_code', 'fbi_code', 'x_coordinate',
                                   'y_coordinate', 'year', 'updated_on', 'latitude', 'longitude', 'gps_location'])

    crimeDate=crimeDataObj['date'].copy().iloc[1:]
    crimeArrested=crimeDataObj['arrested'].copy().iloc[1:]
    crimedDomestic= crimeDataObj['domestic'].copy().iloc[1:]
    crimedDes = crimeDataObj['primary_description'].copy().iloc[1:]
    crimeLatitude = crimeDataObj['latitude'].copy().iloc[1:]
    crimeLongitude = crimeDataObj['longitude'].copy().iloc[1:]

    dateObj=[ get_time_in_sec(str(v)[11:19]) for k, v in crimeDate.items() if len(str(v)) > 19]
    arrObj = [ 1 if v == 'true' else 2 for k, v in crimeArrested.items()]
    domObj = [1 if v == 'true' else 2 for k, v in crimedDomestic.items()]
    #domOtemp = [1 for k, v in crimedDomestic.items()]
    desObj = [crime_list[v][0] for k, v in crimedDes.items()]
    latiObj = [float(v) for k, v in crimeLatitude.items()]
    longObj = [float(v) for k, v in crimeLongitude.items()]
    combined = (dateObj,arrObj,domObj,desObj)
    combinedT = np.array(combined).T
    #combinedT = combinedT[~combinedT.isnan(combinedT).any(axis=1)]

    #print(combinedT)
    return combinedT


def convertCrimeDataToClusterObj(dateText, arrestedObj, domesticObj, descriptionText):
    dateObj = get_time_in_sec(str(dateText)[11:19])
    arrObj = 1 if arrestedObj == 'true' else 2
    domObj = 1 if domesticObj == 'true' else 2
    desObj = crime_list[descriptionText][0]
    return (dateObj,arrObj,domObj,desObj)


def kmeans_train():
    shutil.rmtree('data/KMeansModel',ignore_errors=True)
    #sc = SparkContext(appName="KMeansExample")  # SparkContext
    rdd = sc.parallelize(selectDataForClusting())
    # Build the model (cluster the data)
    clusters = KMeans.train(rdd, 27, maxIterations=1, initializationMode="random")
    #for x in clusters.clusterCenters: print(x)
    clusters.save(sc, "data/KMeansModel")



def kmeans_predic_cluster(dateText, arrestedObj, domesticObj, descriptionText):
    #sc = SparkContext(appName="KMeansExample")  # SparkContext
    # clusters.save(sc, "data/KMeansModel")
    sameModel = KMeansModel.load(sc, "data/KMeansModel")
    #for x in sameModel.clusterCenters: print(x)
    center = sameModel.centers[sameModel.predict(convertCrimeDataToClusterObj(dateText, arrestedObj, domesticObj, descriptionText))]
    #print(center)
    return center

def kmeans_predic_clusterr(dateText, arrestedObj, domesticObj, descriptionText):
    return True if random.sample(range(1, 100), 1)[0] < 95 else False


loadCrimeNames()
#kmeans_train()
#kmeans_predic_cluster("03/18/2015 07:44:00 PM","true","true","ARSON")

#selectDataForClusting()




