# CS 141 lab 11
# testPolygon.py
#
# Modified by: Yingzhu Zhang
#
# This program creates a Polygon class that implements methods such as: 
# returning the number of vertices that define the polygon, returning the 
# vertex stored at some index position within the list containing the 
# collection of vertices, returning the index of a given vertex within the list
# containing the collection of vertices, inserting the given vertex, deleting
# the given vertex and returning the total lengh of the perimeter of the 
# polygon.

from carpoint import Point

class Polygon:
    def __init__ (self, vertex1, vertex2, vertex3):
        self.vertexlist = []
        self.vertexlist.append(vertex1)
        self.vertexlist.append(vertex2)
        self.vertexlist.append(vertex3)
    
    def numVertices(self):
        return len(self.vertexlist)
    
    def getVertex(self, ndx):
        if ndx < len(self.vertexlist) and ndx >= 0:
            return self.vertexlist[ndx]
        else:
            return False
    
    def findVertex(self, vertex):
        index = 0
        t = 1
        for vertices in self.vertexlist:
            if vertices.isEqual(vertex):
                t = 0
                return index
            index += 1
        if t == 1:
            return False
        
    def insertVertex (self, vertex, afterNdx):
        afterNdx = int(afterNdx)
        if afterNdx > len(self.vertexlist) or afterNdx < 0:
            return False
        if afterNdx == len(self.vertexlist):
            self.vertexlist.insert(0, vertex)
            return True
        else:
            self.vertexlist.insert(afterNdx + 1, vertex)
            return True 
        
    def deleteVertex (self, ndx):
        if ndx > len(self.vertexlist) or ndx <0 or len(self.vertexlist) <= 3:
            return False
        else:
            self.vertexlist.pop (ndx)
        
    def perimeter (self):
        total = 0
        i = 0
        while i < len(self.vertexlist) - 1:
            total += self.vertexlist[i].distance(self.vertexlist[i + 1])
            i += 1
        total += self.vertexlist[i].distance(self.vertexlist[0])
        return total
                
            