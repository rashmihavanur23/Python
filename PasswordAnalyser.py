pw = input("Enter your password: ")
print("Password Analysis: ")

list = []
if any(i.islower() for i in pw):
    print("✔ Password contains lowercase letters")
    a = "True"
    list.append(a)
else:
    print("✖ Password does not contain lowercase letters")
    a = "False"
    list.append(a)
if any(i.isupper() for i in pw):
    print("✔ Password contains uppercase letters")
    b = "True"
    list.append(b)
else:
    print("✖ Password does not contain uppercase letters")
    b = "False"
    list.append(b)
if any(i.isdigit() for i in pw):
    print("✔ Password contains numbers")
    c = "True"
    list.append(c)
else:
    print("✖ Password does not contain numbers")
    c = "False"
    list.append(c)
if any(i.isalnum() for i in pw):
    print("✔ Password contains special characters")
    d = "True"
    list.append(d)
else:
    print("✖ Password does not contain special characters")
    d = "False"
    list.append(d)
if len(pw) == 8:
    print("✔ Length of the character is valid")
    e = "True"
    list.append(e)
elif len(pw) > 8:
    print("✖ Length of the character is not valid")
    e = "False"
    list.append(e)
else:
    print("✖ Length of the character is not valid")
    e = "False"
    list.append(e)

count = list.count("True")
if count == 5:
    print("Password Strength = STRONG")
elif count <= 2:
    print("Password Strength = WEAK")
else :
    print("Password Strength = MEDIUM")

 

 


