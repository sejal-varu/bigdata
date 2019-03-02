from student_ops import get_grade, get_details
from student import Student

name = raw_input('Enter name : ')
gender = raw_input('Enter gender : ')
marks = float(raw_input('Enter marks : '))

s1 = Student(name, gender, marks)
'''s1.name = name
s1.gender = gender
s1.marks = marks
'''
#print s1.name
#print s1.marks
#print s1.gender

print s1.get_grade()
print s1.get_details()
print s1.get_name_marks()

s2 = Student('sejal','f',50)
#print s2.name
#print s2.marks
#print s2.gender
print s2.get_grade()
print s2.get_details()

'''
s3 = Student('Jane')
print s3.get_grade()
print s3.get_details()
'''


'''
print s3.name
print s3.marks
print s3.gender

print id(s1)
print id(s2)

print 'Your Grade is : ', get_grade(marks)
print get_details(name, gender, marks)
'''