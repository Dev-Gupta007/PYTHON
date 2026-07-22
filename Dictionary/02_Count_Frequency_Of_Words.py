sentence = input("Enter the sentence: ")

words = sentence.split()
freq = {}

for i in words:
    freq[i] = words.count(i)

print(freq)