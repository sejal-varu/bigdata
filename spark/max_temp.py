from pyspark import SparkContext, SparkConf

conf = SparkConf()\
		.setAppName('Max Temp Yearly')\
		.setMaster('local')

sc = SparkContext(conf=conf)
path = '/home/sejal/Documents/datascience/dataset/data/weather_data/'
rdd = sc.textFile(path)

ansRdd = rdd.map(lambda line:line.split('|'))\
	.filter(lambda tokens : tokens[4] != '' and tokens[4] !='NA')\
	.map(lambda tokens : (int(tokens[1]),float(tokens[4])))\
	.reduceByKey(lambda temp1,temp2:max(temp1,temp2))

ans = ansRdd.collect()

print('Max temprature on yearly basis is : ')
print(ans)


sc.stop()