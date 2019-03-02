from pyspark import SparkContext, SparkConf

conf = SparkConf()\
		.setAppName('Max Temp Yearly')\
		.setMaster('local')

sc = SparkContext(conf=conf)

users_path = '/home/sejal/Documents/datascience/dataset/data/userComments/users.txt'
comments_path = '/home/sejal/Documents/datascience/dataset/data/userComments/users.txt'

r1 = sc.textFile(users_path)
r1kv = r1.map(lambda entry: (entry.split(',')[0],entry.split(',')[3]))


r2 = sc.textFile(comments_path)
r2kv = r2.map(lambda entry: (entry.split(',')[0],'C'))

ansRdd = r1kv.join(r2kv).values()
ans = ansRdd.countByKey()


print('Gender wise number of comments : ')
print(ans)

sc.stop()
