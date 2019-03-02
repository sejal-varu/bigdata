from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

spark = SparkSession.builder\
		.appName('Words')\
		.master('local')\
		.getOrCreate()


path = '/home/sejal/Documents/datascience/dataset/data/words'

lines_df = spark.read.text(path)

tmp = lines_df.select(\
	explode(split(lines_df.value," ")).alias("words"))


ans = tmp.groupby('words')\
	.count()\
	.orderBy(desc("count"))\
	.limit(5)

cols = ans.coalesce(1)
cols.write.csv('/tmp/sparksql/words')

spark.stop()