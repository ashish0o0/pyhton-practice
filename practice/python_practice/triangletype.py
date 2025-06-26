# Write a program to check if a triangle is equelateral, scalene, isosceles

a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

def check_triangle(a, b, c):
    if a == b == c:
        print("The triangle is Equelateral.")
    elif a == b or b == c or a == c:
        print("The triangle is Isosceles.")
    else:
        print("The triangle is Scalene")

# check if the sides form a valid triangle
if a + b > c and a + c > b and b + c > a:
    check_triangle(a, b, c)
else:
    print("The given sides do not form a valid triangle.")
