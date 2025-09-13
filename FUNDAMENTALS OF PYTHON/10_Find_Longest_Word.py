sentence = "python is programmming laanguage"
words = sentence.split()

longest = max(words, key=len)
print("Longest word is:", longest)