num = "123456789" 

hidden = "*" * (len(num) - 4) + num[-4:]
print(hidden)
