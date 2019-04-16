# Hatnotation

> Hatnotation is short for the *Hatzakis Base 64 notation system* which is a method to encode/decode arbitrary binary strings of data, invented by Steven Hatzakis and open-sourced here under [Apache License 2.0] (https://github.com/hatgit/hatnotation/blob/master/LICENSE).

 <blockquote>
<pre><code>[Use of Hatnotation is subject to Apache License 2.0 ] <a href="https://github.com/hatgit/hatnotation/blob/master/LICENSE">https://github.com/hatgit/hatnotation/blob/master/LICENSE</a>
</code></pre>
</blockquote>

## Purpose
An encoding/decoding method that allows users to compress their human-readable data into fewer humand-readable characters than other popular notation systems, for any arbitrary underlying machine-readable binary string. 


## Warning: 

This software is still in its experimental phase and should not be relied upon for production. 

## Background on Mnemonics (private keys) and Human vs Machine-readable code

Mnemonics (aka recovery phrases) are used in many popular crypto wallet applciations including [BIP39] (https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) (which follows a specific wordlist and checksum requirement, among other steps for wallet derivation such as BIP32, BIP44) enable a user to backup their initial entropy in human-readable format. 

For example, instead of a user having to backup a string of 128 bits or their private key, they can simply store the encoded mnemonic which represents those bits or a private key. 

> Note: While the word "private key" is usually associated with public/private key-pairs in cryptogrpahy, for the purpose of this Readme.md file, the use of private key refers to the master private key (initial entropy) for a crypto vault (within which accounts and private keys are dervived) which can also be considered a pre-image of the mnemonic.


|                |12-word mnemonic               |24-word mnemonic             |
|----------------|-------------------------------|-----------------------------|
|Initial Entropy (security) |`128 bits`          |`256 bits`                   |
|Checksum        |`4 bits`                       |`8 bits`                     |
|Total Bits      |`132 bits`                     |`264 bits`                   |
|Total Words     |`132/11 = 12 words`            |`264/11 = 24 words`          |
|----------------|-------------------------------|-----------------------------|

In terms of actual pre-image resistance, the initial entropy should be generated in a cryptographically-secure manner that is pre-image resistant and resistant to other attacks, such as outlined in the W3C Cryptography API or via the "secrets" module in Python), and the psuedo-random binary string that results will be that is machine-readable where the purpose of encoding it into a mnemonic is to make it easier to notate, recite, read, and write, compared to binary (machine-readable).



### Example of various notation methods for a given binary (base 2) string: 

- Binary (base-2) format: 
>`00001001100111001011111110101111000100110000001100100111011101101011100000111110011000110100110000101100001011101010000000010111`
- Hexidecimal(base-16) format: 
> `99cbfaf13032776b83e634c2c2ea017`
- Decimal (base-10) integer format: 
>`12776938083042441757844264502598475799`
- Mnemonic format (BIP39): 
>`another tourist type champion crash robust thought small equip gesture pool cool`  (note: this mnemonic conveys 132 bits as the extra 4-bit checksum is deterministic based on the initial 128 bits).</ul></li>

- >Hatnotation format:
 > `9$B_,4-C$T(W_O;-)B'0N`


## Important

The Hatnotation system is *not intended to be an alternative to human-readable mnemonics*, but rather a complement and simply another representation of the machine-readable code, with the benefit of a reduction in the number of characters needed to notate and backup/store the data, using common and special characters from a library of 64 total possible characters (in range of 2^6). 



### Security: 

Just as a mnemonic that represents a 132 bits of some initial entropy should convey 128 bits of security if generated properly, as the last 4 bits are deterministically derived from the hash-based checksum computation (hashing the initial entropy as a byte array). Those same 132 bits can be encoded using the Hatnotation system which will result in 22 characters, sourced from the 64 character library. Mathematically, 64^22 == 2^132, hence why there is no information/security loss, for example. 

### Lemma 
For any arbitrary binary (base-2) string x of length n, after hatnotation is applied to x, the length n = ((x - (x % 6))/6)+(x %6, optionally in some cases depending on how the encoder/decoder is constructed). Optimal compression will occur when the [COMPLETE THIS SECTION]  

- `(128-(128 % 6)) / 6 == 21 == 2^128`
- `(132-(132 % 6)) / 6 == 22 == 2^132`
- `(256-(256 % 6)) / 6 == 42 == 2^256`
- `(264-(264 % 6)) / 6 == 44 == 2^264`


|  Private Key          |12-word mnemonic               |24-word mnemonic     |
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
46 | "101110", | "+",
47 | "101111", | ",",
48 | "110000", | "-",
49 | "110001", | ".",
50 | "110010", | "/",
51 | "110011", | ":",
52 | "110100", | ";",
53 | "110101", | "<",
54 | "110110", | "=",
55 | "110111", | ">",
56 | "111000", | "?",
57 | "111001", | "@",
58 | "111010", | "[",
59 | "111011", | "\",
60 | "111100", | "]",
61 | "111101", | "^",
62 | "111110", | "_",
63 | "111111", | "`",

## Library verification

In Python version 3.7 using the strings library, the following steps can be taken to verify the library and character order and by omitting the last 4 characters "{|}~" in the fourth step below (zeroed-index values 64-67 which have been omitted from the above list as well): 

- ```>>> import string```
- ```>>> dir(string)['Formatter', 'Template', '_ChainMap', '_TemplateMetaclass', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_re', '_string', 'ascii_letters', 'ascii_lowercase', 'ascii_uppercase', 'capwords', 'digits', 'hexdigits', 'octdigits', 'printable', 'punctuation', 'whitespace']```
- ```>>> print(string.digits+string.ascii_uppercase+string.punctuation)```
- ```0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~```

(i.e. ~~```"{|}~"```~~)

## Requirements

Python 3 or higher


## Installation: 

## Tests: 

## Reources: 

## Roadmap/Plans:


