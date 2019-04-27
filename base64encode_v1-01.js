//Author: Andrea Zuccarini @2019
// Version 1.01

//test binary data string: 0b010010010111011111001110010111011101001110001101001011100010011100011101001110011111001110010111010001001010011101100011001010010100010010011100111001000010000000000001001000

//test string as hex: '0x125df39774e34b89c74e7ce5d129d8ca512739080048'

//test string result :'INVENTEDBYSTEVENHATZAKIS@2018'

// legacy notes: #FIX: LEADING ZEROS LOST (i.e.w/ test string 0x064ce8c835f4d374e04e33244beccad0)
// also, even when no leading zero in string, the leading zeroes of the actual base64 character are discarded,
// as the encoding appears to happen from right to left, see this test string where leading zeroes of
// first char 2 are discarded, and last char is N  0xb13ae7e331ce9dfa59799e95ee8dc117

function base64en(address_hex) {  // important never to rename base64en to "base64" which can corrupt the Python installation.
    // (renamed alphabet to base64library below) alphabet = string.digits+string.ascii_uppercase+string.punctuation
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
    b64_string = '';
    // Convert hex to decimal
    address_int = parseInt(address_hex,16);
    // Append digits to the start of string
    while(address_int > 0) {
        digit = address_int % 64;
        digit_char = base64library[digit];
        b64_string = digit_char + b64_string;
        address_int = parseInt(address_int/64);
    }
    return b64_string;
}
//hexer=input('enter hex with pad');
hexer = '0x125df39774e34';
console.log(base64en(hexer));
console.log("The above is this many char's long: ", base64en(hexer).length);
