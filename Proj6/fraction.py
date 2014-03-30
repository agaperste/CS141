# CS 141 lab 11
# fraction.py
#
# Modified by: Yingzhu Zhang
#
# A class that represents a fraction or rational number.

import math
import sys

class Fraction:
    def __init__(self, num, den):
       # The denominator can not be zero. If it is, abort the program.
        if den == 0: 
            sys.exit("Divide by zero")
        
       # Compute the greatest common divisor and reduce the numerator
       # and the denominator.
        div = gcd(num, den)
        self.num = abs(num // div)
        self.den = abs(den // div)
      
       # A negative fraction will be indicated by a negative numerator. 
        if num * den < 0: 
            self.num = -self.num
    
    
    def getNum(self):
        return self.num

    
    def getDen(self):
        return self.den
    
    
    def __add__(self, rhsFrac):
        the_lcm = lcm(self.den, rhsFrac.den)
        numerator_sum = (the_lcm * self.num/self.den) + \
                       (the_lcm * rhsFrac.num/rhsFrac.den)
        return str(int(numerator_sum)) + "/" + str(the_lcm)
        
    
    def __sub__(self, rhsFrac):
        the_lcm = lcm(self.den, rhsFrac.den)
        numerator_dif = (the_lcm * self.num/self.den) - \
                       (the_lcm * rhsFrac.num/rhsFrac.den)
        return str(int(numerator_dif)) + "/" + str(the_lcm) 
     
    
    def __neg__(self):
        return -str(self.num) + "/" + str(self.den)
        
        
    def __eq__(self, rhsFrac):
        a = self.num
        b = self.den
        c = rhsFrac.num
        d = rhsFrac.den
        return  (a == c and b == d)
        
        
    def __str__(self):
        return str(self.num) + "/" + str(self.den) 
      

# greatest common divisor function
# param:
# bigger  int   one of the two numbers which is bigger than the other
# smaller int   one of the two numbers which is smaller than the other
#
# return: the greatest common divisor of bigger and smaller
def gcd(bigger, smaller):
    while smaller != 0:
        temp = smaller
        smaller = bigger % smaller
        bigger = temp
    return bigger

def lcm (b,d):
    """Calculate the lowest common multiple of two positive integers."""
    return (b*d)//gcd(b,d) 

