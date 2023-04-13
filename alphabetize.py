#!/usr/bin/env python3

def alphabetical(s):
    
    words = s.split(", ")       # Strip commas

    words.sort()                # Alphabetize

    
    betized = ", ".join(words)  # Comma's Back

    return betized

if __name__ == "__main__":      #Standalone
    s = input("Please enter a string of words separated by commas: \n")
    betized = alphabetical(s)
    print("In alphabetical order:\n", betized)