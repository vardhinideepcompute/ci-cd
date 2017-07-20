def is_prime(Number):
	print "Python file"
	for i in range(2,Number):
		if Number%i == 0:
			print "Not a prime"
			return False
	print "Prime number"
	return True
