queue = []

while True:
	print("Enter a number")
	entry = input()
	if entry == "stop":
		print(queue)
		break
	elif entry == "pop":
		if len(queue) > 0:
			print("pop: " + queue[0])
			queue.pop(0)
	elif entry == "peek":
		if len(queue) > 0:
			print("peek: " + queue[0])
	else:
		try:
			num = str(entry)
			queue.append(num)
		except ValueError:
			print("not a number")
