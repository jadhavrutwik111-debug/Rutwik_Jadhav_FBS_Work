nums = [1, 2, 3, 4, 5, 6]
target = 10

result = set()

n = len(nums)
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if nums[i] + nums[j] + nums[k] == target:
                result.add(tuple(sorted((nums[i], nums[j], nums[k]))))

print("Combinations:", result)