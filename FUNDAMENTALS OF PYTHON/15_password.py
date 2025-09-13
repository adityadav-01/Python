password = input("Enter your password: ")

has_upper = any(ch.isupper() for ch in password)
has_digit = any(ch.isdigit() for ch in password)
has_special = any(not ch.isalnum() for ch in password)

if has_upper and has_digit and has_special and len(password) >= 6:
    print("Strong Password")
else:
    print("Weak Password")


# second method 

password = input("Enter your password: ")

has_upper = False
has_digit = False
has_special = False

for ch in password:
    if ch.isupper():
        has_upper = True
    if ch.isdigit():
        has_digit = True
    if not ch.isalnum():   
        has_special = True

if has_upper and has_digit and has_special and len(password) >= 6:
    print("Strong Password")
else:
    print("Weak Password")