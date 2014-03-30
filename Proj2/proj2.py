# Proj2.py
# Fall 2013
# craps
#
# This project is written by: Yingzhu (Jacqueline) Zhang for cs141 section 01.
# Contact information: email: yzhang21@email.wm.edu; phone number: 7329978980. 
# 
# This program is to simulate the old gambling game, Craps.

import random


# Initialize the variables.

number_of_wins = 0
total_number_dice_rolled = 0
number_of_1 = 0
number_of_2 = 0
number_of_3 = 0
number_of_4 = 0
number_of_5 = 0
number_of_6 = 0

# Prompt the user for a random number generator seed.

seed_raw = input ("Please enter the random number generator seed: ")
print (seed_raw)
s = int (seed_raw)
random.seed(s)

# Prompt the user for the number of games to be played.

desired_number_of_games = input ("Please enter the number of games to play: ")
print (desired_number_of_games)
desired_number_of_games = int (desired_number_of_games)

# Similate the process of Craps.

actual_number_of_games = 0

while actual_number_of_games < desired_number_of_games:
    var1 = random.randint (1,6)
    var2 = random.randint (1,6)  
    
    if var1 == 1:
        number_of_1 += 1
    elif var1 == 2:
        number_of_2 += 1
    elif var1 == 3:
        number_of_3 += 1
    elif var1 == 4:
        number_of_4 += 1
    elif var1 == 5:
        number_of_5 += 1
    elif var1 == 6:
        number_of_6 += 1
    if var2 == 1:
        number_of_1 += 1
    elif var2 == 2:
        number_of_2 += 1
    elif var2 == 3:
        number_of_3 += 1
    elif var2 == 4:
        number_of_4 += 1
    elif var2 == 5:
        number_of_5 += 1
    else:
        number_of_6 += 1
    total_number_dice_rolled += 2
    point = var1 + var2
    if point == 7 or 11:
        number_of_wins += 1
        
        actual_number_of_games += 1        
    elif point == 2 or 3 or 12:
        number_of_wins += 0
        
        actual_number_of_games += 1        
    else:
        var3 = random.randint (1,6)
        var4 = random.randint (1,6)
        point2 = var3 + var4 
        total_number_dice_rolled += 2
        while (point2 !=point or point2 !=7):
            if var3 == 1:
                numer_of_1 += 1
            elif var3 == 2:
                number_of_2 += 1
            elif var3 == 3:
                number_of_3 += 1
            elif var3 == 4:
                number_of_4 += 1
            elif var3 == 5:
                number_of_5 += 1
            elif var3 == 6:
                number_of_6 += 1
            if var4 == 1:
                numer_of_1 += 1
            elif var4 == 2:
                number_of_2 += 1
            elif var4 == 3:
                number_of_3 += 1
            elif var4 == 4:
                number_of_4 += 1
            elif var4 == 5:
                number_of_5 += 1
            else:
                number_of_6 += 1
            var3 = random.randint (1,6)
            var4 = random.randint (1,6)            
            point2 = var3 + var4
            total_number_dice_rolled += 2
        
            
            
        if point2 == point:
            number_of_wins += 1
        elif point2 == 7:
            number_of_wins += 0
        actual_number_of_games += 1            
    

probability_to_win = number_of_wins / actual_number_of_games
probability_of_1 = number_of_1 / total_number_dice_rolled
probability_of_2 = number_of_2 / total_number_dice_rolled
probability_of_3 = number_of_3 / total_number_dice_rolled
probability_of_4 = number_of_4 / total_number_dice_rolled
probability_of_5 = number_of_5 / total_number_dice_rolled
probability_of_6 = number_of_6 / total_number_dice_rolled

# Print the outputs.

print ()
print ("We simulated", actual_number_of_games, "games of Craps.")
print ()
print ("In all, a die was tossed", total_number_dice_rolled, "times.")
print ("The numbers:           1        2        3        4        5        6" )
print ("Their frequencies:%8d %8d %8d %8d %8d %8d" % 
       (number_of_1, number_of_2, number_of_3,number_of_4, number_of_5, 
        number_of_6))
print ("Their probabilities: %8.4f %8.4f %8.4f %8.4f %8.4f %8.4f" % 
       (probability_of_1, probability_of_2, probability_of_3, probability_of_4, 
        probability_of_5, probability_of_6))
print ("Of the", actual_number_of_games, "simulated games, you won", 
       number_of_wins, "times.")
print ("So the probability of winning at Craps is: %8.4f" % 
       (probability_to_win))