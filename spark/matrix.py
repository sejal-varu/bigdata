from pyspark import SparkContext, SparkConf

conf = SparkConf()\
		.setAppName('Max Temp Yearly')\
		.setMaster('local')

sc = SparkContext(conf=conf)

m_path = '/home/sejal/Documents/datascience/dataset/data/matrix/m.txt'
n_path = '/home/sejal/Documents/datascience/dataset/data/matrix/n.txt'

m = sc.textFile(m_path)
n = sc.textFile(n_path)

mt = m.map(lambda entry: entry.split(','))
nt = n.map(lambda entry: entry.split(','))

mp = mt.map(lambda entry : (entry[1], (entry[0],int(entry[2])) ))
np = nt.map(lambda entry : (entry[0], (entry[1],int(entry[2])) ))

j = mp.join(np)

jv = j.values()

s1 = jv.map(lambda entry: ((entry[0][0], entry[1][0]) , entry[0][1]*entry[1][1]) )
s2 = s1.reduceByKey(lambda x,y : x + y )

ans = s2.map(lambda entry : (entry[0][0], entry[0][1], entry[1]) )

print('Matrix multiplied : ')
#print(ans.collect())

ans.saveAsTextFile('/tmp/matrix-spark/')


sc.stop()