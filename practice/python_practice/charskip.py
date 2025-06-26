# write a program to skip the character in a string
#If the string length is less than 2, return an error message 
def first_and_last_two(s): 
    if len(s) <2: 
        return "It must have at least 2 characters"
    return s[:2] +s[-2:]

s = input("Enter the string: ")
print(first_and_last_two(s))
