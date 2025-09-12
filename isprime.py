# Check if a number is prime

def isPrime(num):
	if(num <= 1):
		return "not prime"
	for i in range(2, int(num**0.5) + 1):
		if (num %  i == 0):
			return "not prime"
	return "prime"

# Print all prime numbers up to n
num = 51
for i in range(num + 1):
	print(str(i) + ": " + isPrime(i))
