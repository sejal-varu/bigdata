from mrjob.job import MRJob
from mrjob.step import MRStep

class TotalDistinctWords(MRJob):

	def steps(self):
		return[
			MRStep(mapper = self.map_line_to_words, 
				reducer=self.reducer_distinct_words),
			MRStep(mapper = self.map_distinct_word_to_one, 
				reducer=self.reduce_total_distinct_words)
		]

	def map_line_to_words(self, key, value):
		tokens = value.split(' ')
		for t in tokens:
			yield t , 'W'

	def reducer_distinct_words(self, key, values):
		yield key, 'DW'

	def map_distinct_word_to_one(self, key, values):
		yield 'DW',1

	def reduce_total_distinct_words(self, key, values):
		yield 'DWs', sum(values)


if __name__ == '__main__':
	TotalDistinctWords.run()
