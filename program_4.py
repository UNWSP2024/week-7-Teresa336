# Programmer: Teresa Fischer
# Date: 10/15/24
# Program #4: Coordinates

# Write a distance function that will take two 3-dimensional coordinates (as input) 
# and will return (as output) the distance between those points in space.  
# The 3-dimensional coordinates must be stored as tuples.

import math

def distance(coordinates1, coordinates2):
    distance_of_points = math.sqrt((coordinates2[0] - coordinates1[0]) ^ 2 + (coordinates2[1] - coordinates1[1]) ^ 2 + (coordinates2[2] - coordinates1[2]) ^ 2)
    return distance_of_points

# Now write a mainline that has the user enter the two tuples.
def main():
    try:
        print('For the first 3-dimensional coordinate:')
        list1 =((int(input('Enter an x value:'))), (int(input('Enter an y value:'))), (int(input('Enter an z value:'))))
        print('For the second 3-dimensional coordinate:')
        list2 = ((int(input('Enter an x value:'))), (int(input('Enter an y value:'))), (int(input('Enter an z value:'))))

        coordinates1 = tuple(list1)
        coordinates2 = tuple(list2)
    except ValueError:
        print('Invalid input. Please enter a valid integer')

# The mainline calls the distance function and stores the distance in a variable.
    total_distance = distance(coordinates1, coordinates2)
# The mainline then displays the distance.
    print('Distance between points:', total_distance)
# Also include exception handling to deal with faulty input.
# The distance between two points (x1,y1,z1) and (x2, y2, z2) is 
#    given by:   sqrt ((x2-x1)^2 + (y2 - y1)^2 + (z1 - z2)^2)

main()