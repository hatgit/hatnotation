import string
import binascii
import math
import secrets

#Author: Steven Hatzakis @2018, Licensed under Apache 2.0

#Version 1.01


# Example Test string target to decode: HELLOWORLD
# Each letter decodes to respective 6-bit group: `"010001","001110","010101","010101","011000"," ", "100000","011000","011011","010101","001101",
# Each Word as Continous string `"010001001110010101010101011000" "100000011000011011010101001101"
# Concatenation of both words into one string: `"010001001110010101010101011000100000011000011011010101001101"
# Converted binary string to hex: `0x44e55562061b54d`


b64dict=dict()

base64library=["0",
"1",
"2",
"3",
"4",
"5",
"6",
"7",
"8",
"9",
"A",
"B",
"C",
"D",
"E",
"F",
"G",
"H",
"I",
"J",
"K",
"L",
"M",
"N",
"O",
"P",
"Q",
"R",
"S",
"T",
"U",
"V",
"W",
"X",
"Y",
"Z",
"!",
'"',
"#",
"$",
"%",
"&",
"'",
"(",
")",
"*",
'+',
",",
"-",
".",
"}",
":",
";",
"<",
"=",
">",
"?",
"@",
"[",
"{",
"]",
"^",
"_",
"`"]
for i in range(len(base64library)):
    b64dict[base64library[i]] = i


def decodeAsBin(string):
    output = []
    s=''
    print(len(string))
    for j in range(len(string)):

        if (string[j] != ' '):
            output.append(bin(b64dict[string[j].upper()])[2:].zfill(6))

    return s.join(output)


def decodeAsHex(string):

    return hex(int(decodeAsBin(string), 2))

hatdata2decode=input('Enter any combination of the following characters to decode without spaces: 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!"'"#$%&'"'()*+,-.{:;<=>?@[}]^_`:')
                     
print(decodeAsBin(hatdata2decode))

## test decode string "HELLOWORLD" should return the binary equivalent of hex: 0x44e55562061b54d
## test decode string "INVENTEDBYSTEVENHATZAKIS@2018' should return this hex 0x125df39774e34b89c74e7ce5d129d8ca512739080048 as equivalent in binary to this output: 010010010111011111001110010111011101001110001101001011100010011100011101001110011111001110010111010001001010011101100011001010010100010010011100111001000010000000000001001000
## Note/ WARNING: leading zeroes are not retained in the Hatnotated string, therefore, when decoding the test string `9$B_,4-C$T(W_O;-)B'0N` found in the Readme file, two leading zeroes will not appear. Software implementers should pad enough zeroes to math the Hatnotated character lenght (i.e. 22 pasted characters should compute 132 bits, but if only 130 bits show then 2 leading zeroes shoud be padded. 
## Note/CONSIDERATION: In version 1.01 to resolve a rendering conflict, the Forward slash `/` and Backslash `\` characters have been swapped out and replaced by the closing curly bracket `}` and opening curly bracket `{` on purpose.



