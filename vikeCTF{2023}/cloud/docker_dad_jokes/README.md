# Docker Dad Jokes: Find the Punchline

| Difficulty | Points |
| ---------- | ------ |
| Easy       | 500    |

## Description

> Did vikings have dad jokes back in the day? Well, I know one thing for sure,
> these dad jokes are great!
> <details><summary>Hint</summary>
> It would be nice to see revision history somehow, maybe the flag was
> accidentally placed out in the open at some point...
> </details>

Files:

```
dadJokes.tar.gz: gzip compressed data, from Unix, original size modulo 2^32
61044736
```

## Approach

Looking through the files after uncompressing the given file, we searched for
the string of the flag prefix `vikeCTF` in all the files with the following
grep command:

```
$ grep -Pro "vikeCTF{.*?}" *
28d282b692c962584154dfe0a11c65d0fe79cba57fce57be58d14f2dcbbcf8f8.json:vikeCTF{D4D_H45_7H3_J0K35}
```

- `-P` use Perl regex to use non-greedy matching `.*?` for the closing `}`
- `-r` search recursively into subdirectories
- `-o` only show matching text (the flag)

Flag:

```
vikeCTF{D4D_H45_7H3_J0K35}
```
