#!/usr/bin/env python
"""Paul MacKay - V00967869"""

import sys

def sort(words):
    print("\n")
    uniq = list(set(words))
    print("Unique words: ", uniq, "\n")

    alph = sorted(uniq)
    print("Sorted alphabetically: ", alph, "\n")
    
    longest = max(uniq, key=len)
    print("Longest word: ", longest, "\n")

    shortest = min(uniq, key=len)
    print("Shortest word: ", shortest, "\n")
    print("List of all words: ", words, "\n")


def main():
    if len(sys.argv) < 2:
        print("usage:", sys.argv[0], "'some,string,with,words'")
        sys.exit(1)

    f = open(sys.argv[1], "rt")

    line = list(f)
    line = ''.join(line)
    word = line.split(",")
    
    sort(word)

    f.close()

if __name__ == "__main__":
    main()
