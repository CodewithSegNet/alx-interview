#!/usr/bin/python3
""" a method that determines given data set repersents\
        a valid UTF-8 encoding """


def validUTF8(data):
    """ checks utf8 valid data set """
    i = 0
    while i < len(data):
        """ convert the byte to binary """
        bin_char = format(data[i], '08b')

        if bin_char.startswith('0'):
            pass
        elif bin_char.startswith('110'):
            """ Two-byte character (110xxxxx 10xxxxxx) """
            if i + 1 >= len(data) or not format(data[i + 1], '08b')\
                    .startswith('10'):
                return False
            i += 1

        elif bin_char.startswith('1110'):
            """ Three-byte character (1110xxxx 10xxxxxx 10xxxxxx) """
            if i + 2 >= len(data) or not format(data[i + 1], '08b')\
                    .startswith('10') or not format(data[i + 2], '08b')\
                    .startswith('10'):
                return False
            i += 2

        elif bin_char.startswith('11110'):
            """ four-byte char (11110xxx 10xxxxxx 10xxxxxx) """
            if i + 3 >= len(data) or not format(data[i + 1], '08b')\
                    .startswith('10') or not format(data[i + 2], '08b')\
                    .startswith('10') or not format(data[i + 3], '08b')\
                    .startswith('10'):
                return False
            i += 3

        else:
            """ Invalid UTF-8 encoding """
            return False

        i += 1

    return True
