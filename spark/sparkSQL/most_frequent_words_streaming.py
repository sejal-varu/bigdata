from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder\
		.appName('Frequent words streaming')\
		.master('local')\
		.getOrCreate()

lines = spark.readStream\
		.format('socket')\
		.option('host', 'localhost')\
		.option('port',9000)\
		.load()


words = lines.select(
	explode(split('value',' ')).alias('word'))

a = words.groupBy('word')\
		.count()\
		.orderBy(desc('count'))
q = a.writeStream\
	.outputMode('complete')\
	.format('console')\
	.start()


q.awaitTermination()