from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import *

spark = SparkSession.builder\
		.appName('Max Temp Yearly')\
		.master('local')\
		.getOrCreate()

path = '/home/sejal/Documents/datascience/dataset/data/weather_data'

sch = StructType([
	StructField('stationno', IntegerType(), False),
	StructField('year', IntegerType(), False),
	StructField('datemonth', StringType(), False),
	StructField('hourmin', StringType(), False),
	StructField('temprature', FloatType(), True)
	])

df = spark.read.csv(path, sep="|", schema = sch)
cdf = df.dropna()

#Method - 1
sdf = cdf.select(cdf.year,cdf.temprature)\
		.groupBy('year')\
		.agg({'temprature' : 'max'})

#Method - 2
sdf = cdf.select(cdf.year,cdf.temprature)\
		.groupBy('year')\
		.agg(F.max('temprature'))

#Method - 3
sdf = cdf.select(cdf.year,cdf.temprature)\
		.groupBy('year')\
		.max('temprature')

sdf.write.csv('/tmp/sparksql/weatherdata')

spark.stop()