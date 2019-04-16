# Hatnotation
Hatnotation is short for the Hatzakis Base 64 notation system which is a method to encode/decode arbitrary binary strings of data, invented by Steven Hatzakis and open-sourced here under Apache License 2.0 https://github.com/hatgit/hatnotation/blob/master/LICENSE.

 <blockquote>
<pre><code>[Use of Hatnotation is subject to Apache License 2.0 ] <a href="https://github.com/hatgit/hatnotation/blob/master/LICENSE">https://github.com/hatgit/hatnotation/blob/master/LICENSE</a>
</code></pre>
</blockquote>

## Warning: 

This software is still in its experimental phase and should not be relied upon for production. 

## Background on Mnemonics (private keys) and Human vs Machine-readable code

Mnemonics (aka recovery phrases) are used in many popular crypto wallet applciations including BIP39 (which follows a specific wordlist and checksum requirement, among other steps for wallet derivation such as BIP32, BIP44) enable a user to backup their initial entropy in human-readable format. For example, instead of a user having to backup a string of 128 bits or their private key, they can simply store the encoded mnemonic which represents those bits or a private key. Note: While the word private key is usually associated with public/private key-pairs in cryptogrpahy, for the purpose of this Readme.md file, the use of private key refers to the master private key (initial entropy) for a crypto vault (within which accounts and private keys are dervived) which can also be considered a pre-image of the mnemonic.


|                |12-word mnemonic               |24-word mnemonic             |
|----------------|-------------------------------|-----------------------------|
|Initial Entropy (security) |`128 bits`                     |`256 bits`                   |
|Checksum        |`4 bits`                       |`8 bits`                     |
|Total Bits      |`132 bits`                     |`264 bits`                   |
|Total Words     |`132/11 = 12 words`            |`264/11 = 24 words`          |
|----------------|-------------------------------|-----------------------------|

In terms of actual pre-image resistance, the initial entropy should be generated in a cryptographically-secure manner that is pre-image resistant and resistant to other attacks), and the psuedo-random binary string that results will be that is machine-readable where the purpose of encoding it into a mnemonic is to make it easier to notate, recite, read, and write, compared to binary (machine-readable)format.



### Example of various notation methods for a given binary (base 2) string: 

<li><ul>Binary (base-2) format: `00001001100111001011111110101111000100110000001100100111011101101011100000111110011000110100110000101100001011101010000000010111`</ul>
<ul>Hexidecimal(base-16) format: `99cbfaf13032776b83e634c2c2ea017`</ul>
<ul>Decimal (base-10) integer format: `12776938083042441757844264502598475799`</ul>
<ul>Mnemonic format (BIP39): `another tourist type champion crash robust thought small equip gesture pool cool`  (note: this mnemonic conveys 132 bits as the extra 4-bit checksum is deterministic based on the initial 128 bits).</ul>

<ul>Hatnotation format: `9$B_,4-C$T(W_O;-)B'0N`</ul>
</li>

## Important

The Hatnotation system is *not intended to be an alternative to human-readable mnemonics*, but rather a complement and simply another representation of the machine-readable code, with the benefit of a reduction in the number of characters needed to notate and backup/store the data, using common and special characters from a library of 64 total possible characters (in range of 2^6). 



### Security: 

Just as a mnemonic that represents a 132 bits of some initial entropy should convey 128 bits of security if generated properly, as the last 4 bits are deterministically derived from the hash-based checksum computation (hashing the initial entropy as a byte array). Those same 132 bits can be encoded using the Hatnotation system which will result in 22 characters, sourced from the 64 character library. Mathematically, 64^22 == 2^132, hence why there is no information/security loss, for example. 

### Lemma 
For any arbitrary binary (base-2) string x of length n, after hatnotation is applied to x, the length n = ((x - (x % 6))/6)+(x %6, optionally in some cases depending on how the encoder/decoder is constructed). Optimal compression will occur when the  

`(128-(128 % 6)) / 6 == 21 == 2^128
`(132-(132 % 6)) / 6 == 22 == 2^132
`(256-(256 % 6)) / 6 == 42 == 2^256
`(264-(264 % 6)) / 6 == 44 == 2^264


|                |12-word mnemonic               |24-word mnemonic             |
|----------------|-------------------------------|-----------------------------|
| 128 bits       |`21 characters`                |`Checksum must be computed'  |
| 132 bits       |`22 characters`                |`Checksum included           |
| 256 bits       |`42 characters`                |`Checksum must be computed`  |
| 264 bits       |`44 characters`               |`Checksum included`          |
|----------------|-------------------------------|-----------------------------|


## Library 

Using the binascii libary in python which contains the string library, we source 64 characters as follows: 

10 digits (0-9)
26 Uppercase letters (A-Z)
28 Special characters (!-`)

