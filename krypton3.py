from pwn import *


r = process(["cat","krypton3-data","krypton3-data2","krypton3-data3"])
text = r.recvall()

print(len(text))

text = text.decode("utf-8").replace(" ", "")


result = {}
for char in text:
    try:
        entry = result[char]
        result[char] = result[char] + 1
    except KeyError:
        print("Letter is new: " + char)
        result[char] = 1


print(result)

sorted_dict = {k: v for k, v in sorted(result.items(), key=lambda item: item[1])}

print(sorted_dict)

pw = "KSVVW BGSJD SVSIS VXBMN YQUUK BNWCU ANMJS".replace(" ","")
alpha = "EATSORNIHCLDUPGFWYMBKVJXQZ"

index = 0

# SE EE FF
new_pass = ""

dict = {}
for old in sorted_dict.__reversed__():
    new = alpha[index]
    dict[old]=new
    print("old: "  + old + " new: " + new)
    index+=1

# C - G
# H - R
for old in pw:
    new = dict[old]
    new_pass+=new

print(new_pass)


#print(newPass.replace("C","G"))
#print(newPass.replace("H","R"))
#print(newPass.replace("C","G").replace("C","G"))

# WELLDONETHELEVELFOURPASSWORDISBRUTE
# WELLDONETHELEVELFOURPASSWORDISBRUTE