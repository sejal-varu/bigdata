
# from pyspark.sql import SparkSession
# from pyspark.sql.functions import *
# from pyspark.sql.types import *
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.tree import DecisionTree
from pyspark import SparkContext, SparkConf


conf = SparkConf()\
		.setMaster('local')\
		.setAppName('Hire OR no-Hire')

sc = SparkContext(conf = conf)


def prepare_data_for_DT(fields):
	years_of_exp = int(fields[0])
	employed = 1 if fields[1] == "Y" else 0
	previousEmployers = int(fields[2])
	if(fields[3] == "BS"):
		education_level = 1
	elif(fields[3] == "MS"):
		education_level = 2
	elif(fields[3] == "PHD"):
		education_level = 3
	else:
		education_level = 0

	if fields[4] == "Y":
		top_tier_school = 1
	else:
		top_tier_school = 0

	if fields[5] == "Y":
		internship = 1
	else:
		internship = 0

	if fields[6] == "Y":
		hired = 1
	else:
		hired = 0

	return LabeledPoint(hired, [years_of_exp,employed,previousEmployers,education_level,top_tier_school,internship])



path = '/home/sejal/Documents/datascience/dataset/data/emp/candidates_hired_past.csv'

r1 = sc.textFile(path)
r2 = r1.map(lambda entry: entry.split(','))

training_data = r2.map(prepare_data_for_DT)

test_data = [10,1,2,2,1,0]

model = DecisionTree.trainClassifier(training_data, numClasses=2, categoricalFeaturesInfo={1:2, 3:4,4:2,5:2})

predictions = model.predict(test_data)

print("Hire OR No-Hire")
print (predictions)

print (model.toDebugString())
# results = predictions.collect()

# for result in results:
# 	print result
