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

The given file, `1N73rC3P710N.enc`, contains some dots and dashes which looks
like morse code. So we copy the file into
[CyberChef](https://gchq.github.io/CyberChef/) Note that we encountered an
issue when we initially imported the file into CyberChef with the "Open file as
input" button, the solution was to copy paste the contents of the file into the
Input box. After some CyberChefing (spamming the
[Magic](https://github.com/gchq/CyberChef/wiki/Automatic-detection-of-encoded-data-using-CyberChef-Magic)
operation) we end up with the following recipe that outputs the flag:

```json
[
  { "op": "From Morse Code", "args": ["Space", "Line feed"] },
  { "op": "Substitute", "args": ["T", "1", false] },
  { "op": "Substitute", "args": ["F", "0", false] },
  { "op": "From Binary", "args": ["Space", 8] },
  { "op": "From Base64", "args": ["A-Za-z0-9+/=", true, false] },
  { "op": "Substitute", "args": [".", " ", false] },
  { "op": "From Charcode", "args": ["Space", 10] },
  { "op": "From Base32", "args": ["A-Z2-7=", true] },
  { "op": "Reverse", "args": ["Character"] },
  { "op": "ROT13 Brute Force", "args": [true, true, false, 100, 0, false, "vikeCTF"] }
]
```

Flag: 

```
vikeCTF{C0D3_8r34K3r5_637_Cr4CK1N6}
```
