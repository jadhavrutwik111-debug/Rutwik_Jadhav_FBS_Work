strings = ["flower", "flow", "flight"]

prefix = ""
for chars in zip(*strings):
    if len(set(chars)) == 1:
        prefix += chars[0]
    else:
        break

print("Longest Common Prefix:", prefix)