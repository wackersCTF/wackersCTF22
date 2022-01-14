from pwn import *

def main():
        r = remote("20.85.231.234", 1337)
        password = ""
        r.recvuntil('Your key is:')
        key = int(r.recvline())
        key = key^1337
        n = 2
        chars = [str(key)[index : index + n] for index in range(0, len(str(key)), n)]
        for char in chars:
                password += chr(int(char))
        print(password)
        r.sendline(password)
        r.interactive()

if __name__ == "__main__":
        main()
