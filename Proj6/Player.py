#Player.py

class Player (object):
    def __init__ (self, first, last):
        '''the constructor for a player'''
        self.first = first
        self.last = last
        self.rating = 0
        self.info = []


    def update(self, team, year, comp, att, yeards, tds, itcs):
        '''create a list of information for this player for this year and 
append it to the info field. Then call calcrating.'''


    def calcrating(self):
        '''go through all sub-lists in info adding up totals for comps, 
attempts, etc. Then calculate the overall rating for this player. Store it
in the instance variable "rating" '''


    def returnName(self):
        '''return the name of the player first last'''


    def returnReverseName(self):
        '''return the name of the player as last, first'''


    def __eq__ (self, other):
        '''determine if this person's name is the same as the other person's
name'''


    def __lt__(self,other):
        '''determine if this person's name is less than the other person's
name alphabetically'''


    def __gt__ (self, other):
        '''determine if this person's name is greater than the other person's
name alphabetically'''


    def __str__(self):
        '''return a string of the person's name and their rating in a nice
format'''


    def calc(self, sublist):
        '''calculate a passer rating for one sub-list year in  the info list'''


    def printInfo(self):
        '''print individual year information about his player including each 
year's passer rating. The list should be in year order. Use calc to assist.'''
