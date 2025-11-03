a = {1: "Bob", 2: "Jill", 3: "Dave", 4: "Sally", 5: "Mary"}
b = {1: "Lisa", 2: "Don", 3: "Sally", 4: "Dave", 5: "Bob"}

common_values = set(a.values()) & set(b.values())

print(common_values)
