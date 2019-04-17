import string
import binascii
import math
import secrets

#Author: Steven Hatzakis @2018, Licensed under Apache 2.0

# NOTE: The initial version of this application is not yet functional and requires a code fix/rewrite in order to properly decode using the sample test string below.

# Example Test string target to decode: hello world
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
"+",
",",
"-",
".",
"/",
":",
";",
"<",
"=",
">",
"?",
"@",
"[",
"\\",
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

print(decodeAsBin("INVENTEDBYSTEVENHATZAKIS@2018"))

## test string should 29 hex: 0x125df39774e34b89c74e7ce5d129d8ca512739080048 equivalent in binary to this output: 010010010111011111001110010111011101001110001101001011100010011100011101001110011111001110010111010001001010011101100011001010010100010010011100111001000010000000000001001000


## Note/CONSIDERATION: Last four punctuation characters "{|}`" have been omitted from the above list, and even though they exists in the encoder python app it never appears in results (perhaps should be added here so a warning/error would trigger if those values ever appear in results or when entered into a decoder.



