from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import *

spark = SparkSession.builder\
		.appName('Facebook')\
		.master('local')\
		.getOrCreate()

path = '/home/sejal/Documents/datascience/dataset/data/facebook_logs'

sch = StructType([
	StructField('username', StringType(), False),
	StructField('action_date', DateType(), False),
	StructField('action_time', StringType(), False),
	StructField('action', StringType(), True)
	])

df = spark.read.csv(path, schema = sch)
cdf = df.dropna()

#Method - 1
sdf = cdf.select(cdf.username,cdf.action)\
		.where(cdf.action == 'out')\
		.groupBy('username')\
		.agg({'action' : 'count'})
		


sdf.write.csv('/tmp/sparksql/facebook')

spark.stop()



