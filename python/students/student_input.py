from student_ops import get_grade, get_details

name = raw_input('Enter name : ')
gender = raw_input('Enter gender : ')
marks = float(raw_input('Enter marks : '))

print 'Your Grade is : ', get_grade(marks)
print get_details(name, gender, marks)