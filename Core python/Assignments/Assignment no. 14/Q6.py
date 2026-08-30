nums = [1, 10, 2, 6, 5, 3]

nums_set = set(nums)
nums_list = sorted(nums_set)

max_product = nums_list[-1] * nums_list[-2]

print("Maximum product:", max_product)