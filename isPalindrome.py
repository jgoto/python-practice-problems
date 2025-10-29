str = "A man a plan a canal panama"

if str.lower().replace(" ", "") == "".join(reversed(str)).lower().replace(" ", ""):
	print(str + " is a palindrome")
else:
	print(str + " is not a palindrome")
