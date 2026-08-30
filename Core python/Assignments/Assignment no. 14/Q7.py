set1 = {1, 2, 3, 4, 5}
set2 = {2, 4, 6}

missing_in_set2 = set1 - set2
missing_in_set1 = set2 - set1

print("Missing in set2:", missing_in_set2)
print("Missing in set1:", missing_in_set1)