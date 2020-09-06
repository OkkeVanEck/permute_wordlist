#!/usr/bin/env python3

import argparse


leetDict = {
    'A': ['A', 'a'],
    'a': ['a', 'A'],
    'B': ['B', 'b'],
    'b': ['b', 'B'],
    'C': ['C', 'c'],
    'c': ['c', 'C'],
    'D': ['D', 'd'],
    'd': ['d', 'D'],
    'E': ['E', 'e'],
    'e': ['e', 'E'],
    'G': ['G', 'g'],
    'g': ['g', 'G'],
    'H': ['H', 'h'],
    'h': ['h', 'H'],
    'I': ['I', 'i'],
    'i': ['i', 'I'],
    'J': ['J', 'j'],
    'j': ['j', 'J'],
    'K': ['K', 'k'],
    'k': ['k', 'K'],
    'L': ['L', 'l'],
    'l': ['l', 'L'],
    'M': ['M', 'm'],
    'm': ['m', 'M'],
    'N': ['N', 'n'],
    'n': ['n', 'N'],
    'O': ['O', 'o'],
    'o': ['o', 'O'],
    'P': ['P', 'p'],
    'p': ['p', 'P'],
    'Q': ['Q', 'q'],
    'q': ['q', 'Q'],
    'R': ['R', 'r'],
    'r': ['r', 'R'],
    'S': ['S', 's'],
    's': ['s', 'S'],
    'T': ['T', 't'],
    't': ['t', 'T'],
    'U': ['U', 'u'],
    'u': ['u', 'U'],
    'V': ['V', 'v'],
    'v': ['v', 'V'],
    'W': ['W', 'w'],
    'w': ['w', 'W'],
    'X': ['X', 'x'],
    'x': ['x', 'X'],
    'Y': ['Y', 'y'],
    'y': ['y', 'Y'],
    'Z': ['Z', 'z'],
    'z': ['z', 'Z']
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
