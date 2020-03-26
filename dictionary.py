import json
from difflib import get_close_matches
data = json.load(open("data.json"))
def meaning(word):
    if word in data:
        return word, data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        while True :
            print("\nDid you mean this ? : %s"%get_close_matches(word, data.keys())[0])
            decide = input("'Y' for yes or 'N' for no : ").lower()
            if decide == 'y':
                return get_close_matches(word, data.keys())[0], data[get_close_matches(word,data.keys())[0]]
            elif decide == 'n':
                return word,False
            else:
                print("\n=> Incorrect entry !!!") 
    else :
        return word, False

def opening():
    print('''
    ***********************
     WELCOME TO DICTIONARY
    ***********************
     @AUTHOR : SANKALP
    ***********************
    ''')
choice = True
opening()
while choice:
    word = input("\nEnter the word : ").lower()
    word,mean = meaning(word)

    if mean == False:
        print("\nWORD NOT FOUND !!")
    else:
        print("\nMeaning of {} is :\n\n=> {}".format(word,"\n=> ".join(mean)))
    choice = input("\nEnter 'Q' to quit or any character to continue : ").lower()
    if choice == 'q':
        print("\nThanks for using this dictionary.")
        choice = False
    else:
        choice = True


