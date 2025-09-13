string = "PALLAVI"

vowels = "AEIOUaeiou"  
v_count = 0
c_count = 0

for ch in string:
    if ch in vowels:          
        v_count += 1
    else:                     
        c_count += 1

print("Vowels:", v_count)
print("Consonants:", c_count)
