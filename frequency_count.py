char_dict = {}
text = "The quick red fox jumped over the lazy dog"
text = text.replace(" ","").lower()

for char in text:
	if char in char_dict:
		char_dict[char] += 1
	else:
		char_dict[char] = 1

for key, value in char_dict.items():
	print(key, ": ", value)



