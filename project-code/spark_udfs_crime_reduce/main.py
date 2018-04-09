from pyspark.sql import SparkSession
from pyspark.sql import Row

import pandas as pd

conf = "crimedata.csv"
saveFile = "crimedata_small.csv"
crimeByType = "crimeByType.csv"
crimeByLocation = "crimeByLocation.csv"
crimeByMonth = "crimeByMonth.csv"
crimeByMonthYear = "crimeByMonthArrested.csv"

def do_random_sampling(sampleSize):
    crimes = pd.read_csv(conf)
    print(crimes.head())
    random_subset = crimes.sample(n=sampleSize)
    random_subset.to_csv(saveFile, encoding='utf-8', index=False)

def reduce_crime_by_type():
    crimeData = pd.read_csv(conf, index_col='ID')
    total = crimeData.groupby('Primary Type', as_index=False).size().sort_values(ascending=False).to_frame('counts')
    total.T.to_csv(crimeByType, encoding='utf-8')


def reduce_crime_by_location():
    crimeData = pd.read_csv(conf, index_col='ID')
    total = crimeData.groupby('Location Description', as_index=False).size().sort_values(ascending=False).to_frame('counts')
    total.T.to_csv(crimeByLocation, encoding='utf-8')


def reduce_crime_by_month():
    crimeData = pd.read_csv(conf, index_col='Date')

    #total = crimeData.groupby('location_cat', as_index=False).size().sort_values(ascending=False).to_frame('counts')
    crimes = crimeData['ID']
    crimes.index = pd.to_datetime(crimes.index)
    print(crimes.head())
    total=crimes.resample('M').nunique()
    print(total.head())
    total.T.to_csv(crimeByMonth, encoding='utf-8')

def reduce_crime_by_month_arrested():
    crimeData = pd.read_csv(conf, index_col='Date')
    crimeData.index = pd.to_datetime(crimeData.index)
    crimes = crimeData[crimeData['Arrest'] == True]['Arrest']
    #total = crimeData.groupby('location_cat', as_index=False).size().sort_values(ascending=False).to_frame('counts')
    print(crimes.head())
    total=crimes.resample('M').sum()
    print(total.head())
    total.T.to_csv(crimeByMonthYear, encoding='utf-8')


#do_random_sampling(10000)
reduce_crime_by_type()
reduce_crime_by_location()
reduce_crime_by_month()
reduce_crime_by_month_arrested()


def process_data(line):
    fields = line.split(',')
    stationID = fields[0]
    entryType = fields[2]
    temperature = float(fields[3]) * 0.1 * (9.0 / 5.0) + 32.0
    return Row(ID=stationID, t_type=entryType, temp=temperature)


# Create a SparkSQL Session

spark = SparkSession.builder.appName('Simple SparkSQL UDF example'
        ).getOrCreate()

# Get the raw data

lines = spark.sparkContext.textFile('temperature_data.csv')

# Convert it to a RDD of Row objects
parsedLines = lines.map(process_data)

# alternative lamda fundtion
'''
parsedLines = lines.map(lambda line: Row(ID=line.split(',')[0],
                        t_type=line.split(',')[2],
                        temp=float(line.split(',')[3]) * 0.1 * (9.0
                        / 5.0) + 32.0))
'''

# Convert that to a DataFrame

TempDataset = spark.createDataFrame(parsedLines)

# show first 20 rows temperature converted data
# TempDataset.show()

# Some SQL-style magic to sort all movies by popularity in one line!

TempDatasetProcessed = TempDataset.where(TempDataset['t_type'] == 'TMAX'
        ).orderBy('temp', ascending=False).cache()

# show first 20 rows of filtered and sorted data

#TempDatasetProcessed.show()

			