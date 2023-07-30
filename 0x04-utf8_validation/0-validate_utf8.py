#!/usr/bin/env python3
""" a method that determines given data set repersents\
        a valid UTF-8 encoding """


def validUTF8(data):
    """ checks utf8 valid data set """
    for byt in data:
        bin_char = format(byt, '08b')

        if bin_char.startswith('0'):
            continue
        elif bin_char.startswith('110'):
            continue
        elif bin_char.startswith('1110'):
            continue
        elif bin_char.startswith('11110'):
            continue
        else:
            return False
    return True
