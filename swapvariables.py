# Swap two variables without using a temporary variable

a = "red"
b = "blue"

print(a + b)

a, b = b, a

print(a + b)
