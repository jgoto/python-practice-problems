print("Enter a number between 1 and 100")

try:
	num = int(input())
	if num > 0 and num <= 100:
		print(str(num) + ": is valid")
	else:
		print(str(num) + ": is not valid")
		
except ValueError:
	print("not a number")

