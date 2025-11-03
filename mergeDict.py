fruit = {1: "Apple", 2: "Pear", 3: "Cherry"}
vegitables = {4: "Carrot", 5: "Cabbage", 6: "Celery"}
fruitAndVeg = {**fruit, **vegitables}
print(fruitAndVeg)

moreFruit = {7: "tomato", 8: "Plum"}

fruitAndVeg = fruitAndVeg | moreFruit

print(fruitAndVeg)

moreVeg = {9: "Broccoli", 10: "Cauliflour"}

fruitAndVeg.update(moreVeg)

print(fruitAndVeg)
