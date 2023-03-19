import random

alphabet = "abcdefghijklmnopqrstuvwxyz"

plaintext = "vikeCTF"
enc_flag  = "zexqSNE"

ciphertext = ""

key = []
for i, c in enumerate(plaintext):
    if not c.isalpha():
        ciphertext += c
        continue

    offset = alphabet.find(c.lower())
    result = alphabet.find(enc_flag[i].lower())
    # result = offset + rotation
    # rotation = result - offset
    if result <= offset: # mod reset
        rotation = (result + len(alphabet)) - offset
    else:
        rotation = result - offset
    key += [rotation]

print("key:", *key)

ciphertext  = "zexqSNE{cVaLuM_xRxBuRs_vE_mTtAe_ToOiN_oEiK}"
plaintext = ""

# key = [random.randint(1, len(alphabet)) for _ in range(len("vikeCTF"))]
# key = [4, 22, 13, 12, 16, 20, 25]

for i, c in enumerate(ciphertext):
    if not c.isalpha():
        plaintext += c
        continue

    offset = alphabet.find(c.lower()) # index of letter, or -1 if not found
    rotation = key[i % len(key)] # random number

    result = alphabet[(offset - rotation) % len(alphabet)]
    if c.islower():
        plaintext += result
    else:
        plaintext += result.upper()

print("decrypted plaintext:")
print(plaintext) # "vikeCTF{gIoVaN_bElLaSo_iS_sUpEr_DuPeR_cOoL}"
