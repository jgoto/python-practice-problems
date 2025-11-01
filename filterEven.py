def is_even(num):
	if(num % 2 == 0):
		return True
	else:
		return False
		
nums = []

for n in range(1, 101):
	nums.append(n)

evens = list(filter(is_even, nums))

print("Even by Filtering")
print(evens)

print("Odd by Comprehension")
print([n for n in nums if n % 2 == 1])
