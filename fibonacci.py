# Print the Fibonacci sequence up to n
# f(n) = f(n-1) + f(n-2)
# f(0) = 0 
# f(1) = 1

def getFibonacci(num):
	if num == 0:
		return 0
	elif num == 1:
		return 1
	else:
		return (getFibonacci(num - 1) + getFibonacci(num - 2))
		
for i in range(15):
	print(getFibonacci(i))
