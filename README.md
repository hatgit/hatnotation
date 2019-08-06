# :tophat: Hatnotation

> Hatnotation is short for the *Hatzakis Base 64 notation system* which is a method to encode/decode arbitrary binary strings of data, invented by Steven Hatzakis and open-sourced here under [Apache License 2.0](https://github.com/hatgit/hatnotation/blob/master/LICENSE).

 <blockquote>
<pre><code>[Use of Hatnotation is subject to Apache License 2.0] <a href="https://github.com/hatgit/hatnotation/blob/master/LICENSE">https://github.com/hatgit/hatnotation/blob/master/LICENSE</a>
</code></pre>
</blockquote>

## Purpose
An encoding/decoding method that allows users to compress their human-readable data into fewer human-readable characters than other popular notation systems, for any arbitrary underlying machine-readable binary string, using a 6-bit values from the range of 2^6 values. 


## Warning: 

This software is still in its experimental phase (including debugging, redesign and error-checking/testing) and should not be relied upon for production. For example, as of April 30 before the conclusion of the Ethereal Hackathon our Javascript versions of the Decoder were still being debugged. 

## Background on Mnemonics (private keys) and Human vs Machine-readable code

Mnemonics (aka recovery phrases) are used in many popular crypto wallet applciations including [BIP39 (https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) (which follows a specific wordlist and checksum requirement, among other steps for wallet derivation such as BIP32, BIP44) enable a user to backup their initial entropy in human-readable format. 

For example, instead of a user having to backup a string of 128 bits or their private key, they can simply store the encoded mnemonic which represents those bits or a private key. 

> Note: While the word "private key" is usually associated with public/private key-pairs in cryptogrpahy, for the purpose of this Readme.md file, the use of private key refers to the master private key (initial entropy) for a crypto vault (within which accounts and private keys are derived) which can also be considered a pre-image of the mnemonic.


|                |12-word mnemonic               |24-word mnemonic             |
|----------------|-------------------------------|-----------------------------|
|Initial Entropy (security) |`128 bits`          |`256 bits`                   |
|Checksum        |`4 bits`                       |`8 bits`                     |
|Total Bits      |`132 bits`                     |`264 bits`                   |
|Total Words     |`132/11 = 12 words`            |`264/11 = 24 words`          |
|----------------|-------------------------------|-----------------------------|

In terms of actual pre-image resistance, the initial entropy should be generated in a cryptographically-secure manner that is pre-image resistant and resistant to other attacks, such as outlined in the [W3C Cryptography API](https://www.w3.org/TR/WebCryptoAPI/) or via the [secrets](https://docs.python.org/3/library/secrets.html) module in Python), and the psuedo-random binary string that results will be machine-readable where the purpose of encoding it into a mnemonic is to make it easier to notate, recite, read, and write, (i.e. human-readable) compared to binary (machine-readable).



### Example of various notation methods for a given binary (base 2) string: 

- 132-bit Binary (base-2) format with leading 0b): 
>`0b000010011001110010111111101011110001001100000011001001110111011010111000001111100110001101001100001011000010111010100000000101111110`
- 33-character Hexidecimal(base-16) format (with leading 0x): 
> `0x099cbfaf13032776b83e634c2c2ea017e`
- 39-decimal (base-10) integer format: 
>`204431009328679068125508232041575612798`
- 12-word Mnemonic format (BIP39): 
>`another tourist type champion crash robust thought small equip gesture pool cool`  (note: this mnemonic conveys 132 bits as the extra 4-bit checksum '1110' from the above binary string is deterministic based on the initial 128 bits).</ul></li>

- >Hatnotation format:
 > 2P{`(.C39>Q?F#DCB2[W5_
 
  


## Important

The Hatnotation system is *not intended to be an alternative to human-readable mnemonics*, but rather a complement and simply another representation of the machine-readable code, with the benefit of a reduction in the number of characters needed to notate and backup/store the data, using common and special characters from a library of 64 total possible characters (in the zero-indexed range of 2^6-1). 



### Security: 

Just as a mnemonic that represents a 132 bits of some initial entropy should convey 128 bits of security if generated properly, as the last 4 bits are deterministically derived from the hash-based checksum computation (hashing the initial entropy as a byte array). Those same 132 bits can be encoded using the Hatnotation system which will result in 22 characters, sourced from the 64 character library. Mathematically, 64^22 == 2^132, hence why there is no information/security loss, for example. 

### Lemma 
For any arbitrary binary (base-2) string x of length n, after hatnotation is applied to x, the length n = ((x - (x % 6))/6)+(x %6, optionally in some cases depending on how the encoder/decoder is constructed). 

Optimal compression will occur when the x modulo 6 is equal to zero, and least optimum when x modulo 6 is equal to 5 (The assumption in this last sentence should be checked). 

Below are two examples of when notation is optimum, using 132 bits and 264 bits as an example, and which are standard bit-lengths for the underlying entropy that represents 12-word or 24-word mnemonics used with crypto wallets. 

- `(64^((132-(132 % 6)) / 6) == 2^132`

- `(64^((264-(264 % 6)) / 6) == 2^264`


|  Private Key          |Length after Hatnotation     | BIP39 checksum    |
|----------------|-------------------------------|-----------------------------|
| 128 bits       |21 characters                |Checksum must be computed  |
| 132 bits       |22 characters             |Checksum included     |
| 256 bits       |42 characters                |Checksum must be computed  |
| 264 bits       |44 characters                 |Checksum included        |
|----------------|-------------------------------|-----------------------------|


## Library 

Using the binascii libary in python which contains the string library, we source 64 characters as follows: 

10 digit values (symbols 0-9)
26 Uppercase letter values (letters A-Z)
28 Special character values (!-`)

`Index | 6-bit number, | character/value,`
-- | -- | --
0 | "000000", | "0",
1 | "000001", | "1",
2 | "000010", | "2",
3 | "000011", | "3",
4 | "000100", | "4",
5 | "000101", | "5",
6 | "000110", | "6",
7 | "000111", | "7",
8 | "001000", | "8",
9 | "001001", | "9",
10 | "001010", | "A",
11 | "001011", | "B",
12 | "001100", | "C",
13 | "001101", | "D ",
14 | "001110", | "E",
15 | "001111", | "F",
16 | "010000", | "G",
17 | "010001", | "H",
18 | "010010", | "I",
19 | "010011", | "J",
20 | "010100", | "K",
21 | "010101", | "L",
22 | "010110", | "M",
23 | "010111", | "N",
24 | "011000", | "O",
25 | "011001", | "P",
26 | "011010", | "Q",
27 | "011011", | "R",
28 | "011100", | "S",
29 | "011101", | "T",
30 | "011110", | "U",
31 | "011111", | "V",
32 | "100000", | "W",
33 | "100001", | "X",
34 | "100010", | "Y",
35 | "100011", | "Z",
36 | "100100", | "!",
37 | "100101", | """,
38 | "100110", | "#",
39 | "100111", | "$",
40 | "101000", | "%",
41 | "101001", | "&",
42 | "101010", | "’",
43 | "101011", | "(",
44 | "101100", | ")",
45 | "101101", | "*",
46 | "101110", | '+',
47 | "101111", | ",",
48 | "110000", | "-",
49 | "110001", | ".",
50 | "110010", | "{",
51 | "110011", | ":",
52 | "110100", | ";",
53 | "110101", | "<",
54 | "110110", | "=",
55 | "110111", | ">",
56 | "111000", | "?",
57 | "111001", | "@",
58 | "111010", | "[",
59 | "111011", | "}",
60 | "111100", | "]",
61 | "111101", | "^",
62 | "111110", | "_",
63 | "111111", | "`",

## Library verification

In Python version 3.7 using the strings library, the following steps can be taken to verify the library and character order and notice that the following 4 characters are omitted "\\~/|" in the fourth step below: 

- ```>>> import string```
- ```>>> dir(string)['Formatter', 'Template', '_ChainMap', '_TemplateMetaclass', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_re', '_string', 'ascii_letters', 'ascii_lowercase', 'ascii_uppercase', 'capwords', 'digits', 'hexdigits', 'octdigits', 'printable', 'punctuation', 'whitespace']```
- ```>>> print(string.digits+string.ascii_uppercase+string.punctuation)```
- ```0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~```

- Note, the backslash `\` and forwardslash `/`characters were swapped with opening `{` and closing `}` curly brackets in the following issue: https://github.com/hatgit/hatnotation/issues/3. 
- The list of valid Hatnotation library characters are thus as follows: 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-.{:;<=>?@[}]^_`

- And the following four remain excluded/reserved ~~```"\/|~"```~~).

## Requirements

Python 3 or higher


## Installation: 

## Tests: 

> Example Test strings (note: these are not ASCII notations): 

- Decode Target: `HELLOWORLD`

- Each letter decodes to respective 6-bit group: `"010001","001110","010101","010101","011000"," ", "100000","011000","011011","010101","001101",

- Each Word as Continous string `"010001001110010101010101011000" "100000011000011011010101001101"

- Concatenation of both words into one string: `"010001001110010101010101011000100000011000011011010101001101"

- Converted binary string to hex (can be used as starting point to encode to "HELLOWORLD": `0x44e55562061b54d`

>The following Hex string can be fed to the encoder to print all characters in their linear order except for the first which is "0" (zero) and gets omitted: 

0x108310518720928b30d38f41149351559761969b71d79f8218a39259a7a29aabb2dbafc31ef3d35db7e39eb2f3dfbf

The easiest of this example can be seen using the Hatnotation library of 64 characters as the input to the decoder: 

0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-.{:;<=>?@[}]^_`

The library in binary format as a continous string: 

000000000001000010000011000100000101000110000111001000001001001010001011001100001101001110001111010000010001010010010011010100010101010110010111011000011001011010011011011100011101011110011111100000100001100010100011100100100101100110100111101000101001101010101011101100101101101110101111110000110001111011110011110100110101110110110111111000111001111010110010111100111101111110111111

The above 384-bit binary string (based on 64*6 bits) in hex is: 0x108310518720928b30d38f41149351559761969b71d79f8218a39259a7a29aabb2dbafc31ef3d35db7e39eb2f3dfbf

When the above hex string is encoded back to hatnotation it loses the leading zero (or first 6 zeroes of the above binary string) resulting in it missing from the start of the resulting encoded characters: "123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-.{:;<=>?@[}]^_`"

The loss of leading zeroes has been discussed in the following issue and is common across other popular notation systems when converting from left-padded binary data: https://github.com/hatgit/hatnotation/issues/6

## On the subject of leading zeroes (different note): 
It should be noted that if the Decoder happens to output a leading zero at the start of the string, any such continous run of zeroes (up to 5) can be discarded and means that the program appended the zero(s) because the length of the encoded binary data modulo 6 was greater than 0, unless the length of data modulo 6 is equal to zero and there are still leading zeroes. 

**When leading zeroes CAN be discarded:** If the following 64-bit string `1111111101110110000010000001010100110110010101010010100100100000` was pasted into the Hatnotation encoder (where 64 mod 6 = 4), there would be two zeroes automatically appended by the program to the left when decoding back into the string as follows `001111111101110110000010000001010100110110010101010010100100100000` (so that `66 mod 6 = 0`) which would only be noticeable when decoding the Hatnotation `F^=21K=LI!W` back to binary using the decoder, where two leading zeroes would appear and which should be discarded to obtain the original binary data (There is however, an exception to this rule noted below in the next example).

As noted above, the **exception when leading zeroes should NOT be discarded** is when the length of the string being encoded is already equal to zero when modulo 6, and thus leading zeroes are already present such as in the following string, `001111111101110110000010000001010100110110010101010010100100100000` which when encoded would appear also as `F^=21K=LI!W` and indistinguishable from an identical string that lacked such two leading zeroes prior to encoding, and thus the user must retain the initial length of the string prior to encoding, in order to decide whether any leading zeroes should be discarded or not when decoding back to the initial data. 

This approach is necessary as appending the zeroes instead at the right end would increase the size of the number versus at the front ( `['111111', '110111', '011000', '001000', '000101', '010011', '011001', '010101', '001010', '010010', '0000']`) which could lead to errors, compared to the way the program works now where the output is read as a big-endian number where the most significant bit starts at the left and thus any leading zeroes should be dropped : [`'001111', '111101', '110110', '000010', '000001', '010100', '110110', '010101', '010010', '100100', '100000'`] (especially as the encoder cannot encode the value `0` at the start position in hatnotation which in binary is "`000000`").

** There can be some formatting issues in Python which affect how data is printed as noted in this committ: https://github.com/hatgit/hatnotation/commit/66727918cef8a5bdfad21051d52b9c1e483c7fbc

## Resources: 

- Other base64 encoding schemes: https://en.wikipedia.org/wiki/Base64
- Notational conventions: https://tools.ietf.org/html/rfc2822
- Human-readable keys (1994) https://tools.ietf.org/html/rfc1751

## Roadmap/Plans:

- develop a range of potential use cases 
- potentially propose a request for comments (RFC) for consideration as a standard.
- add error message for invalid characters (i.e. lowercase and reserved characters `\|/~`

# About Hatnotation-Password-Generator-Python.py

Author: Steven Hatzakis @ 2019

A cryptographcially-secure password generator that uses Python's built-in "secrets" module and that is compatible with the Hatnotation library (i.e. Generates passwords that only use the 64 Hatnotation characters).


