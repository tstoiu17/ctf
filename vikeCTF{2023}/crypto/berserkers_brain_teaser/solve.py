#!/usr/bin/python3

import random

alphabet = "abcdefghijklmnopqrstuvwxyz"

# use the known portion to get the key
plaintext = "vikeCTF"
enc_flag  = "zexqSNE"

key = []
for i, c in enumerate(plaintext):
    offset = alphabet.find(c.lower())
    result = alphabet.find(enc_flag[i].lower())
    if result <= offset: # case: mod reset the index
        rotation = (result + len(alphabet)) - offset
    else:                # case: mod did not reset the index
        rotation = result - offset
    key += [rotation]

# print("key:", *key)

ciphertext = "zexqSNE{cVaLuM_xRxBuRs_vE_mTtAe_ToOiN_oEiK}"
flag = ""

for i, c in enumerate(ciphertext):
    if not c.isalpha():
        flag += c
        continue

    offset = alphabet.find(c.lower())
    rotation = key[i % len(key)]

    # rotate in the opposite ↓↓↓ direction
    result = alphabet[(offset - rotation) % len(alphabet)]
    if c.islower():
        flag += result
    else:
        flag += result.upper()

# print("decrypted flag:")
print(flag)
