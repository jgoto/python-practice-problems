# Find the average of numbers in a list

nums = [13, 19, 16, 7, 9, 18]
print(round(sum(nums) / len(nums),2))

total, length = 0, 0

for n in nums:
	length += 1
	total += n
	
print(round(total / length, 2))
