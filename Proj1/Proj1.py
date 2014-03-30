#Proj1.py
#This project is written by: Yingzhu (Jacqueline) Zhang for cs141 section 01.
#Contact information: email: yzhang21@email.wm.edu; phone number: 7329978980. 

#Given the radius and the height of a right triangle, this program is to
#find the area and perimeter of that triangle, and the volume and surface
#area of a cone created by rotating the right triangle around the axis that
#is the height of the right triangle.



import math

# Prompting the user for radius and height.

radiusStr = input("Please enter the triangle's radius ==> ")
print(radiusStr)
radius = float(radiusStr)

heightStr = input("Please enter the triangle's height ==> ")
print(heightStr)
height = float(heightStr)


# Calculate the area and perimeter of the triangle.
# Calculate the volume and surface area of the cone. 

area = radius * height / 2
perimeter = radius + height + math.sqrt(radius ** 2 + height ** 2)
volume = math.pi * radius ** 2 * height / 3
surfaceArea = math.pi * radius * (radius + math.sqrt(radius ** 2 + 
                                                     height ** 2))

# Print output results.
print(" ")
print("-" * 40)
print(" ")

print("       The triangle's radius = %9.3f" % radius)
print("       The triangle's height = %9.3f" % height)
print("         The triangle's area = %9.3f" % area)
print("    The triangle's perimeter = %9.3f" % perimeter)
print("           The cone's volume = %9.3f" % volume)
print("     The cone's surface area = %9.3f" % surfaceArea)

print(" ")
print("-" * 40)
print(" ")

print("Thank you for using this program. ")
