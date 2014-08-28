# Author: Ben Eggers <ben.eggers36@gmail.com>
#
# This script reads dictionary.txt and checks to see if any two words
# are the result of the same sequence of key-presses, one on a qwerty
# keyboard and one on a dvorak keyboard.

# {qwerty -> dvorak} character. On qwerty, q = 1, w = 2, etc. We're also going
# to add ', ,, ;, and . because they're used as letters on the dvorak keyboard.
CHAR_MAP = {
        'q': '\'',
        'w': ',',
        'e': '.',
        'r': 'p',
        't': 'y',
        'y': 'f',
        'u': 'g',
        'i': 'c',
        'o': 'r',
        'p': 'l',
        'a': 'a',
        's': 'o',
        'd': 'e',
        'f': 'u',
        'g': 'i',
        'h': 'd',
        'j': 'h',
        'k': 't',
        'l': 'n',
        ';': 's',
        'z': ';',
        'x': 'q',
        'c': 'j',
        'v': 'k',
        'b': 'x',
        'n': 'b',
        'm': 'm',
        ',': 'w',
        '.': 'v',
        '/': 'z'
    }


def main():
    dict = open("dictionary.txt", "r")


if __name__ == "__main__":
    main()
