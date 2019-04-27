//Author: Andrea Zuccarini @2019

//Version 1.01

// Example Test string target to decode: HELLOWORLD
// Each letter decodes to respective 6-bit group: "010001","001110","010101","010101","011000"," ", "100000","011000","011011","010101","001101",
// Each Word as Continous string "010001001110010101010101011000" "100000011000011011010101001101"
// Concatenation of both words into one string: "010001001110010101010101011000100000011000011011010101001101"
// Converted binary string to hex: "0x44e55562061b54d"


b64dict= {};

base64library=['0',
'1',
'2',
'3',
'4',
'5',
'6',
'7',
'8',
'9',
'A',
'B',
'C',
'D',
"E",
'F',
'G',
'H',
'I',
'J',
'K',
'L',
'M',
'N',
'O',
'P',
'Q',
'R',
'S',
'T',
'U',
'V',
'W',
'X',
'Y',
'Z',
'!',
'"',
'#',
'$',
'%',
'&',
"'",
'(',
')',
'*',
'+',
',',
'-',
'.',
'}',
':',
';',
'<',
'=',
'>',
'?',
'@',
'[',
'{',
']',
'^',
'_',
'`'];

for(var i=0;i<base64library.length;i++) {
    b64dict[base64library[i]] = i;
}

function zfill(source, length) {
  var source = source.toString();
  while(source.length < length) {
    source = '0' + source;
  }
  return source;
}

function decodeAsBin(string) {
    output = [];
    s='';
    for(var j=0;j<string.length;j++) {
      if(string[j] != ' ') {
        output.push(zfill(b64dict[string[j].toUpperCase()].toString(2), 6));
      }
    }
    return output.join('');
}

function decodeAsHex(string) {
  bin = decodeAsBin(string);
  output = [];
  s='';
  // Pad with 0 for binaries not divisible by 4, for hex conversion
  binModule = bin.length % 4;
  if(binModule != 0) {
    bin = zfill(bin, bin.length + 4 - binModule);
  }
  for(var i=0;i<bin.length;i=i+4) {
    output.push(parseInt(bin.slice(i,i+4), 2).toString(16));
  }
  return output.join('');
}

//hatdata2decode=prompt('Enter any combination of the following characters to decode without spaces: 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&()*+,-.{:;<=>?@[}]^_`:');
console.log(decodeAsBin('HELLOWORLD'));
console.log('0x' + decodeAsHex('HELLOWORLD'));


// test decode string "HELLOWORLD" should return the binary equivalent of hex: 0x44e55562061b54d
// test decode string "INVENTEDBYSTEVENHATZAKIS@2018" should return this hex 0x125df39774e34b89c74e7ce5d129d8ca512739080048 as equivalent in binary to this output: 010010010111011111001110010111011101001110001101001011100010011100011101001110011111001110010111010001001010011101100011001010010100010010011100111001000010000000000001001000

// Note/CONSIDERATION: In version 1.01 to resolve a rendering conflict, the Forward slash "/" and Backslash "\" characters have been swapped out and replaced by the closing curly bracket "}" and opening curly bracket "{" on purpose.
