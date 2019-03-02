def fibo(n):
	a, b = 0, 1 
	print a
	print b
	for no in range(1, n - 1): 
		c = a + b
		print c
		a = b
		b = c

def even_series(n):
	print range(0, n + 1, 2)