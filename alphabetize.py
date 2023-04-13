#!/usr/bin/env python3

def alphabetical(s):                #Function to sort by alphabetical order
    
    words = s.split(", ")           # Strip commas

    words.sort()                    # Alphabetize

    
    betized = ", ".join(words)      # Comma's Back

    return betized

def properize(s):                   #Function to Capitalize all words and add an 'and'

    words = s.split(", ")           #Strip commas

    for i in range(len(words)):     #Iterate/Count numbers of words
        words[i] = words[i].strip().capitalize()    #Capitalize and remove spaces from all words

    properized = ", ".join(words)   #Comma's Back

    if len(words) > 1:              #Only add an and if there's more than one word
        properized = properized.rsplit(",", 1)[0] + ", and" + properized.rsplit(",", 1)[1]
                                    #Add the and, but only before the last word
    return properized

if __name__ == "__main__":                      #Standalone
    s = input("Please enter a string of words separated by commas: \n")
    betized = alphabetical(s)                   #Perform function on input
    print("In alphabetical order:\n", betized)  #Print

    decision = input("\nWould you like to capitalize this string?\nType 'y' to Proceed or 'n' to Quit:\n")                 #Added this because not everyone wants to capitalize every word
    if decision == 'y':
        properized=properize(betized)    #Feed output from first function to second function     
        print("Here's your fancy string:\n", properized)   
    else:           
        print("Thank you, have a nice rest of your day!")          
        quit