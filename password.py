import secrets
import string

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

letters = letters + digits + special_chars

pwd_len = int(input("Enter password length: "))

pwd = ''

for i in range(pwd_len):
    pwd += ''.join(secrets.choice(letters))

print(pwd)

txt = open("passwords.txt", "a")
write = txt.write(str(pwd) + "\n")
txt.close()
