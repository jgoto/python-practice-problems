def makeString(**kwargs):
	str = ""
	for key, value in kwargs.items():
		str += key
		str += " "
		str += value
		str += " "		
	return str
		
print(makeString(first="She", second="sells", third="seashells", forth="by", fifth="the", sixth="seashore"))
		
