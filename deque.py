from collections import deque

queue = deque()

while True:
	print("Enter a number")
	entry = input()
	if entry == "stop":
		print(queue)
		break
	elif entry == "pop":
		if len(queue) > 0:
			queue.popleft()
	elif entry == "peek":
		if len(queue) > 0:
			print(queue[0])
	else:
		try:
			num = str(entry)
			queue.append(num)
		except ValueError:
			print("not a number")

