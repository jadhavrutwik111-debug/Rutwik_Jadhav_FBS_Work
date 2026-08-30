nums = [2, 4, 3, 5, 7, 8]
target = 7

pairs = []
seen = set()

for num in nums:
    if target - num in seen:
        pairs.append((num, target - num))
    seen.add(num)

print("Pairs:", pairs)
