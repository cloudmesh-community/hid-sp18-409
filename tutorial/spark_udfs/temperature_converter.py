from pyspark.sql import SparkSession
from pyspark.sql import Row


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

TempDatasetProcessed.show()

			