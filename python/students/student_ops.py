def get_grade(marks):
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

def get_details(name, gender, marks):
	details = 'Name:'  + name + '\nGender: ' + gender + '\nMarks : ' + str(marks)
	return	details
