d = {'a': 1, 'b': 2, 'c': 3}

key = input("Enter key to remove: ")

if key in d:
    del d[key]
    print("Updated Dictionary:", d)
else:
    print("Key not found")