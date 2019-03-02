# ACTUAL LOGIC STARTS HERE
import series as ss
from series import even_series
from mypack.math import is_even_or_odd

while True:
	print '1 : FIbonacci series\n2 : Check Even/ Odd\n3 : Print Evens\n4 : Exit'

	choice = int(raw_input('Enter choice number :'))
	if not choice == 4:
		n = int(raw_input('Enter a number : '))
	if choice == 1:		
		#series.fibo(n)
		ss.fibo(n)
	elif choice == 2:
		is_even_or_odd(n)
	elif choice == 3:
		#series.even_series(n)
		even_series(n)
	elif choice == 4:
		break;