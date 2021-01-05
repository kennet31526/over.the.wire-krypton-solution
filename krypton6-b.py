from pwn import *



abc = string.ascii_uppercase
# shift values found by script a
shifts = [4,8,2,19,3,6,24,8,24,25,10,19,7,13,18]
print(len(shifts))
cipher = "PNUKLYLWRQKGKB"
index = 0
plain_pw = ""
for c in cipher:
    shift = shifts[index]
    cchar = abc.find(c)
    pchar = (cchar - shift) % 26
    plain = abc[pchar]
    plain_pw+=plain
    index+=1
print(plain_pw)

#LFSRISNOTRANDOM