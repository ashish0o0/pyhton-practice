# Write a program to find the factorial of a number

def factorial(n):
    if n < 0:
        return "Invalid Input! Please eneter a non-negative integer"
    
    result = 1

    for i in range(1, n+1):
        result *= i

    return result

n = int(input("Enter the integer: "))
print(factorial(n))
