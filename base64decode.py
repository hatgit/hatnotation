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


arbitrarystring=format(secrets.randbits(139),'139b')
#arbitrarystring=str(arbitrarystring)
print("0b"+arbitrarystring)
print("As hex:",hex(int(arbitrarystring, 2)))
arbitrarystring=arbitrarystring[:132]


print("first 132 bits:",arbitrarystring)
s=str(arbitrarystring)
groups= [s[i:i+6] for i in range(0,len(s),6)]

print(groups)
padgroup=[s[i:i+6] for i in range(0,len(s),6)]

#print(padgroup)


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
"D ",
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

## Note/CONSIDERATION: Last four punctuation characters "{|}`" have been omitted from the above list, and even though they exists in the encoder python app it never appears in results (perhaps should be added here so a warning/error would trigger if those values ever appear in results or when entered into a decoder.

#OLD jolly=[padgroup[i:i+6] for i in range(0,len(base64library[0]),6)]
index=[padgroup[i:i+22] for i in range(0,len(str(padgroup[0])),6)]
print('Index:', index)

First=int((padgroup[0]),2)

#First=bin(First)

print(base64library[First])

Second=int(padgroup[1],2)

print(base64library[Second])
Third=int(padgroup[2],2)
print(base64library[Third])
Fourth=int(padgroup[3],2)
print(base64library[Fourth])
Fifth=int(padgroup[4],2)
print(base64library[Fifth])
Sixth=int(padgroup[5],2)
print(base64library[Sixth])
Seventh=int(padgroup[6],2)
print(base64library[Seventh])
Eigth=int(padgroup[7],2)
print(base64library[Eigth])
Ninth=int(padgroup[8],2)
print(base64library[Ninth])
Tenth=int(padgroup[9],2)
print(base64library[Tenth])
Eleventh=int(padgroup[10],2)
print(base64library[Eleventh])    
Twelfth=int(padgroup[11],2)
print(base64library[Twelfth])
Thirteenth=int(padgroup[12],2)
print(base64library[Thirteenth])
Fourteenth=int(padgroup[13],2)
print(base64library[Fourteenth])
Fifteenth=int(padgroup[14],2)
print(base64library[Fifteenth])
Sixteenth=int(padgroup[15],2)
print(base64library[Sixteenth])
Seventeenth=int(padgroup[16],2)
print(base64library[Seventeenth])
Eighteenth=int(padgroup[17],2)
print(base64library[Eighteenth])
Nineteenth=int(padgroup[18],2)
print(base64library[Nineteenth])
Twentieth=int(padgroup[19],2)
print(base64library[Twentieth])
TwentyFirst=int(padgroup[20],2)
print(base64library[TwentyFirst])
TwentySecond=int(padgroup[21],2)
print(base64library[TwentySecond])

##
 
print(base64library[First],base64library[Second],base64library[Third],base64library[Fourth],base64library[Fifth],base64library[Sixth],base64library[Seventh],base64library[Eigth],base64library[Ninth],base64library[Tenth],base64library[Eleventh],base64library[Twelfth],base64library[Thirteenth],base64library[Fourteenth],base64library[Fifteenth],base64library[Sixteenth],base64library[Seventeenth],base64library[Eighteenth],base64library[Nineteenth],base64library[Twentieth],base64library[TwentyFirst],base64library[TwentySecond])
print(base64library[First]+base64library[Second]+base64library[Third]+base64library[Fourth]+base64library[Fifth]+base64library[Sixth]+base64library[Seventh]+base64library[Eigth]+base64library[Ninth]+base64library[Tenth]+base64library[Eleventh]+base64library[Twelfth]+base64library[Thirteenth]+base64library[Fourteenth]+base64library[Fifteenth]+base64library[Sixteenth]+base64library[Seventeenth]+base64library[Eighteenth]+base64library[Nineteenth]+base64library[Twentieth]+base64library[TwentyFirst]+base64library[TwentySecond])
print("Length of initial ent as hex:",len(hex(int("0b"+arbitrarystring, 2))))
