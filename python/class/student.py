class Student:
	def __init__(self, name, gender = None, marks = None):
		#constructors
		#Constructor Overloading
		self.name = name
		self.gender = gender
		self.marks = marks

	def get_grade(self):
		marks = self.marks
		if marks > 100 or marks < 0:
			return 'Invalid'
		elif marks >= 70:
			return 'Grade A'
		elif marks >= 60:
			return 'Grade B'
		elif marks >= 40:
			return 'Grade C'
		elif marks < 40:
			return 'Grade D'
		else :
			return 'Weird !!'
	
	def get_details(self):
		details = 'Name : ' + self.name + ' Gender : ' + self.gender + ' Marks: ' + str(self.marks)
		return details

	def get_name_marks(self):
		return (self.name, self.marks)