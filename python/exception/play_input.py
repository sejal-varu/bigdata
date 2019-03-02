print 'Program starts'
n = raw_input('Enter n : ')

try :
	i = int(n)
except ValueError:
	#Executes when error
	print 'Hey! Please enter numerals only'
else:
	#Executes when no error raised in corresponding try block
	print 'The number is ', i
print 'Program ends'