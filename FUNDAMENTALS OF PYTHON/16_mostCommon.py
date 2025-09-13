sentence = "ram is ram"

words = sentence.split()   
most_word = ""
max_count = 0

for i in words:
    c = words.count(i)   
    if c > max_count:
        max_count = c
        most_word = i

print("Most common word:", most_word)