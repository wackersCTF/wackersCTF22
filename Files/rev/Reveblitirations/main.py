import random
import string

flag = open("flag.txt", "r").readline()
char_set = string.ascii_uppercase + string.digits

chars = ''.join(random.sample(char_set*6, 6))
key=""
for x in chars:
  key += str(ord(x))
key = int(key)^1337
print(f"Your key is: {key}")
user_answer = input("What's my password? ")
if user_answer == chars:
  print(f"Wow, great job!: {flag}")
else:
  print("That's not my password!")
  exit()
