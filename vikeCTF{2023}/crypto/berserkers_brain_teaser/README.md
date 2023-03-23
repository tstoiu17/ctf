# Berserker’s Brain Teaser

| Difficulty | Points |
| ---------- | ------ |
| Medium     | 500    |

## Description

> Welcome to the "Berserker's Brain Teaser" challenge! The Vikings were known for
> their fearless and frenzied warriors called berserkers, and this challenge will
> require you to channel your inner berserker to solve a cryptogram. Can you
> break the code and decipher the message to claim victory?
> 
> ```
> zexqSNE{cVaLuM_xRxBuRs_vE_mTtAe_ToOiN_oEiK}
> ```

Files:

```
BerserkerBrainTeaserEncrypt.py
```

## Approach

We are given the following `BerserkerBrainTeaserEncrypt.py`:

```py
import random

alphabet = "abcdefghijklmnopqrstuvwxyz"

plaintext = input("text to encrypt:\n")
ciphertext = ""

key = [random.randint(1, len(alphabet)) for _ in range(len("vikeCTF"))]
print("key:", *key)

for i, c in enumerate(plaintext):
    if not c.isalpha():
        ciphertext += c
        continue

    offset = alphabet.find(c.lower())
    rotation = key[i % len(key)]

    result = alphabet[(offset + rotation) % len(alphabet)]
    if c.islower():
        ciphertext += result
    else:
        ciphertext += result.upper()

print("ciphertext:")
print(ciphertext)
```

The "code" given in the challenge:
`zexqSNE{cVaLuM_xRxBuRs_vE_mTtAe_ToOiN_oEiK}` seems to be in the flag format:
`vikeCTF{.*}`. So it seems that we need to reverse engineer this encryption
script to decrypt the encrypted flag:
`zexqSNE{cVaLuM_xRxBuRs_vE_mTtAe_ToOiN_oEiK}`.

The first step is to understand how the program works. 

### 4 Variables

We set 4 variables: `alphabet`, `plaintext`, and `ciphertext` are
self-explanatory. The `key` variable stores a list of 7 random integers in the
interval [1, 26], using
[`random.randint()`](https://docs.python.org/3/library/random.html?highlight=random%20randint#random.randint),
and 7 is the number of characters in the flag prefix: `vikeCTF`. The key can be
thought of as 7 random indexes of the 1-indexed alphabet. 

### `for` loop

The program then loops over the `plaintext` variable encrypting it one
character at a time and storing the resulting encrypted string in `ciphertext`.
The first `if` statement checks if the current character `c` is not a letter,
if it isn't a letter it adds it to the ciphertext and skips the rest of the
iteration for that character with `continue`. This means anything that is
not a letter will appear in the encrypted string unchanged, these are the
opening and closing curly brace and the underscores. Then it sets 2
variables:

- `offset`: the index of the current character `c` in the 0-indexed alphabet
- `rotation`: the index of the current key value in the 1-indexed alphabet

The next line is the important part, `result` is the encrypted letter. We get
it by indexing the `alphabet` with `(offset + rotation) % len(alphabet)`.
`offset + rotation` rotates or shifts the character `c` by `rotation` positions
in the alphabet, since `offset` is the index of `c`. The modulus operation
facilitates cyclic indexing so that a large `rotation` always results in a
valid alphabet index. It then indexes the alphabet and stores the letter in
`result`. Finally we add the encrypted letter to the `ciphertext` with the same
capitalization it had in the `plaintext`. This is similar to a ROT13 cipher but
instead of rotating by 13 positions we rotate by one of the 7 randomly
generated numbers in our `key`. So the *key* to decrypting our flag is to know
the `key` (pun intended)

Now that we understand how it works we can create a `solve.py` that can decrypt
any ciphertext encrypted by this program, given the at least 7 characters from
the original plaintext. 

### `solve.py`

```py
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
```

Flag:

```
vikeCTF{gIoVaN_bElLaSo_iS_sUpEr_DuPeR_cOoL}
```
