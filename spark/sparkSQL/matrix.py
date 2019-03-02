from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import *

spark = SparkSession.builder\
		.appName('Martix')\
		.master('local')\
		.getOrCreate()

m_path = '/home/sejal/Documents/datascience/dataset/data/matrix/m.txt'
n_path = '/home/sejal/Documents/datascience/dataset/data/matrix/n.txt'

sch_m = StructType([
	StructField('mr', IntegerType(), False),
	StructField('mc', IntegerType(), False),
	StructField('mv', IntegerType(), False)
	])

sch_n = StructType([
	StructField('nr', IntegerType(), False),
	StructField('nc', IntegerType(), False),
	StructField('nv', IntegerType(), False)
	])

m = spark.read.csv(m_path, schema = sch_m)
n = spark.read.csv(n_path, schema = sch_n)


j = m.join(n , m.mc == n.nr )

s1 = j.select(j.mr.alias('r'), j.nc.alias("c"), (j.mv*j.nv).alias('v') )


ans = s1.groupBy('r','c')\
		.agg({'v':'sum'})

cols = ans.coalesce(1)
cols.write.csv('/tmp/sparksql/matrix')

spark.stop()