length = float(raw_input('Enter Length : '))
breadth = float(raw_input('Enter breadth : '))

def perimeter(l = 3 , b = 2):
	#perimeter values to parameters of functions
	# default parameters cannot have non default
	# parameters decalred after it
	p = 2 *(l + b)
	return p

per = perimeter(length, breadth)
print per

print perimeter(6)
print perimeter(b = 2.75)

#keyword arguments
print perimeter(l=10, b=2)