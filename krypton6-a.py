from pwn import *

plain_file = "/tmp/plain"
cipher_file = "/tmp/cipher"


# create files
subprocess.check_output(["touch", plain_file])
subprocess.check_output(["touch", cipher_file])
subprocess.check_output(["chmod", "a+w", plain_file])
subprocess.check_output(["chmod", "a+w", cipher_file])

write(cipher_file, b"")

abc = string.ascii_uppercase


def try_char_seq(char):
    print("length: " + str(len(char)))
    print("current string: " + char)
    pchar = abc.find(char[len(char) - 1])
    print("pos in alpha: " + str(pchar))
    write(plain_file, bytes(char, "utf-8"))
    subprocess.check_output(["/krypton/krypton6/encrypt6", plain_file, cipher_file])
    cipher = read(cipher_file).decode("utf-8")
    print("current cipher: " + cipher)
    cchar = abc.find(cipher[len(cipher) - 1])
    print("pos in alhpa: " + str(cchar))
    print("delta: " + (pchar+cchar)%26)
    print("")

# try finding pattern
for char in abc:
    for i in range(15):
        try_char_seq(char * (i + 1))

# found pattern running the above script
# always modulo 26
# first cchar = first plain pchar+4
# second cchar = first(cchar) + 8
# third char = first(cchar) + 2
# fourth char = first(cchar) + 19
# fifth char = first(cchar) + 3
# sixth char = first(cchar) + 6
# seventh char = first(cchar) + 24
# eighth cchar = first(cchar) + 8
# nineth cchar = first(cchar) + 24
# 10. cchar = first(cchar) + 25
# 10 19 7 13 18