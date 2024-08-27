import math

def area_of_circle(radius):
    return math.pi * radius ** 2

def area_of_rectangle(length, width):
    return length * width

radius = 5
length = 10
width = 6

circle_area = area_of_circle(radius)
rectangle_area = area_of_rectangle(length, width)

print(f"Area of the circle with radius {radius} is {circle_area:.2f}.")
print(f"Area of the rectangle with length {length} and width {width} is {rectangle_area:.2f}.")




