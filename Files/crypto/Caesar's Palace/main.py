import random
import string

flag = open("flag.txt", "r").readline()
dictionary = open("dictionary.txt", "r").read().splitlines()

def caesar(txt, s):
    result = ""
    for i in range(len(txt)):  
        char = txt[i]  
        result += chr((ord(char) + int(s) - 96) % 26 + 97)  
    return result

print("\nWelcome to Caesar's Palace!")

for n in range(500):
	word = random.choice(dictionary).lower()
	caesared_word = caesar(word, random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']))
	print(f" Encrypted word: {caesared_word}")
	user_input = input("Decrypted word: ")
	if user_input == word:
		print("Good")
	else:
		print("That is not the right decrypted word!")
		exit()
print(f"Nice job, you are the caesar master: {flag}")
