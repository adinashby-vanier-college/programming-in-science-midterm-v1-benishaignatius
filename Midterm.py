import math

# Q1: Calculate the area of a circle
def area_of_circle(radius):
    
    return (round( math.pi * ( radius ** 2 ), 2))

# Q2: Hollow Right Triangle
def hollow_right_triangle(n):

    if n<4:
        return "The triangle height should be at least 4."
    
    result = ""
    for i in range(1, n+1):
        if i==1 or i==n:
            result += "*" * i + "\n"

        else:
            result += "*" + " " * (i-2) + "*" + "\n"

    return result.rstrip()


# Q3: Inverted Pyramid
def inverted_pyramid(n):

    if n<3:
        return "The pyramid height should be at least 3."
    
    result = ""

    for i in range(1, n+1):
        star = "*" * (2 * ( n- i + 1) -1)
        spaces = " " * (i-1)
        result += spaces + star + "\n"

    return result.rstrip() 

# ----------------------------------------------------------------
print(area_of_circle(5))
print()

print(hollow_right_triangle(3))
print()

print(hollow_right_triangle(4))
print()

print(hollow_right_triangle(5))
print()

print(inverted_pyramid(3))
print()

print(inverted_pyramid(4))
print()

print(inverted_pyramid(5))
print()