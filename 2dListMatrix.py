def printMatrix(matrix):
	for row in matrix:
		for val in row:
			print(val, end=" ")
		print()	

matrix = [
[3, 9, 2],
[5, 7, 1],
[8, 4, 6]
]

printMatrix(matrix)

matrix[1][2] = 19
matrix[0][0] = 0
matrix[2][1] = 99

print()

printMatrix(matrix)
