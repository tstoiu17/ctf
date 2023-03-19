import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]
# lookup table to get number value
lookup = {letter: i for i, letter in enumerate(ALPHABET)}
cipher = "lkmjkemjmkiekeijiiigljlhilihliikiliginliljimiklligljiflhiniiiniiihlhilimlhijil"

def unshift(cipher, k):
    unshifted = ""
    for c in cipher:
        t1 = ord(c) - LOWERCASE_OFFSET
        t2 = ord(k) - LOWERCASE_OFFSET
        unshifted += ALPHABET[(t1 - t2) % len(ALPHABET)]
    return unshifted

# try all possible keys
for key in ALPHABET:
    unshifted = unshift(cipher, key)
    # translate cipher to number
    lst_4b = [lookup[letter] for letter in unshifted]
    MSBs = lst_4b[0::2]
    LSBs = lst_4b[1::2]
    flag = "".join(chr((msb << 4) | lsb) for msb, lsb in zip(MSBs, LSBs))
    if all(c in string.printable for c in flag):
        print(f"key: '{key}' -> picoCTF{{{flag}}}")
