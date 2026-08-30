strings = ["apple orange", "apple banana", "orange banana apple"]

words = []
for s in strings:
    words.extend(s.split())

unique_words = set(words)

freq = {}
for word in unique_words:
    
    freq[word] = words.count(word)

print("Unique words:", unique_words)
print("Frequency:", freq)