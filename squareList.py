squares = []

for n in range(1, 13):
	squares.append([n, n*n])
	
for index, square in enumerate(squares):
	print(str(index) + ": " + str(square))
