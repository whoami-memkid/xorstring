#!/usr/bin/python2.7
import sys

def usage():
    print "This script will xor your string with the int you pass"
    print "{} -s <string_to_encode> -k <key_int>".format(sys.argv[0])
    exit(0)

def string_to_bytes(string, key):
    # string vars for printing later
    length = len(string)
    string_to_bytes     = ""
    encoded_string      = ""
    char_string         = ""

    for i in range(length):

        # takes the whole string and turns it into printable hex
        # the format is \x41\x41\x41
        # you can copy and paste it into as the
        # string you will pass into the stack

        string_to_bytes += '\\x' + str(hex(bytearray(string, 'utf-8')[i])).strip('0x')
        encoded_string  += '\\x' + str( hex( bytearray(string, 'utf-8')[i] ^ key ) ).strip('0x')
        char_string     += chr( bytearray(string, 'utf-8')[i] ^ key )

    print "Text   : {}".format(string)
    print "Key    : {}".format(key)
    print "String : {}".format(string_to_bytes)
    print "Encoded: {}".format(encoded_string)
    print "Chars  : {}".format(char_string)

def main():
    # Flag Vars
    cli_args            = sys.argv
    string_to_encode    = ""
    key_int             = 0

    # Loop to set flag vars
    for i in range(len(cli_args)):
        if cli_args[i] == "-s" or i == "-S":
            string_to_encode = cli_args[i+1]
        elif cli_args[i] == "-k" or i == "-K":
            key_int = int(cli_args[i+1])
        elif i >= len(cli_args):
            usage()

    if string_to_encode == "":
        usage()

    # calling func()
    string_to_bytes(string_to_encode, key_int)


if __name__ == '__main__':
    main()
