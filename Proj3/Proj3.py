#Proj3.py
#Fall 2013
#Let's Play a Game

#This project is written by: Yingzhu (Jacqueline) Zhang & John Chalovich.
#Contact information: email: yzhang21@email.wm.edu; phone number: 732-997-8980.
#Contact information: email: jtchalovich@email.wm.edu; cell: 215-595-8388

#This program contains five word games defined as following:
#1. Find all the words of a particular length containing just a single vowel 
#that does not have a particular letter in it.
#2. Find all words that use each of letters "i", "j", "t", "x" exactly once.
#3. Find words that contain all but one of the letters in a given string. (The 
#letters in the string must be unique.)
#4. Find all the words containing all the letters of a particular word (in no 
#particular order).
#5. Find all the palindromes of a particular length.
# A main looping menu prompts users to select which game to play,
# and directs the code to execute the appropriate procedure that contains the
# game. When each game is ended, the menu is reprinted, and the user has the
# option to quit the menu and end the program.


# open the reference dictionary text file and initialize game_choice variable
dictionary = open("dictionary.txt", "r")
game_choice = ""

#-------------------------------------------------------------------------------

def a_game(dictionary_param):
    """Find all the words of a particular length containing just a single vowel 
    that does not have a particular letter in it."""
    
    dictionary.seek(0)
    length = input("Please enter the word length you are looking for: ")
    print(length)
    length = int(length)
    letter = input("Please enter the letter you'd like to exclude: ")
    print(letter)
    print()
    word_count = 0

    for word in dictionary_param:
        word = word.strip()
        vowel_str = "aeiou"
        vowels_in_word = ""
        
        for char in word:
            if char in vowel_str:
                vowels_in_word += char
        if len(vowels_in_word) == 1:
            if len(word) == length:
                if letter not in word:
                    print(word)
                    word_count += 1
    if word_count == 0:
        print("There are no words that fit this criteria.")

#-------------------------------------------------------------------------------

def b_game(dictionary_param):
    """Find all words that use each of letters "i", "j", "t", "x" exactly once.
    """
    dictionary_param.seek(0)
    word_count = 0
    
    for word in dictionary_param:
        word = word.strip()     
        
        if word.count("i") == 1 and word.count("j") == 1 and \
           word.count("t") == 1 and word.count("x") == 1:
            print(word)
            word_count =+ 1
    if word_count == 0:
        print("There are no words that fit this criteria.")           

#-------------------------------------------------------------------------------

def c_game(dictionary_param):
    """Find words that contain all but one of the letters in a given string. 
    (The letters in the string must be unique.)"""
    
    dictionary.seek(0)
    reference_string = input("Please enter a string of characters: ")
    print(reference_string)
    print()
    word_count = 0
    
    for word in dictionary_param:
        word = word.strip()
        count = 0        
        for char in reference_string:
            if char in word:
                count += 1
        if count + 1 == len(reference_string):
            print(word)
            word_count += 1
    if word_count == 0:
        print("There are no words that fit this criteria.")  

#-------------------------------------------------------------------------------

def d_game(dictionary_param):
    """Find all the words containing all the letters of a particular word (in 
    no particular order)."""  
    
    dictionary.seek(0)
    reference_word = input("Enter word: ")
    print(reference_word)
    length = input("What is the maximum length of the words you want: ")
    print(length)
    length = int(length)
    print()
    word_count = 0
    
    for dictionary_word in dictionary_param:
        dictionary_word = dictionary_word.strip()
        if len(dictionary_word) <= length:
            overlap_characters = ""
            dictionary_word_dup = dictionary_word
            for char in reference_word:
                if char in dictionary_word_dup:
                    overlap_characters += char
                    dictionary_word_dup = dictionary_word_dup.replace(char,"",1)
            if len(reference_word) == len(overlap_characters):
                print(dictionary_word)
                word_count += 1
    if word_count == 0:
        print("There are no words that fit this criteria.") 

#-------------------------------------------------------------------------------

def e_game(dictionary_param):
    """This procedure finds palindromes of specified length in text file"""
    
    dictionary.seek(0)            
    length = input("Enter length of desired words. ")
    print(length)
    length = int(length)

    count = 0
    print()
    for word in dictionary_param:
        word = word.strip()
        if len(word) == length:
            if word == word[::-1]:
                print(word)
                count += 1
                
    if count == 0:
        print("There are no words that fit this criteria.")

#-------------------------------------------------------------------------------

# Main menu section of the code. It is a loop that is repeated
# until the user enters q and exits the loop, quitting the game and closing
# the dictionary text file and program.

while game_choice != "q":
    game_choice = input("""
Choose which game you want to play
a) Find words with only one vowel and excluding a specific letter
b) Find words with i, j, t, and x.
c) Find words containing all but one letter of a given string.
d) Find words containing all the letters of another word with a maximum\
length.
e) Find palindromes of a particular length.
q) Quit

Enter choice: """)
    
    print(game_choice)
    game_choice = game_choice.lower()
    print("")

# execute a_game procedure if user enters a
    if game_choice == "a":                                          
        a_game(dictionary)     

# execute b_game procedure if user enters b                
    elif game_choice == "b":              
        b_game(dictionary)   

# execute c_game procedure if user enters c        
    elif game_choice == "c":
        c_game(dictionary)

# execute d_game procedure if user enters d        
    elif game_choice == "d":      
        d_game(dictionary)        

# execute e_game procedure if user enters e        
    elif game_choice == "e":        
        e_game(dictionary) 

# if user enters q, print nothing        
    elif game_choice == "q":
        print("", end = "")

# if the user enters an invalid menu option, print error message        
    else:
        print("You've entered an incorrect choice. Try again")

# close dictionary text file and program if user enters q
else:
    print("Thanks for playing")
    dictionary.close()