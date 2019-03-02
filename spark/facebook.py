from pyspark import SparkContext, SparkConf

conf = SparkConf()\
		.setAppName('Max Temp Yearly')\
		.setMaster('local')

sc = SparkContext(conf=conf)
path = '/home/sejal/Documents/datascience/dataset/data/facebook_logs/'
rdd = sc.textFile(path)

ansRdd = rdd.map(lambda line:line.split(','))\
	.filter(lambda tokens : tokens[3] == 'out')\
	.map(lambda tokens : (tokens[0],tokens[3]))\
	.countByKey()


print('Facebook logout counts : ')
print(ansRdd)

sc.stop()