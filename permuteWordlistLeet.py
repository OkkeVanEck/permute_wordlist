#!/usr/bin/env python3

import argparse


leetDict = {
    'a': ['a', '/\\', '/-\\'],
    'c': ['c', '<'],
    'd': ['d', '[)'],
    'e': ['e', '3'],
    'g': ['g', '&'],
    'i': ['i', '!'],
    'j': ['j', ']', '(/'],
    'k': ['k', '|c'],
    'm': ['m', '/V\\'],
    'n': ['n', '[\\]'],
    'o': ['o', '()', '°'],
    'p': ['p', '|>'],
    't': ['t', '7'],
    'u': ['u', '|_|'],
    'w': ['w', '\\|/'],
    'y': ['y', '`/']
}


def permute(dictWord):
    if len(dictWord) > 0:
        currentLetter = dictWord[0]
        restOfWord = dictWord[1:]

        if len(restOfWord) > 0:
            if currentLetter in leetDict:
                perms = [sub + p for p in permute(restOfWord)
                         for sub in leetDict[currentLetter]]
            else:
                perms = [currentLetter + p for p in permute(restOfWord)]
        else:
            if currentLetter in leetDict:
                perms = leetDict[currentLetter]
            else:
                perms = [currentLetter]

        return perms


if __name__ == '__main__':
    parser = argparse\
                .ArgumentParser(description="Permutate words of a wordlist.")
    parser.add_argument("input_file", help="an input wordlist")
    parser.add_argument("output_file",
                        help="an output file for permuted wordlist")
    args = parser.parse_args()

    bplf = open(args.input_file, "r")
    profaneWords = bplf.read().splitlines()
    bplf.close()

    pplf = open(args.output_file, "w")

    print("Working...")

    for profaneWord in profaneWords:
        pplf.writelines([p + '\n' for p in permute(profaneWord)])

    pplf.close()

    print("Done.")
