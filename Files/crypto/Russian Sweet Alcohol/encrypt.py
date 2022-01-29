from math import gcd 
flag = open('flag.txt', 'r').read()
flagChars = []
for character in flag:
  flagChars.append(ord(character))

p = getPrime()
q = getPrime()
n = p * q
print(f'p: {p}')
print(f'q: {q}')

e = getE()
print(f'e: {e}')

ct = []
for character in flagChars:
  ct.append(pow(character, e, n))
print(ct)