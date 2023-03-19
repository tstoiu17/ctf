# Cipher Cracking

| Difficulty     | Points         |
| -------------- | -------------- |
| Easy           | 500            |

## Description

> I've been sitting here for days, listening to the radio and writing down dots
> and dashes. I'm starting to feel like one of those old-timey codebreakers, you
> know? To be honest, I have no idea what it all means! Think you can help me
> out?
> <details>
> <summary>Hint</summary>
> This guy was on the radio talking about CyberChef, ever heard of it?
> </details>

Files:
- `1N73rC3P710N.enc`: 223 lines of morse code, each line has 8 characters

## Approach

After some CyberChefing we get the following recipe to get the flag:

```py
From_Morse_Code('Space', 'Line feed')
Substitute('T', '1', false)
Substitute('F', '0', false)
From_Binary('Space', 8)
From_Base64('A-Za-z0-9+/=', true, false)
Substitute('.', ' ', false)
From_Charcode('Space', 10)
From_Base32('A-Z2-7=', false)
Reverse('Character')
ROT13_Brute_Force(true, true, false, 100, 0, true, 'vikeCTF')
```

Flag: 

```
vikeCTF{C0D3_8r34K3r5_637_Cr4CK1N6}
```

