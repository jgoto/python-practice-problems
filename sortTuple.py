tupOne = (3, 4, 2)
tupTwo = (7, 1, 4)
tupThree = (8, 3, 6)

tupleList = [tupOne, tupTwo, tupThree]

print(tupleList)
tupleList.sort(key = lambda x: x[1])
print(tupleList)
