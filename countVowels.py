text = "Long time no see!"
vowels = "aeiou"
count = 0

for char in text.lower():
	if char in vowels:
		count+=1
	
print('"' + text + '" has ' + str(count) + ' vowels')

