marks = float(raw_input('Enter your marks : '))

if marks > 100 or marks < 0:
	print 'Invalid'
elif marks >= 70:
	print 'Grade A'
elif marks >= 60:
	print 'Grade B'
elif marks >= 40:
	print 'Grade C'
elif marks < 40:
	print 'Grade D'
else :
	print 'Weird !!'