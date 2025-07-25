#  Store following word meanings in a python dictionary : 
# table : “a piece of furniture”, “list of facts & figures”
#  cat : “a small animal”

word_meanings = {
    "table": ["a piece of furniture", "list of facts & figures"],
    "cat": ["a small animal"]
}

# Print the dictionary
print("Dictionary of word meanings:")
for word, meanings in word_meanings.items():
    print(f"{word} : {', '.join(meanings)}")
