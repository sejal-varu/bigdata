class Account:
	def __init__(self,acc_no, acc_type, acc_bal):
		self.acc_no = acc_no 
		self.balance = acc_bal
		self.acc_type = acc_type

	def withdraw(self,amount):
		print 'Transaction Starts'
		try:
			if not (	isinstance(amount,float) or  isinstance(amount, int)):
				raise TypeError ('Invalid type of amount. Please enter numerals only')
			if self.balance - amount < 1000:
				raise ValueError ('Amount to be withdrawn causes overdraft in the account')
			self.balance -= amount
			return self.balance
		finally:
			print "Transaction Ends"

a = Account(12345,'savings',4000)
#with_amt = int(raw_input('Enter amount to withdraw'))

print a.withdraw(200)
