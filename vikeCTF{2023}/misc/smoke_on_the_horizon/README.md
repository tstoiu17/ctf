# Smoke on the Horizon

## Description

> By Odin's beard, we've spotted some smoke signals between the longship and
> the village. It's rather cloudy today so you'll need good eyes. Go find the
> messages and figure out what they're saying! Quickly!

Files:
```
SmokeOnTheHorizon.zip: Zip archive data, at least v2.0 to extract, compression method=deflate
smoke.pcap: pcap capture file, microsecond ts (little-endian) - version 2.4 (Ethernet, capture length 262144)
```

Unzipping the zip file gave us a pcap file, so we analyzed it with Wireshark.

After looking around and using different filters, we exported the files that
wireshark was able to assemble by selecting `File` -> `Export Objects` ->
`FTP-DATA...` and `Export Objects` -> `HTTP...`. This gave us a `flag.enc`
file from the FTP-DATA packets and a `decrypt` file from the HTTP packets.

The flag.enc seemed to be an encrypted file, from the `.enc` extension. The
`decrypt` file on the other hand seemed to be an executable.

```
$ file decrypt
decrypt: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, 
interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=717fe553eeaf98be1f9a8401da9eaf1ef4435550, 
for GNU/Linux 3.2.0, stripped
```

We tried running it and got the following:

```
$ ./decrypt
Usage: ./decrypt input_file password
```

This means we needed to run it with 2 arguments: an input file and a password.
Since `flag.enc` is the only file we had that needs to be decrypted, we tried
that first.

Another command we tried using to extract information from the pcap file was
`tcpflow`:

```
tcpflow -r smoke.pcap
```

This command reconstructs the data streams that were captured in `smoke.pcap`,
and creates one file for each flow. Looking through these files we found what
seemed to be an email containing a password:

```
EHLO village.ctf
MAIL FROM:<viktor@village.ctf> SIZE=405
RCPT TO:<eskil@longship.ctf> ORCPT=rfc822;eskil@longship.ctf
DATA
Received: by village.ctf (Postfix, from userid 1001)
	id 76D598031A; Thu, 16 Mar 2023 18:02:38 -0700 (PDT)
Subject: Secret password
To: <eskil@longship.ctf>
User-Agent: mail (GNU Mailutils 3.14)
Date: Thu, 16 Mar 2023 18:02:38 -0700
Message-Id: <20230317010238.76D598031A@village.ctf>
From: viktor@village.ctf

Eskil, 

The password is "p!ll@ge_🔥_p1und3r". You know what to do. 

-Viktor
.
QUIT
```

And sure enough using this password as the argument to the `decrypt` binary
gives us our flag:

```
$ ./decrypt flag.enc 'p!ll@ge_🔥_p1und3r'
Decryption successful: flag.enc -> flag.enc.dec
```

Flag:

```
vikeCTF{C@pt7ur3d_my_p@ckets?_Wh4t5_7h3_r@ns0m?}
```
