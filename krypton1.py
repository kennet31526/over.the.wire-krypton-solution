import string

cipher = "YRIRYGJBCNFFJBEQEBGGRA"
alpha = string.ascii_uppercase
plain = ""
for i in cipher:
    index = alpha.index(i)
    print(index)
    index = (index-13) % len(alpha)
    print("new index: " + str(index))
    plain_char = alpha[index]
    plain+=plain_char
    print("current: " + plain)

# LEVEL TWO PASSWORD ROTTEN
# CAESAR IS EASY
