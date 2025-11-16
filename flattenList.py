nestedList = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o']]

flattened = []

for sublist in nestedList:
	for item in sublist:
		flattened.append(item)

print("Simple Loop:")		
print(flattened)

def recursiveFlatten(nestedList):
	flattened = []
	for item in nestedList:
		if isinstance(item, list):
			flattened.extend(recursiveFlatten(item))
		else:
			flattened.append(item)
	return flattened
	
print("Recursive Function")
print(recursiveFlatten(nestedList))
