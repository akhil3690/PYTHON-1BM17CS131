import string
import random

def passwordGen(length=6):
    pass_chars=string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(pass_chars) for i in range(length))

print("First Random Password: ",passwordGen())
print("Second Random Password: ",passwordGen(10))
print("Third Random Password: ",passwordGen(15))
