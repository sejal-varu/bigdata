from mrjob.job import MRJob


class MaxTempYearly(MRJob):
	def mapper(self,key,value):
		tokens = value.split('|')
		if (len(tokens) == 5):
			try:
				year = int(tokens[1])
				temp = float(tokens[4])
			except:
				pass
			else:
				yield year,temp #key , value (value can be list tuple)

	def combiner(self,key,values):  #IMP: values and not value
		yield key,max(values)

	def reducer(self,key,values):
		yield key,max(values)

if __name__ == '__main__':
	MaxTempYearly.run()