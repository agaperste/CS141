# CS 141 Lab 10
# line.py
#
# Modified by: Yingzhu Zhang
#
# Defines a class that represents a line segment on a Cartesian plane.

from carpoint import Point

class LineSegment:

    # The class constructor that initializes a line segment by storing
    # the two end points in the two attributes self.pointA and self.pointB.
    def __init__(self, pointA, pointB):
        self.pointA = pointA
        self.pointB = pointB
        
    # Returns a string representation of the point. Automatically used
        # by the print() function when printing a Point object.
    def __str__(self):
        return '(' + str(self.xCoord) + ',' + str(self.yCoord) + ')' 
    
    # Returns the end point for pointA.
    def endPointA(self):
        return self.pointA
    
    # Returns the end point for pointB.
    def endPointB(self):
        return self.pointB
    
    # Determines if the line segment is vertical or parallel to the y-axis.
    def isVertical(self):
        return self.pointA.xCoord == self.pointB.xCoord

    # Determines if the line segment is vertical or parallel to the x-axis.
    def isHorizontal(self):
        return self.pointA.yCoord == self.pointB.yCoord
        
    # Determines if the line segment is vertical or parallel to another line 
    #segment. 
    def isParallel(self, otherLine):
        import math
        x_diff = self.pointA.getX() - otherLine.pointA.getX()
        x_diff2 = self.pointB.getX() - otherLine.pointB.getX()
        y_diff = self.pointA.getY() - otherLine.pointA.getX()
        y_diff2 = self.pointB.getY() - otherLine.pointB.getY()          
        return math.fabs(x_diff) == math.fabs(x_diff2) or math.fabs(y_diff) == \
               math.fabs(y_diff2)
    
    # Returns the length of the line segment.
    def length(self):
        import math
        x_diff = self.pointA.getX() - self.pointB.getX()
        y_diff = self.pointA.getY() - self.pointB.getY()
        distance = math.sqrt (x_diff **2 + y_diff **2)
        return distance
    
    # Returns the slope of the line segment.
    def slope(self):
        x_diff = self.pointA.getX() - self.pointB.getX()
        y_diff = self.pointA.getY() - self.pointB.getY()        
        if x_diff != 0:
            slope = y_diff / x_diff
            return slope
        else:
            return False
    
    # Returns a Point object that contains the midpoint of the line segment.
    def midPoint(self):
        mid_x = (self.pointA.getX() + self.pointB.getX()) / 2
        mid_y = (self.pointA.getY() + self.pointB.getY()) / 2
        mid_point = Point(mid_x,mid_y)
        return mid_point
        
        
        

