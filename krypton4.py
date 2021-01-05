from pwn import *


r = process(["cat","krypton4-data1"])
text = r.recvall()


text = text.decode("utf-8").replace(" ", "")

index = 0
# nummer : chars
keysets = {0: "", 1: "", 2: "", 3: "", 4: "", 5: ""}
for cipher_char in text:
    keysets[index % 6]= keysets[index % 6] + cipher_char
    index+=1

print(keysets)
# {nummer : dict{char, amountChars}, ...}
amount_chars_dicts = {0: {}, 1: {}, 2: {}, 3: {}, 4: {}, 5: {}}
for set_number in keysets:
    # {char:amountChars}
    amount_chars_dict = amount_chars_dicts[set_number]
    for cipher_char in keysets[set_number]:
        try:
            amount = amount_chars_dict[cipher_char]
            amount_chars_dict[cipher_char] = amount + 1
        except KeyError:
            amount_chars_dict[cipher_char] = 1


# most wanted = chars occuring most often and thus are most likely be mapped to letter e
def gen_key(most_wanted):
    print("most wanted: " + str(most_wanted))

    alpha = string.ascii_uppercase

    # e + keyChar = most wanted char
    key = ""
    for cipher_char in most_wanted:
        cipher_char_index = alpha.find(cipher_char)
        plain_char_index = alpha.find("E")
        # (cipherCharAscii - x) % 26 = plainCharAscii
        key_char_index = (cipher_char_index - plain_char_index) % len(alpha)
        key += alpha[key_char_index]

    print("key: " + key)
    # (chipher char index - key char index) %26 = plain char index

    pw_cipher = "HCIKVRJOX"

    index = 0
    plain = ""
    for cipher_char in pw_cipher:
        key_char = key[index % 6]
        key_char_index = alpha.find(key_char)
        cipher_char_index = alpha.find(cipher_char)
        plain_char_index = (cipher_char_index - key_char_index) % len(alpha)
        plain += alpha[plain_char_index]
        index += 1

    print("plain:" + plain)


most_wanted = []
for dict_number in amount_chars_dicts:
    s = {k: v for k, v in sorted(amount_chars_dicts[dict_number].items(), key=lambda item: item[1])}
    amount_chars_dicts[dict_number] = s
    most_wanted.append(list(s)[len(s) - 1])

gen_key(most_wanted)
print(amount_chars_dicts)







