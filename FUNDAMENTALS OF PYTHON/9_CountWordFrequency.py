sentence = "Ram is Ram"
words = sentence.split()

word_count = {}

for w in words:
    word_count[w] = word_count.get(w, 0) + 1

for k, v in word_count.items():
    print(f"{k} {v} times")



# or 

sentence = "Ram is Ram Ram"
words = sentence.split()   

for w in words:
    count = words.count(w)   
    print(w, "appears", count, "times")
