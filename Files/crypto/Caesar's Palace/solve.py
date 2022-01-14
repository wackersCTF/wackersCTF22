from pwn import *
import string

dictionary = open("dictionary.txt", "r").read().splitlines()
actual_dictionary = []
alphabet = string.ascii_lowercase

def caesar(ct, key):
    decrypted_message = ""
    for c in ct:
        if c in alphabet:
            position = alphabet.find(c)
            new_position = (position - key) % 26
            new_character = alphabet[new_position]
            decrypted_message += new_character
        else:
            decrypted_message += c
    return decrypted_message

def main():
        for word in dictionary:
                actual_dictionary.append(word.lower())
        r = remote("20.85.231.234", 1338, level = 'debug')
        for x in range(200):
                r.recvuntil(b'Encrypted word: ')
                ct = str(str(r.recvline()).split('\\')[0]).split("'")[1]
                pt = ""
                for i in range(26):
                        pt = caesar(ct, i)
                        if pt in actual_dictionary:
                                r.sendline(pt.encode())
        r.interactive()

if __name__ == "__main__":
        main()
