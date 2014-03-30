# Proj5.py, Fall 2013
#Let's Look up Information

#This project is written by: Yingzhu (Jacqueline) Zhang & John Chalovich.
#Contact information: email: yzhang21@email.wm.edu; phone number: 732-997-8980.
#Contact information: email: jtchalovich@email.wm.edu; cell: 215-595-8388.

#Using dictionaries, this program looks up information about a particular player
#as well as information about a particular team.

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
    
    pass_rating = (completions_calc + yards_calc + touchdowns_calc + \
                   interceptions_calc) / 6 * 100
    return pass_rating

#-------------------------------------------------------------------------------

def find_player_info(firstname_lastname): 
    
    """ Given a player's name, this procedure finds and prints a list of the 
    player's team, year and rating information in year order. Then finds and 
    prints his overall player rating."""
    
    if firstname_lastname in player_dict:
        player_stats = player_dict[firstname_lastname]
        player_stats.sort()
    
        print(firstname_lastname)
        
        
        for different_years_stat in player_stats:
            print("    played for %s in %s with a rating of %5.2f" % \
                  (different_years_stat[1], different_years_stat[0], \
                   different_years_stat[2]))
    else:
        print ("This player is not in the database") 
        print ()
    
        for name in name_rating_dict:
            last_first_name = [name.split(",")]
            first_last_name = str(last_first_name [::-1])
            if first_last_name in name_rating_dict:
                print ("%s has an overall rating of %f5.2" % \
                       firstname_lastname, total_pass_rating)   
                                                  
#-------------------------------------------------------------------------------

def find_team_info(team_initials):
    
    """ Given the team's initial, this procedure finds and prints a list of 
    player info of the team in year order."""
    
    if team_initials in team_dict:
        team_stats = team_dict[team_initials]
        team_stats.sort()
    
        team_full = team_dict[team_initials]
        
        for different_player_stat in team_stats:
            print("    %s played in %s with a rating of %5.2f" % \
                  (different_player_stat[1], different_player_stat[0], \
                   different_player_stat[2])) 
    else:
        print ("This team is not in the database")
        print ()

#-------------------------------------------------------------------------------

def find_overall_ratings():
    
    """ This function creates an empty list and fills it with the information 
    from the dictionary of names and overall ratings."""
    
    pass

def populate_the_dict ():
    
    """ This function populates player_dict for the players with their names 
    as keys and their year, team, and rating as values; or populates team_dict 
    for the teams with teams as keys and their year, name and rating as 
    values."""
    
    player_file = open("passers.csv", "r")
    player_file.readline()
    punctuation = string.punctuation
    
    for line in player_file:
        line = line.strip()
        line = line.strip(punctuation)
        stats_list = line.split(",")
        
        pass_rating = pass_rating_calc(stats_list[7], stats_list[6], stats_list[8],\
                             stats_list[9], stats_list[12])
        
        
        full_name_str = stats_list[0] + " " + stats_list[1]
        yr_team_rating = (stats_list[4], stats_list[3], pass_rating)
        
        if full_name_str not in player_dict:
            player_dict[full_name_str] = [(yr_team_rating)]
        else:
            player_dict[full_name_str].append(yr_team_rating)

        
        yr_name_rating = (stats_list[4], full_name_str, pass_rating)
        
        if stats_list[3] not in team_dict:
            team_dict[stats_list[3]] = [(yr_name_rating)]
        else:
            team_dict[stats_list[3]].append(yr_name_rating)
    
    
    player_file.close()

    return player_dict, team_dict

#-------------------------------------------------------------------------------

def name_rating_dict():
    """ This function populates name_rating_dict with each player's name as key 
    and his overall pass rating as value."""
    
    player_file = open("passers.csv", "r")
    player_file.readline()
    punctuation = string.punctuation
    
    parent_player_list = []
    
    for line in player_file:
        line = line.strip()
        line = line.strip(punctuation)
        stats_list = line.split(",")
        
        full_name_str2 = stats_list[1] + ", " + stats_list[0]
        player_list = [full_name_str2, stats_list[3], stats_list[6], \
                              stats_list[7], stats_list[8], stats_list[9], \
                              stats_list[12]]
        parent_player_list.append(player_list)
    
    player_file.close()
    parent_player_list.sort()
    
    
    unique_names = []
    
    for player_list in parent_player_list:
        if player_list[0] in unique_names:
            unique_names = unique_names
        else:
            unique_names.append(player_list[0])
    
    
    parent_overall_stats_list = []
    
    for name in unique_names:
        overall_stats_list = [name,0,0,0,0,0]
        for player_list in parent_player_list:
            if player_list[0] == name:
                overall_stats_list[1] += float(player_list[2])
                overall_stats_list[2] += float(player_list[3])
                overall_stats_list[3] += float(player_list[4])
                overall_stats_list[4] += float(player_list[5])
                overall_stats_list[5] += float(player_list[6])            
        parent_overall_stats_list.append(overall_stats_list)
  
  
    name_rating_dict = {}
    
    for overall_stats_list in parent_overall_stats_list:
        
        total_pass_rating = pass_rating_calc(overall_stats_list[2], \
                                             overall_stats_list[1], \
                                             overall_stats_list[3], \
                                             overall_stats_list[4], \
                                             overall_stats_list[5])
        
        name_rating_dict[overall_stats_list[0]] = total_pass_rating    
    
    return name_rating_dict

#-------------------------------------------------------------------------------

def menu_choice():
    
    """ This function prints out menu choice and returns user's input."""
    
    print("Menu choices")
    print(\
        "a) Find a passer and print his career information and overall rating")
    print("b) Find a team and print all the passers by year")
    print("c) Print a list of players and their ratings in alpha order")
    print("q) Quit")
    print()
    
    menu_choice = input("Enter choice: ")
    print(menu_choice)
    print()
    menu_choice.lower()
    
    
    return menu_choice

#-------------------------------------------------------------------------------

# Main part of the program.

import string
import sys


# Given: A dictinary of team initials and corresponding full names. 

teams = \
{'MIA': 'Miami', 'NO':'New Orleans', 'STL':'St. Louis','NE':'New England',\
'SD':'San Diego','HOU':'Houston','MIN':'Minnesota','IND':'Indianapolis',\
'TEN':'Tennessee','OAK':'Oakland','ARI':'Arizona','KC':'Kansas City',\
'SF':'San Francisco','GB':'Green Bay','DAL':'Dallas','DET':'Detroit',\
'BAL':'Baltimore','CLE':'Cleveland','CIN':'Cincinnati','WAS':'Washington',\
'DEN':'Denver','NYG':'New York Giants','NYJ':'New York Jets','SEA':'Seattle',\
'ATL':'Atlanta', 'CAR':'Carolina','PHI':'Philadelphia','BUF':'Buffalo',\
'CHI':'Chicago','TB':'Tampa Bay',  'PIT':'Pittsburgh','JAX':'Jacksonville',\
'BOS':'Boston', 'BCL': 'Baltimore Colts' , 'NYY': 'New York Yankees',\
'NYT': 'Newark Tornadoes','DTX':'Dallas Texans' ,'RAM': 'Los Angeles Rams',\
'RAI':'Oakland Raiders','LAD':'Los Angeles Dons','LAC':'Los Angeles Chargers',\
'CRD':'Chicago Cardinals'}

#-------------------------------------------------------------------------------

# Intialize empty dictionaries, open the file, populate player_dict with
# information on the players, team_dict with information on the teams, then 
# close the file. 

player_dict = {}
team_dict = {}

player_file = open("passers.csv", "r")
player_file.readline()
punctuation = string.punctuation

for line in player_file:
    line = line.strip()
    line = line.strip(punctuation)
    stats_list = line.split(",")
    
    pass_rating = pass_rating_calc(stats_list[7], stats_list[6], stats_list[8],\
                         stats_list[9], stats_list[12])
    
    
    full_name_str = stats_list[0] + " " + stats_list[1]
    yr_team_rating = (stats_list[4], stats_list[3], pass_rating)
    
    if full_name_str not in player_dict:
        player_dict[full_name_str] = [(yr_team_rating)]
    else:
        player_dict[full_name_str].append(yr_team_rating)
        
    
    yr_name_rating = (stats_list[4], full_name_str, pass_rating)
    
    if stats_list[3] not in team_dict:
        team_dict[stats_list[3]] = [(yr_name_rating)]
    else:
        team_dict[stats_list[3]].append(yr_name_rating)


player_file.close()

#-------------------------------------------------------------------------------

# Create a list of lists, containing the player's name, team, completions,
# attempts, total yardage, touchdowns, and interceptions.

player_file = open("passers.csv", "r")
player_file.readline()
punctuation = string.punctuation

parent_player_list = []

for line in player_file:
    line = line.strip()
    line = line.strip(punctuation)
    stats_list = line.split(",")
    
    full_name_str2 = stats_list[1] + ", " + stats_list[0]
    player_list = [full_name_str2, stats_list[3], stats_list[6], \
                          stats_list[7], stats_list[8], stats_list[9], \
                          stats_list[12]]
    parent_player_list.append(player_list)

player_file.close()
parent_player_list.sort()

#-------------------------------------------------------------------------------

# Create a list of unique player names.

unique_names = []

for player_list in parent_player_list:
    if player_list[0] in unique_names:
        unique_names = unique_names
    else:
        unique_names.append(player_list[0])

# Referencing the list of unique names, create a list which sums every players'
# completions, attempts, yardage, touchdowns, and interceptions accross every 
# year in order to then calculate their overall passer rating.

parent_overall_stats_list = []

for name in unique_names:
    
    # overall_stats_list[0] = name, [1] = completions, [2] = attempts,
    # [3] = yardage, [4] = touchdowns, [5] = interceptions
    
    overall_stats_list = [name,0,0,0,0,0]
    for player_list in parent_player_list:
        if player_list[0] == name:
            overall_stats_list[1] += float(player_list[2])
            overall_stats_list[2] += float(player_list[3])
            overall_stats_list[3] += float(player_list[4])
            overall_stats_list[4] += float(player_list[5])
            overall_stats_list[5] += float(player_list[6])            
    parent_overall_stats_list.append(overall_stats_list)


# Calculate an overall passing rating for each player. Then, 
# create another list contaning each player's rating and name. Sort this list 
# so that the player with highest rating comes first. 

name_rating_dict = {}

for overall_stats_list in parent_overall_stats_list:
    
    total_pass_rating = pass_rating_calc(overall_stats_list[2], \
                                         overall_stats_list[1], \
                                         overall_stats_list[3], \
                                         overall_stats_list[4], \
                                         overall_stats_list[5])
    
    name_rating_dict[overall_stats_list[0]] = total_pass_rating

#-------------------------------------------------------------------------------

# Print out the menu and perform according to user's choice.

choice = menu_choice()

if choice != "q":
    
    if choice == "a":
        firstname_lastname = input("Enter the player's firstname lastname: ")
        print(firstname_lastname)
        find_player_info(firstname_lastname)
        
        choice = menu_choice()
    
    
    if choice == "b":
        team_initial = input("Enter the team's initials: ")
        print(team_initial)
        find_team_info(team_initial)
        
        choice = menu_choice()
        
        
    if choice == "c":
        players_overall_ratings = find_overall_ratings()
        print(players_overall_ratings)
        
        choice = menu_choice()
        
    
    if choice != "a" or "b" or "c":
        print("Illegal choice. Try again")
        
        choice = menu_choice()


else:
    print ("Thanks for playing")
    
    
