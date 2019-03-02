from mrjob.job import MRJob


class GetDistinctWords(MRJob):
	def mapper(self,key,value):
		tokens = value.split(' ')
		for t in tokens:
			yield t , 'W'

	def combiner(self,key,values):  #IMP: values and not value
		yield key, 'W'

	def reducer(self,key,values):
		yield key, 'DW'

if __name__ == '__main__':
	GetDistinctWords.run()