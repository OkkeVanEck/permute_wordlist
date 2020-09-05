#!/usr/bin/env python3

import argparse


leetDict = {
    'A': ['A', 'a', '4', '@', '^'],
    'a': ['a', 'A', '4', '@', '^'],
    'B': ['B', 'b', 'L3', 'l3', '8', '13', '!3', '|3', ')3', '(3', '6'],
    'b': ['b', 'B', 'L3', 'l3', '8', '13', '!3', '|3', ')3', '(3', '6'],
    'C': ['C', 'c', '(', '[', '{', '<', 'k', 'K'],
    'c': ['c', 'C', '(', '[', '{', '<', 'k', 'K'],
    'D': ['D', 'd', ')', '|)', '(|', '[)', 'o|', '|>', '<|', '>', 'cl', '|}', '?'],
    'd': ['d', 'D', ')', '|)', '(|', '[)', 'o|', '|>', '<|', '>', 'cl', '|}', '?'],
    'F': ['F', 'f', 'ph', 'pH', 'Ph', 'PH', 'v', 'V'],
    'f': ['f', 'F', 'ph', 'pH', 'Ph', 'PH', 'v', 'V'],
    'I': ['I', 'i', 'l', '!', '1', '[]', ']['],
    'i': ['i', 'I', 'l', '!', '1', '[]', ']['],
    'J': ['J', 'j', '1', ']'],
    'j': ['j', 'J', '1', ']'],
    'K': ['K', 'k', '(', 'c', 'C', '>|', '|<', '1<', '|(', '|{', '|c'],
    'k': ['k', 'K', '(', 'c', 'C', '>|', '|<', '1<', '|(', '|{', '|c'],
    'L': ['L', 'l', '1', '7', '!', 'i', '|_', '|'],
    'l': ['l', 'L', '1', '7', '!', 'i', '|_', '|'],
    'M': ['M', 'm', '^^', '{V}', '{v}', '(V)', '(v)', 'nn'],
    'm': ['m', 'M', '^^', '{V}', '{v}', '(V)', '(v)', 'nn'],
    'N': ['N', 'n', '^'],
    'n': ['n', 'N', '^'],
    'O': ['O', 'o', '0', 'Q', '()', '[]', 'p', '<>'],
    'o': ['o', 'O', '0', 'Q', '()', '[]', 'p', '<>'],
    'P': ['P', 'p', '|*', '?', '|^', '|>', '|"', '9', '|7'],
    'p': ['p', 'P', '|*', '?', '|^', '|>', '|"', '9', '|7'],
    'Q': ['Q', 'q', '9', '()_', '2', '0_', '<|', '&'],
    'q': ['q', 'Q', '9', '()_', '2', '0_', '<|', '&'],
    'R': ['R', 'r', 'I2', '|`', '|~', '|?', '/2', '|^', '|9', '2', '12', '[z', '|2'],
    'r': ['r', 'R', 'I2', '|`', '|~', '|?', '/2', '|^', '|9', '2', '12', '[z', '|2'],
    'S': ['S', 's', '5', '$', 'z', '2'],
    's': ['s', 'S', '5', '$', 'z', '2'],
    'T': ['T', 't', '7', '+', '-|-', '~|~'],
    't': ['t', 'T', '7', '+', '-|-', '~|~'],
    'U': ['U', 'u', '(_)', '|_|', 'v', 'V', 'L|'],
    'u': ['u', 'U', '(_)', '|_|', 'v', 'V', 'L|'],
    'V': ['V', 'v', 'u', 'U', '|/'],
    'v': ['v', 'V', 'u', 'U', '|/'],
    'W': ['W', 'w', 'vv', 'VV', '(n)', 'uu', 'UU', '2u', '2U'],
    'w': ['w', 'W', 'vv', 'VV', '(n)', 'uu', 'UU', '2u', '2U'],
    'X': ['X', 'x', '><', '}{', '?', ')(', ']['],
    'x': ['x', 'X', '><', '}{', '?', ')(', ']['],
    'Y': ['Y', 'y', 'j', 'J', '`/', '7'],
    'y': ['y', 'Y', 'j', 'J', '`/', '7'],
    'Z': ['Z', 'z', '2', '7_', '%', '>_', 's'],
    'z': ['z', 'Z', '2', '7_', '%', '>_', 's']
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
