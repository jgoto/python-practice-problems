stack = []

while True:
	print("Enter a number: ")
	entry = input()
	
	if entry == "stop":
		break
	elif entry == "pop":
		if len(stack) > 0:
			print("removing " + str(stack.pop()))
	elif entry == "peek":
		if len(stack) > 0:
			print(stack[-1])
	else:
		try:
			num = int(entry)
			stack.append(num)
		except ValueError:
			print("Not a number")

print(stack)
