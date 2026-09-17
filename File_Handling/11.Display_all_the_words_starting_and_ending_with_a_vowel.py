f = open("sample.txt" , "r")

file = f.read()

words = file.split()

def Display_vowel_words(words):
    for word in words:
        if word[0] in "aeiou" and word[-1] in "aeiou":
            print(word)

Display_vowel_words(words)

f.close()