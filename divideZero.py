def divide_this(x, y):
	return x / y

try:
	print('15 / 6 = ' + str(round(divide_this(15, 6),2)))
	print('77 / 13 = ' + str(round(divide_this(77, 13),2)))
	print('100 / 0 = ' + str(round(divide_this(100, 0),2)))

except ZeroDivisionError:
	print('you cannot divide by zero')	
