"""
1. Python program to print the area and perimeter for :
-> square
-> rectangle
-> circle
-> sphere
"""
from constant import pi
class area_perimeter:
    def square(self,side):
        area = side**2
        perimeter = 4*side
        print("area = {0} perimeter = {1}".format(area,perimeter))

    def rectangle(self,length,breadth):
        area = length*breadth
        perimeter = 2*length*breadth
        print("area = {0} perimeter = {1}".format(area,perimeter))

    def circle(self,radius):
        area = pi*(radius**2)
        perimeter = 2*pi*radius
        print("area = {0} perimeter = {1}".format(area,perimeter))

    def sphere(self,radius):
        surface_area =  4*pi*(radius**2)
        print("surface_area = {0}".format(surface_area))
          
area = area_perimeter()
area.circle(int(input("Enetr radius")))
area.rectangle(int(input("Enetr length")),int(input("Enetr breadth")))
area.square(int(input("Enetr length")))
area.sphere(int(input("Enetr radius")))