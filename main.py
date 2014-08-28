# -*- encoding: utf-8 -*-
# Author: Ben Eggers <ben.eggers36@gmail.com>
#
# This script reads dictionary.txt and checks to see if any two words
# are the result of the same sequence of key-presses, one on a qwerty
# keyboard and one on a dvorak keyboard.

import argparse


def main():
    parser = argparse.ArgumentParser(description="Find words in a \
dictionary that come from the same sequence of key strokes, one on a qwerty \
and the other on a dvorak keyboard. Skips words composed at least 50% of \
a's and m's, since those are the same on qwerty and dvorak.")
    parser.add_argument('--dict', dest='dict_file', action='store',
                        type=str, default='dictionary.txt',
                        help='The file to use as a dictionary. Must have \
exactly one word per line. Defaults to ./dictionary.txt.')
    parser.add_argument("--min", dest='min_length', action='store',
                        type=int, default=3, help='Minimum length of a word \
for it to be considered interesting enough to print. Defaults to 3.')
    args = parser.parse_args()

    dict = open(args.dict_file, "r")

    # throw those suckers in a set
    words = set()
    for line in dict:
        assert len(line.split()) == 1  # sanity check
        words.add(line.lower()[:-1])

    # see if the dvorak-ized version of any word is also in our set
    matches = []
    for word in words:
        dv = dvorakize(word)
        if dv in words and not trivial(dv, args.min_length):
            matches.append((word, dv))

    report_matches(matches)


def dvorakize(word):
    dv = ""
    for c in word:
        dv += CHAR_MAP[c]
    return dv


def trivial(word, length):
    """
    'a' and 'm' are the same in qwerty and dvorak, so if any word is composed
    of mostly these, we'll throw it away. We'll also allow throw away words
    shorter than the passed length.
    """
    bad_chars = word.count('a') + word.count('m')
    return bad_chars >= (len(word) / 2.) or len(word) < length


def report_matches(matches):
    if not matches:
        print("No matches found, homes")
    else:
        print("QWERTY\t\tDVORAK\n")
        for match in matches:
            print("%s\t\t%s" % match)


# {qwerty -> dvorak} characters.
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


if __name__ == "__main__":
    main()
