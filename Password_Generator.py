import random
import string

print("Password Generator")
print("------------------")

length = int(input("Enter desired password length: "))
letters = string.ascii_letters  # a-z + A-Z
digits = string.digits  # 0-9
symbols = string.punctuation  # special characters like !@#$

all_chars = letters+digits+symbols

password = "".join(random.choice(all_chars) for _ in range(length))
print("Your generated password is:", password)
