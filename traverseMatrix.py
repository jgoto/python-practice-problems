import random

def getRandInt():
	return random.randint(1, 10)

def makeMatrix(size):
	matrix = [[None for _ in range(size)] for _ in range(size)]
	for row in range(size):
		for n in range(size):
			 matrix[row][n] = getRandInt()
	return matrix

def printMatrix(matrix):
	for row in matrix:
		for n in row:
			print(n, end=" ")
		print()
	print()

def totalMatrix(matrix):
	total = 0
	for row in matrix:
		for n in row:
			total += n
	return total
		
numMatrix = makeMatrix(5)
printMatrix(numMatrix)
total = totalMatrix(numMatrix)
print("Matrix total is:")
print(total)
