from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *


conf = SparkConf()\
		.setMaster('local')\
		.setAppName('Movie Analysis')


sc = SparkContext(conf = conf)

spark = SparkSession.builder\
		.appName('Movie analysis')\
		.master('local')\
		.getOrCreate()


movies_path = '/home/sejal/Documents/datascience/dataset/data/movielens/movies.dat'
users_path = '/home/sejal/Documents/datascience/dataset/data/movielens/users.dat'
ratings_path = '/home/sejal/Documents/datascience/dataset/data/movielens/ratings.dat'

# movies_df = spark.read.text(path)
moviesRdd = sc.textFile(movies_path)
movies = moviesRdd.map(lambda entry : entry.split("::"))\
				  .map(lambda tokens : (int(tokens[0]), tokens[1], tokens[2]))

sch_m = StructType([
	StructField('movie_id', LongType(), False),
	StructField('movie_title', StringType(), False),
	StructField('genres', StringType(), False)
	])



usersRdd = sc.textFile(users_path)
users = usersRdd.map(lambda entry : entry.split("::"))\
				  .map(lambda tokens : (int(tokens[0]), tokens[1], int(tokens[2]), int(tokens[3]), tokens[4]))

sch_u = StructType([
	StructField('user_id', LongType(), False),
	StructField('gender', StringType(), False),
	StructField('age_group', IntegerType(), False),
	StructField('occupation', IntegerType(), False),
	StructField('pincode', StringType(), False),
	])



ratingsRdd = sc.textFile(ratings_path)
ratings = ratingsRdd.map(lambda entry : entry.split("::"))\
				  .map(lambda tokens : (int(tokens[0]), int(tokens[1]), int(tokens[2]), int(tokens[3])))

sch_r = StructType([
	StructField('user_id', LongType(), False),
	StructField('movie_id', LongType(), False),
	StructField('ratings', IntegerType(), False),
	StructField('datetime', LongType(), False),
	])



movies_df = spark.createDataFrame(movies,schema=sch_m)
users_df = spark.createDataFrame(users,schema=sch_u)
ratings_df = spark.createDataFrame(ratings,schema=sch_r)

#get titles of movies who has ratings count more than 500

movies_rating = movies_df.join(ratings_df , movies_df.movie_id == ratings_df.movie_id )

top_movies = movies_rating.groupBy('movie_title')\
				.count()\
				.where('count > 500')\
				.orderBy(desc('count'))

ptm = top_movies.select(top_movies.movie_title.alias('most_rated_title'))

#Get Mean of rating Gender wise for all movie titles
#PIVOT
data = movies_rating.join(users_df, movies_rating.user_id == users_df.user_id)

d = data.join(ptm, data.movie_title == ptm.most_rated_title)\
		.select(d.movie_title, d.gender, d.ratings)

#Sort by most liked movie by Female
t = d.groupBy('movie_title')\
	.pivot('gender',['M','F'])\
	.mean('ratings')\
	.orderBy(desc('F'))

#Sort by most liked movie by male
t = d.groupBy('movie_title')\
	.pivot('gender',['M','F'])\
	.mean('ratings')\
	.orderBy(desc('M'))
