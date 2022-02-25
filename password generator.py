
import string
import random
import re
def strong(v):
    if v == "\n" or v == " ":
        return 0
   
    if 9 <= len(v) <= 20:
   
        if re.search(r'(.)\1\1', v):
            return 0
        if re.search(r'(..)(.*?)\1', v):
            return 0
        else:
            return 1
   
    else:
        return 0
def generate():
    l = int(input("Enter length of password:"))
    inp = input("Enter words:")
    chars = list(inp)
    random.shuffle(chars)
    password = []
    for i in range(l):
        password.append(random.choice(chars))
        random.shuffle(password)
        result = "".join(password)
    print(result)
    f = open('password.txt', 'w')
    f.write(result) 
    f.close()
    if strong(result):
        print("Strong password")
    else:
        print("Weak password")

generate()