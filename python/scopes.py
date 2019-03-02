length = 10 #global
breadth = 5 #global

def area():
	# in python global variables can be accessed
	#even in function defined in same file
	#only refer their values
	return length*breadth


def perimeter(length, breadth):
	# length and breadth are local here to perimeter function
	return 2 * (length + breadth)

print area()
print perimeter(5, 3)

x = 7 #global
y = 9
z = 5

def func():
	x = 9 #local scope
	print x # 9
	''' this is an error
	y = y + 10
	print y '''
	global z 
	''' modifies global variable z PLEASE DONT DO THIS BAD PRACTICE ''' 
	z = z * 3
	print z

func()
print x # 7
print y
print z #15

n = 10
if n % 2 == 0:
	msg = 'Is Even'
else:
	msg = 'Is odd'
'''In python only functions create scope,
Rest of block (if elif loops class)
do not create scope

Scope of variable is always nearest enclosing scope'''

print msg

