import string
import binascii
import math
import secrets
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
	b64dict[base64library[i]]=i

def decodeAsBin(string):
	output=[]
	print(len(string))
	for j in range(len(string)):
		
		if(string[j]!=' '):
			output.append(bin(b64dict[string[j].upper()])[2:].zfill(6))
			
	return output	

print(decodeAsBin('hello world'))
