# Part 3 of the Python Review
def is_prime(x):
	for i in range(2, int(math.sqrt(x))):
		if x%i == 0:
			return False
	return True

class Cipher:

	def __init__(self, secret_message, key, limit):
		if secret_message < 1 and key < 1:
			print("Invalid input: Keys and messages must be greater than one.")
		if not is_prime(secret_message) and not is_prime(key):
			print("Invalid input: Both key and message must be prime.")

	def encode(self):
		pass


class Decoder:

	def __init__(self, coded_message, limit):
		pass

	def decode(self):
		pass