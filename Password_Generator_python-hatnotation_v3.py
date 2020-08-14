import string
import secrets
import sys
import math

#Author:  © Steven J Hatzakis, 2020

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
print('This is the alphabet we will be using:',joinedalphabet, 'which has', len(alphabet), 'characters (total 64), and where the length of passwords generated randomly from this alphabet will determine their strength in terms of bits of security (entropy).') 
print(len(string.ascii_letters + string.digits+ string.punctuation))

# total printable is 95 with whitespace:
#'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ '
char=int(input('Please enter a number (i.e. enter ''22'' for a 22-character password with 128 bits of security):'))
password = ''.join(secrets.choice(alphabet) for i in range(char))

library=64 #used to calculate entropy

numberchars=len(password)
entropy=library**numberchars
logentropy=math.log2(entropy)
print(password)
print("your above",len(password),
      "character-long password has entropy of security in this many bits",
      int(logentropy))



