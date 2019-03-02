from mrjob.job import MRJob


class GetCounts(MRJob):
	def mapper(self,key,value):
		tokens = value.split(',')
		if (len(tokens) == 4 and tokens[3] == "out"):
			try:
				user = str(tokens[0])
			except:
				pass
			else:
				yield user,1 #key , value (value can be list tuple)

	'''def combiner(self,key,values):  #IMP: values and not value
					yield key, 'W'
			'''
	def reducer(self,key,values):
		yield key, sum(values)

if __name__ == '__main__':
	GetCounts.run()
