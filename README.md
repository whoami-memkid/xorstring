# xorstring


Script for xoring a whole string using an int

Useful when trying to get rid of bad

characters in a string that you want to push to

the stack.

# usage


./xorstring.py -s "/bin/sh" -k 16


Text   : /bin/sh

Key    : 16

String : \x2f\x62\x69\x6e\x2f\x73\x68

Encoded: \x3f\x72\x79\x7e\x3f\x63\x78

Chars  : ?ry~?cx



# output lines

Text: is the string you pass after -s, -S

Key: is the int you pass after -k, -K

String: is your string as string

Encoded: is your string xor'd with the key

Chars: is the characters that come out of the encoded bytes
