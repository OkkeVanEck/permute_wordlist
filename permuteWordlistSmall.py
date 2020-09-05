#!/usr/bin/env python3

import argparse


leetDict = {
    'A': ['A', 'a', '4', '@', '^'],
    'a': ['a', 'A', '4', '@', '^'],
    'B': ['B', 'b', '8', '6'],
    'b': ['b', 'B', '8', '6'],
    'C': ['C', 'c', '(', '[', '{', '<'],
    'c': ['c', 'C', '(', '[', '{', '<'],
    'D': ['D', 'd', ')'],
    'd': ['d', 'D', ')'],
    'F': ['F', 'f'],
    'f': ['f', 'F'],
    'I': ['I', 'i', '!', '1'],
    'i': ['i', 'I', '!', '1'],
    'J': ['J', 'j', '1'],
    'j': ['j', 'J', '1'],
    'K': ['K', 'k', '('],
    'k': ['k', 'K', '('],
    'L': ['L', 'l', '1', '7', '!', 'i', '|'],
    'l': ['l', 'L', '1', '7', '!', 'i', '|'],
    'M': ['M', 'm', '^^', 'nn'],
    'm': ['m', 'M', '^^', 'nn'],
    'N': ['N', 'n', '^'],
    'n': ['n', 'N', '^'],
    'O': ['O', 'o', '0'],
    'o': ['o', 'O', '0'],
    'P': ['P', 'p', '9'],
    'p': ['p', 'P', '9'],
    'Q': ['Q', 'q', '9', '2', '0_'],
    'q': ['q', 'Q', '9', '2', '0_'],
    'R': ['R', 'r', '2', '12'],
    'r': ['r', 'R', '2', '12'],
    'S': ['S', 's', '5', '$', 'z', '2'],
    's': ['s', 'S', '5', '$', 'z', '2'],
    'T': ['T', 't', '7', '+'],
    't': ['t', 'T', '7', '+'],
    'U': ['U', 'u', 'v', 'V'],
    'u': ['u', 'U', 'v', 'V'],
    'V': ['V', 'v', 'u', 'U'],
    'v': ['v', 'V', 'u', 'U'],
    'W': ['W', 'w', 'vv', 'VV', 'uu', 'UU'],
    'w': ['w', 'W', 'vv', 'VV', 'uu', 'UU'],
    'X': ['X', 'x', '><', '}{', ')(', ']['],
    'x': ['x', 'X', '><', '}{', ')(', ']['],
    'Y': ['Y', 'y', 'j', 'J', '7'],
    'y': ['y', 'Y', 'j', 'J', '7'],
    'Z': ['Z', 'z', '2', 's'],
    'z': ['z', 'Z', '2', 's']
}


def permute(dictWord):
    if len(dictWord) > 0:
        currentLetter = dictWord[0]
        restOfWord = dictWord[1:]

        if currentLetter in leetDict:
            substitutions = leetDict[currentLetter] + [currentLetter]
        else:
            substitutions = [currentLetter]

        if len(restOfWord) > 0:
          perms = [s + p for s in substitutions for p in permute(restOfWord)]
        else:
          perms = substitutions

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
