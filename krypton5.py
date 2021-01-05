from pwn import *


r = process(["cat","krypton5-data2"])
text = r.recvall()
text = text.decode("utf-8").replace(" ", "")


def gen_key(most_wanted, key_length):
    print("most wanted: " + str(most_wanted))
    # print("second most wanted: " + str(secondMostWanted))

    # alpha = string.ascii_uppercase
    alpha = string.ascii_uppercase

    # e + keyChar = mostWanted char
    key = ""
    for cipher_char in most_wanted:
        cipher_char_index = alpha.find(cipher_char)
        plain_char_index = alpha.find("E")
        # cipherCharAscii - x = plainCharAscii
        key_char_index = (cipher_char_index - plain_char_index) % len(alpha)
        key += alpha[key_char_index]

    print("key: " + key)
    # (chipher char index - key char index) %26 = plain char index

    pw_cipher = "BELOSZ"

    index = 0
    plain = ""
    for cipher_char in pw_cipher:
        key_char = key[index % key_length]
        key_char_index = alpha.find(key_char)
        cipher_char_index = alpha.find(cipher_char)
        plain_char_index = (cipher_char_index - key_char_index) % len(alpha)
        plain += alpha[plain_char_index]
        index += 1

    print("plain:" + plain)


def try_key_length(key_length):
    # [{number : chars},...]
    keysets = []
    # split
    index = 0
    for cipher_char in text:
        try:
            keysets[index % key_length]= keysets[index % key_length] + cipher_char
        except IndexError:
            keysets.append(cipher_char)
        index += 1

    print(keysets)
    # list of dicts with each dict = {"char":amount_chars}
    amount_chars_dicts = []
    index = 0
    for cipher in keysets:
        #print(cipher)
        for cipher_char in cipher:
            try:
                amount_chars_dict = amount_chars_dicts[index]
                amount = amount_chars_dict[cipher_char]
                amount_chars_dict[cipher_char] = amount + 1
            except IndexError:
                amount_chars_dicts.append({cipher_char:1})
            except KeyError:
                amount_chars_dict = amount_chars_dicts[index]
                amount_chars_dict.update({cipher_char:1})
        index+=1
    # find most wanted = chars occuring most often and thus are most likely be mapped to letter e
    print("amount Char dicts: " + str(amount_chars_dicts))
    most_wanted = []
    index = 0
    for amount_char_dict in amount_chars_dicts:
        s = {k: v for k, v in sorted(amount_char_dict.items(), key=lambda item: item[1], reverse=True)}
        amount_chars_dicts[index] = s
        # put best in most wanted list
        most_wanted.append(list(s)[0])
        index+=1

    gen_key(most_wanted, key_length)
    # print(amountCharsDicts)


for key_length in range(1, 10):
    print("trying keylength: " + str(key_length))
    try_key_length(key_length)
    print(" ")



