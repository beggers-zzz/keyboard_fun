# Author: Ben Eggers <ben.eggers36@gmail.com>
#
# This script reads dictionary.txt and checks to see if any two words
# are the result of the same sequence of key-presses, one on a qwerty
# keyboard and one on a dvorak keyboard.

# {qwerty -> dvorak} character. On qwerty, q = 1, w = 2, etc. We're also going
# to add ', ,, ;, and . because they're used as letters on the dvorak keyboard.

# I use a dvorak keyboard with a qwerty layout painted on the keys and
# jesus was this hard.
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

    # throw those suckers in a set
    words = set()
    for line in dict:
        assert len(line.split()) == 1  # sanity check
        words.add(line)

    # see if the dvorak-ized version of any word is also in our set
    for word in words:
        dv = dvorakize(word)
        if dv in words:
            report_match(word, dv)


def dvorakize(word):
    dv = ""
    for c in word:
        dv += CHAR_MAP[c]
    return dv


def report(q, dv):
    print("lol")


if __name__ == "__main__":
    main()
