import math
# Part 2 of the Python Review lab.
def is_prime(x):
	#print(math.sqrt(x))
	for i in range(2, int(math.sqrt(x))):
		if x%i == 0:
			#print("a")
			return False
	#print("Works")
	return True

def encode(x, y):
	while not is_prime(x):
		x += 1
	while not is_prime(y):
		y += 1
	print("X is", x)
	print("Y is", y)
	if 1<y and y<250 and 500<x and x<1000:
		print("Y u no work?")
		return x*y
	print("Invalid input: Outside range.")
	return None

def decode(coded_message):
	print("The coded message is", coded_message)
	temp = 0
	fin = 0
	for i in range(2,coded_message):
		temp = coded_message%i
		if  is_prime(i) and coded_message%i == 0:
			print(i, coded_message/i)
			break

decode(encode(502, 100))

# we have twp prime numbers that have been multiplied and we want to take the product of them and find the original two numbers