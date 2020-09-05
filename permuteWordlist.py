#!/usr/bin/env python3

import argparse


leetDict = {
    'A': ['A', '4', '@', '^', 'aye', 'Aye'],
    'a': ['a', '4', '@', '^', 'aye'],
    'B': ['B', 'L3', '8', '13', '!3', '|3', '/3', ')3', '(3', '6'],
    'b': ['b', 'L3', '8', '13', '!3', '|3', '/3', ')3', '(3', '6'],
    'C': ['C', '(', '[', '{', '<', 'k', 'K'],
    'c': ['c', '(', '[', '{', '<', 'k', 'K'],
    'D': ['D', ')', '|)', '(|', '[)', 'o|', '|>', '<|', '>', 'cl', '|}', '?'],
    'd': ['d', ')', '|)', '(|', '[)', 'o|', '|>', '<|', '>', 'cl', '|}', '?'],
    'F': ['F', 'ph', 'pH', 'Ph', 'PH', 'v', 'V'],
    'f': ['f', 'ph', 'pH', 'Ph', 'PH', 'v', 'V'],
    'I': ['I', 'l', '!', '1', 'eye', '3y3', '[]', ']['],
    'i': ['i', 'l', '!', '1', 'eye', '3y3', '[]', ']['],
    'J': ['J', '1', ';', ']'],
    'j': ['j', '1', ';', ']'],
    'k': ['k', '(', 'c', 'C', '>|', '|<', '1<', '|(', '|{', '|c'],
    'K': ['K', '(', 'c', 'C', '>|', '|<', '1<', '|(', '|{', '|c'],
    'L': ['L', '1', '7', '!', 'i', '|_', '|'],
    'l': ['l', '1', '7', '!', 'i', '|_', '|'],
    'M': ['M', 'JVI', '^^', '{V}', '{v}', '(V)', '(v)', 'nn', 'IVI'],
    'm': ['m', 'JVI', '^^', '{V}', '{v}', '(V)', '(v)', 'nn', 'IVI'],
    'N': ['N', '^'],
    'n': ['n', '^'],
    'O': ['O', '0', 'Q', '()', 'oh', '[]', 'p', '<>'],
    'o': ['o', '0', 'Q', '()', 'oh', '[]', 'p', '<>'],
    'P': ['P', '|*', '?', '|^', '|>', '|"', '9', '[]D', '|7'],
    'p': ['p', '|*', '?', '|^', '|>', '|"', '9', '[]D', '|7'],
    'Q': ['Q', '9', '()_', '2', '0_', '<|', '&'],
    'q': ['q', '9', '()_', '2', '0_', '<|', '&'],
    'R': ['R', 'I2', '|`', '|~', '|?', '/2', '|^', 'lz', '|9', '2', '12', '[z', '.-', '|2', '|-'],
    'r': ['r', 'I2', '|`', '|~', '|?', '/2', '|^', 'lz', '|9', '2', '12', '[z', '.-', '|2', '|-'],
    'S': ['S', '5', '$', 'z', 'ehs', 'es', '2'],
    's': ['s', '5', '$', 'z', 'ehs', 'es', '2'],
    'T': ['T', '7', '+', '-|-', '~|~'],
    't': ['t', '7', '+', '-|-', '~|~'],
    'U': ['U', '(_)', '|_|', 'v', 'V', 'L|'],
    'u': ['u', '(_)', '|_|', 'v', 'V', 'L|'],
    'V': ['V', 'u', 'U', '|/'],
    'v': ['v', 'u', 'U', '|/'],
    'W': ['W', 'vv', 'VV', '(n)', 'uu', 'UU', '2u', '2U'],
    'w': ['w', 'vv', 'VV', '(n)', 'uu', 'UU', '2u', '2U'],
    'X': ['X', '><', '}{', 'ecks', '?', ')(', ']['],
    'x': ['x', '><', '}{', 'ecks', '?', ')(', ']['],
    'Y': ['Y', 'j', 'J', '`/', '7'],
    'y': ['y', 'j', 'J', '`/', '7'],
    'Z': ['Z', '2', '7_', '-/_', '%', '>_', 's', '~/_', '-|_'],
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
