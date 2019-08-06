import string
import secrets
import sys
import math

Author: Steven Hatzakis @ 2019

A cryptographically-secure password generator that uses Python's built-in "secrets" module and that is compatible with the Hatnotation library.

alphabet = ["0",
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
"{",
":",
";",
"<",
"=",
">",
"?",
"@",
"[",
"}",
"]",
"^",
"_",
"`"]
joinedalphabet="".join(alphabet)
print('this is the alphabet we will be using:',joinedalphabet, 
'which has', len(alphabet), 'characters (total 64), and where the length of passwords generated randomly from this alphabet will determine their strength in terms of bits of security (entropy).') 
print(len(string.ascii_letters + string.digits+ string.punctuation))

password22 = ''.join(secrets.choice(alphabet) for i in range(22))
password44 = ''.join(secrets.choice(alphabet) for i in range(44))
password64 = ''.join(secrets.choice(alphabet) for i in range(64))
password176 = ''.join(secrets.choice(alphabet) for i in range(176))


library=64 #used to calculate entropy

numberchars22=len(password22)
entropy22=library**numberchars22
logentropy22=math.log2(entropy22)
print(password22)
print("your above",len(password22), "character-long password has entropy of security in this many bits",int(logentropy22)) #sys.getsizeof(password20),"bits long")

numberchars44=len(password44)
entropy44=library**numberchars44
logentropy44=math.log2(entropy44)
print(password44)
print("your above",len(password44), "character-long password has entropy of security in this many bits",int(logentropy44))#sys.getsizeof(password79),"bits long")


numberchars64=len(password64)
entropy64=library**numberchars64
logentropy64=math.log2(entropy64)
print(password64)
print("your above",len(password64), "character-long password has entropy of security in this many bits" ,int(logentropy64))#,sys.getsizeof(password207),"bits long")

numberchars176=len(password176)
entropy176=library**numberchars176
logentropy176=math.log2(entropy176)
print(password176)
print("your above",len(password176), "character-long password has entropy of security in this many bits" ,int(logentropy176))#,sys.getsizeof(password207),"bits long")


print("START Alphabet",alphabet,"END Alphabet")

