nums = {1: 17, 2: 6, 3: 97, 4: 75, 5: 3, 6: 50}

max_key = max(nums, key=nums.get)
print(max_key)

high_keys = [k for k, v in nums.items() if v >= 50]

print(high_keys)
