# Name:Jeewoo Lim
# SBUID: 115236466
##################### SCORE ######################
#######  Score:  2/10
#################################################
# Remove the ellipses (...) when writing your solutions.

# ---------------------------- Exercise I ---------------------------------------
# ----------------- Convert Fahrenheit to Celsius -------------------------------
# TODO: Complete the implementation of fahrenheit2celsius () and what_to_wear(). 

## your output  -> did not run for the test

# sweater
# 7.0710678118654755
# 32.0
# 27.440161448987652
# 27.527638409423474
# Traceback (most recent call last):
#   File "d:\CSE 101 Ass1\Assignment 1 - Functions and Arithmetic-04-05-2023-05-19-27\Jeewoolim\Homework_1.py", line 94, in <module>
#     what_to_wear(fahrenheit2celsius(fahrenheit))
# NameError: name 'fahrenheit2celsius' is not defined

def farenheit2celsius(farenheit):

    celsius = (5/9) * (farenheit - 32)

    return celsius

def what_to_wear (celsius):
    if celsius < -10:
        print('Puffy jacket')
    if -10 <= celsius <= 0:
        print('Scarf')
    if 0 < celsius <= 10:
        print("sweater")
    if 10 < celsius <= 20:
        print("Light jacket")
    if 20 < celsius:
        print('T-shirt')

farenheit=40
what_to_wear(farenheit2celsius(farenheit))


# ---------------------------- Exercise II --------------------------------------
# ----------------- Area and perimeter of a triangle  ---------------------------
# TODO: Fill the functions shoelace_triangle_area, euclidean_distance and
# compute_triangle_perimeter from scratch  

def shoelace_triangle_area(x1,x2,x3,y1,y2,y3):

    result = abs(((x1*y2 + x2*y3 + x3*y1)-(x1*y3 + x2*y1 + x3*y2))/2)

    return result

def euclidean_distance(x1, x2, y1, y2):
    d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    return d

x1= -4
x2= -5
x3= 3
y1= -4
y2= 5
y3= -3

print(euclidean_distance(x1, x3, y1, y3))
print(shoelace_triangle_area(x1, x2, x3, y1, y2, y3))

def compute_triangle_perimeter(x1, x2, x3, y1, y2, y3):
    s1= euclidean_distance(x1, x2, y1, y2)
    s2= euclidean_distance(x2, x3, y2, y3)
    s3= euclidean_distance(x1, x3, y1, y3)
    p= s1+s2+s3
    return p
print(compute_triangle_perimeter(x1, x2, x3, y1, y2, y3))

# ---------------------------- Exercise III -------------------------------------
# ----------------- Compute the area of a regular polygon -----------------------
# TODO: Fill the functions deg2rad, apothem  and polygon_area 


import math
def deg2rad(n):
   m=n*(math.pi/180)
   return m

def apothem(n, s):
    a = s / (2*math.tan((deg2rad(180/n))))
    return a

def polygon_area(n,s):
    A = (n*s*apothem(n, s))/2
    return A

length_side=4
number_sides=5
print(polygon_area(number_sides, length_side))

# ---------------------------- Test -------------------------------------
# The following lines are for testing purposes, and will not be part of
# your grade. You may freely modify the following codes.

# Exercise 1 test
fahrenheit = 40
what_to_wear(fahrenheit2celsius(fahrenheit))

# Exercise 2 test
x1, x2, x3, y1, y2, y3 = -4, -5, 3, -4, 5, -3 # declaration of the vertices of the triangle
area = shoelace_triangle_area(x1, y1, x2, y2, x3, y3)
perimeter = compute_triangle_perimeter(x1, y1, x2, y2, x3, y3)
print("The area of the triangle is : " + str(area) + " , its perimeter is : " + str(perimeter) )

# Exercise 3 test
number_sides = 5
length_side = 4
print ("The area of the polygon is : " + str(polygon_area(number_sides, length_side)))
