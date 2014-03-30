# Proj6.py, Fall 2013
#Let's Look up Information

#This project is written by: Yingzhu (Jacqueline) Zhang & John Chalovich.
#Contact information: email: yzhang21@email.wm.edu; phone number: 732-997-8980.
#Contact information: email: jtchalovich@email.wm.edu; cell: 215-595-8388.

#Prologue

from Player import Player

#create player dictionary

def create_player_dict ():
    
    """ This function populates player_dict for the players with their names 
    as keys and their player object as values"""
    
    player_dict = {} 
    
    player_file = open("passers.csv", "r")
    player_file.readline()
    punctuation = string.punctuation
    
    for line in player_file:
        line = line.strip()
        line = line.strip(punctuation)
        stats_list = line.split(",")
        
        full_name_str = stats_list[0] + " " + stats_list[1]
        playerObject = Player(stats_list[0], stats_list[1])
        
        if full_name_str not in player_dict:
            player_dict[full_name_str] = [(playerObject)]
        else:
            player_dict[full_name_str].append(playerObject)
        
        # stats_list[0] first name, [1] last name, [2] position(QB), [3] team, 
        # [4] year, [5] unimportant, [6] completions, [7] attempts, 
        # [8] yardage, [9] touchdowns, [10] unimportant, [11] unimportant,
        # [12] interceptions
        playerObject.update(stats_list[3], stats_list[4], stats_list[6], \
                            stats_list[7], stats_list[8], stats_list[9], \
                            stats_list[12])
    
    player_file.close()

    return player_dict

#print alpha player list


def print_alpha_player_list():
    
    player_info_list = []
    
    for player_key in player_dict:
        player_value = player_dict[player_key]
        player_info_list.append(player_value)
    
    player_info_list.sort()
    

#get individual player information
