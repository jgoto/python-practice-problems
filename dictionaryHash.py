text = "the quick red fox jumped over the lazy dog"

letters = {}

for ch in text:
	letters[ch] = letters.get(ch, 0) + 1

print(letters)
