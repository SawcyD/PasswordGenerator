import secrets
import string

letters = string.ascii_letters
numbers = string.digits
specialCharacter = string.punctuation

characters = letters + numbers + specialCharacter



pwdLength = 24

while True:
  pwd = ''
  for i in range(pwdLength):
    pwd += ''.join(secrets.choice(characters))

  if (any(char in characters for char in pwd) and
      sum(char in numbers for char in pwd)>=2):
          break
print(pwd)