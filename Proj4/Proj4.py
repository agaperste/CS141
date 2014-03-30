#Proj4.py
#Fall 2013
#Who Are the Greatest Passers in Football History
#
#This project is written by: Yingzhu (Jacqueline) Zhang & John Chalovich.
#Contact information: email: yzhang21@email.wm.edu; phone number: 732-997-8980.
#Contact information: email: jtchalovich@email.wm.edu; cell: 215-595-8388.
#
#This program finds the best passers in NFL history. It gets the raw NFL stats 
#from a supplied file, computes the passing rating of over 1000 passers and 
#outputs the 50 most efficient players, as well as: (1) the player who passed
#for the most yards in a year; (2) the player who passed for the most touchdowns
#in a year; (3) the player who has the highest completions per attempted pass;
#(4) the player who has the highest yardage per attempted pass; and (5) the
#player who got the most interceptions. It also allows the user to search for
#a specific player to find their overall rating.

#-------------------------------------------------------------------------------

def pass_rating_calc(attempts, completions, yards, touchdowns, interceptions):
    
    """Given a quarterbacks's pass completions, pass attempts, total passing 
    yards, total passing touchdowns, and total interceptions, this function 
    calculates the passer rating of a quarterback."""
    
    attempts = int(attempts)
    comp_per_att = int(completions) / attempts
    yards_per_att = int(yards) / attempts
    touch_per_att = int(touchdowns) / attempts
    inter_per_att = int(interceptions) / attempts
    
    completions_calc = (comp_per_att * 100 - 30) / 20
    yards_calc = (yards_per_att - 3) / 4
    touchdowns_calc = touch_per_att * 20
    interceptions_calc = 2.375 - inter_per_att * 25
    
    pass_rating_1 = (completions_calc + yards_calc + touchdowns_calc + \
                   interceptions_calc) / 6 * 100
    return pass_rating_1

#-------------------------------------------------------------------------------

def most_players(passer_file, index):
    
    """This function calculates the total value for a particular stat of all the
    players and finds the player who has the highest value for that particular 
    stat."""
    
    passer_file.seek(0)
    
    composite_stats_list = []
    player = passer_file.readline()
    
    for player in passer_file:
        player = player.strip()
        player_list = player.split(',')
            
        first_name = player_list[0]
        last_name = player_list[1]
        team = player_list[3]
        season = int(player_list[4])
        name = first_name + " " + last_name
        particular_stat = int(player_list[index])
            
        total_stats_list = [particular_stat, name, team, season]
        composite_stats_list.append(total_stats_list)
        
        composite_stats_list.sort()
        composite_stats_list.reverse()        
        
        best_particular_stat_player = composite_stats_list[0]
    
    return best_particular_stat_player

#-------------------------------------------------------------------------------

def highest_per_att_player(passer_file, index):
    
    """This function calculates the total value of a particular stat, divided 
    by the total attempted pass of all the players and finds the player who has 
    the highest particular stat per attempted pass."""       
    
    passer_file.seek(0)    
    
    composite_stat_per_att_stats_list = []
    player = passer_file.readline()
    
    for player in passer_file:
        player = player.strip()
        player_list = player.split(',')
            
        first_name = player_list[0]
        last_name = player_list[1]
        team = player_list[3]
        season = int(player_list[4])
        att = int(player_list[7])
        name = first_name + " " + last_name
        particular_stat = int(player_list[index])
        raw_stat_per_att = particular_stat / att
        
        stat_per_att_stats_list = [raw_stat_per_att, name, team, season]
        composite_stat_per_att_stats_list.append(stat_per_att_stats_list)
        
        composite_stat_per_att_stats_list.sort()
        composite_stat_per_att_stats_list.reverse()
        
        best_stat_per_att_player = composite_stat_per_att_stats_list[0]
    
    return best_stat_per_att_player

#------------------------------------------------------------------------------    
    
# Main part of the program.

# Convert each line of the file into a list of a player's statistics, store
# lists in a parent list. Condence sub-lists to include only name, year, team,
# and passer rating which you insert. Sort the parent list in reverse order to 
# rank the players in descending order according to passer rating.

import string

passer_file = open("passers.csv", "r")
passer_file.readline()
punctuation = string.punctuation
composite_stats_list = []

for line in passer_file:
    line = line.strip()
    line = line.strip(punctuation)
    stats_list = line.split(",")
    
    pass_rating = pass_rating_calc(stats_list[7], stats_list[6], stats_list[8],\
                     stats_list[9], stats_list[12])
    
    stats_list.insert(0, pass_rating)
    condenced_stats_list = [stats_list[0], stats_list[1], stats_list[2], \
                      stats_list[5], stats_list[4]]
    
    composite_stats_list.append(condenced_stats_list)

passer_file.close()
composite_stats_list.sort()
composite_stats_list.reverse()


# Print out the top 50 players in order from best passer rating to worst. 

count = 0
print()
print("The top 50 passers based on their passer rating in individual years \
are:")
print()
print("Name                        Year  Rating  Team")

for condenced_stats_list in composite_stats_list:
    if count < 50:
        player_stat = composite_stats_list[count]
        name = player_stat[1] + " " + player_stat[2]
        print("%-27s %-5s %-7.2f %-4s" % (name, player_stat[3], \
                                           player_stat[0], player_stat[4]))
        count += 1

#------------------------------------------------------------------------------

# Find the passer whose overall passer rating (over multiple years) is best.
# Create a parent list of sub-lists containing the passer's name, team,
# completions, attempts, total yardage, touchdowns, and interceptions. Sort the 
# list so that the sub-lists are in alphabetical order with all the 
# different years' information for a particular player together.


passer_file = open("passers.csv", "r")
passer_file.readline()
punctuation = string.punctuation
composite_list = []

for line in passer_file:
    line = line.strip()
    line = line.strip(punctuation)
    stats_list = line.split(",")
    
    # Redefine index 0 as first and last name.
    stats_list[0] = stats_list[0] + " " + stats_list[1]

    # Condence the stats_list to contain only name(0), team(3), completions(6)
    # attempts(7), passing yardage(8), touchdowns(9), interceptions(12)
    condenced_list = [stats_list[0], stats_list[3], stats_list[6], \
                      stats_list[7], stats_list[8], stats_list[9], \
                      stats_list[12]]
    
    composite_list.append(condenced_list)

passer_file.close()
composite_list.sort()


# Using the list of lists above, create a new list where each individual
# element is a unique player name, so every name is listed once.

unique_names = []
for player_list in composite_list:
    if player_list[0] in unique_names:
        unique_names = unique_names
    else:
        unique_names.append(player_list[0])


# Referencing the list of unique names, create a list which sums every players'
# completions, attempts, yardage, touchdowns, and interceptions accross every 
# year in order to then calculate their overall passer rating.

parent_list_of_overall_stats_list = []

for name in unique_names:
    
    # overall_stats_list[0] = name, [1] = completions, [2] = attempts,
    # [3] = yardage, [4] = touchdowns, [5] = interceptions
    
    overall_stats_list = [name,0,0,0,0,0]
    for condenced_list in composite_list:
        if condenced_list[0] == name:
            overall_stats_list[1] += float(condenced_list[2])
            overall_stats_list[2] += float(condenced_list[3])
            overall_stats_list[3] += float(condenced_list[4])
            overall_stats_list[4] += float(condenced_list[5])
            overall_stats_list[5] += float(condenced_list[6])            
    parent_list_of_overall_stats_list.append(overall_stats_list)
        

# Calculate an overall passing rating for each player. Then, 
# create another list contaning each player's rating and name. Sort this list 
# so that the player with highest rating comes first. 

parent_name_and_rate_list = []

for overall_stats_list in parent_list_of_overall_stats_list:
    
    total_pass_rating = pass_rating_calc(overall_stats_list[2], \
                                         overall_stats_list[1], \
                                         overall_stats_list[3], \
                                         overall_stats_list[4], \
                                         overall_stats_list[5])
    
    name_and_rate_list = [total_pass_rating, overall_stats_list[0]]
    parent_name_and_rate_list.append(name_and_rate_list)

passer_file.close()
parent_name_and_rate_list.sort()
parent_name_and_rate_list.reverse()


# Print out the person with the highest passer rating.

print()
print("%s %s %s %6.2f." % ("The best player is: ", \
                         parent_name_and_rate_list[0][1], \
                         "with an overall passer rating of", \
                         parent_name_and_rate_list[0][0]))


# Print out the remaining 19 players in the top 20 according to passer rating.

print()
print ("The remainder of the top 20 are:")
count = 2
for name_and_rate_list in parent_name_and_rate_list:
    if count <= 20:
        print("%2d   %-20s %6.2f" % (\
            count, parent_name_and_rate_list[count-1][1], \
            parent_name_and_rate_list[count-1][0]))
        count += 1
    
#-------------------------------------------------------------------------------

# Print out the person who passed for the most yardage.

passer_file = open("passers.csv", 'r')

print ()
print("The person who passed for the most yardage is:")
best_yds_player = most_players(passer_file, 8)
print("   %s passing %s yards for %s in %s." % \
      (best_yds_player[1], best_yds_player[0], \
       best_yds_player[2], best_yds_player[3]))


# Print out the person who scored the most passing touchdowns.

print ()
print ("The person who scored the most passing touchdowns is: ")
best_tds_player = most_players(passer_file, 9)
print ("   %s scoring %s touchdowns for %s in %s." % \
      (best_tds_player[1], best_tds_player[0], \
       best_tds_player[2], best_tds_player[3]))


# Print out the person who has the highest completions per attempted pass.

print ()
print ("The person who has the highest completions per attempted pass is: ")
best_comp_per_att_player = highest_per_att_player(passer_file, 6)
print ("   %s with a %5.2f percent completion rate for %s in %s." % \
      (best_comp_per_att_player[1], best_comp_per_att_player[0] * 100, \
       best_comp_per_att_player[2], best_comp_per_att_player[3]))


# Print out the person who has the highest yardage per attempted pass.

print ()
print ("The person who has the highest yardage per attempted pass is: ")
best_yds_per_att_player = highest_per_att_player(passer_file, 8)
print ("   %s with %4.1f yards per attemp for %s in %s." % \
      (best_yds_per_att_player[1], best_yds_per_att_player[0], \
       best_yds_per_att_player[2], best_yds_per_att_player[3]))


# Print out the person with the most interceptions in a season.

print ()
print ("The person with the most interceptions in a season is: ")
best_intcs_player = most_players(passer_file, 12)
print ("   %s with %s interceptions for %s in %s." % \
      (best_intcs_player[1], best_intcs_player[0], \
       best_intcs_player[2], best_intcs_player[3]))

print ()

#-------------------------------------------------------------------------------

# Ask the user if they are interested in a particular player. Anser "y" or "n".
# If yes, ask the user to enter the person's first name, then last name. Search
# the parent_name_and_rate_list and look for this person's first and last name.
# When found, print the name along with the overall passer rating. Continue to
# ask if the users are interested in a particular player. Quit when the users
# answer something other than yes.

choice = input("Are you interested in the overall rating of a particular \
player? ")
print(choice)
choice = choice.lower()

while choice == "y": 
    
    first_name = input("Enter the player's first name: ")
    print (first_name)
    last_name = input("Enter the player's last name: ")
    print (last_name)
    print ()
    name = first_name + " " + last_name
    
    for name_and_rate_list in parent_name_and_rate_list:
        if name_and_rate_list[1] == name:
            print("%s  %5.2f" % (name, name_and_rate_list[0]))
            print()
                
    choice = input("Are you interested in the overall rating of a particular \
player? ")
    print(choice)
    choice = choice.lower()
    
else:
    print("", end = "")