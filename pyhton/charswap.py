#Write a Python program to change a given string to a newly string where the first and last chars have been exchanged. 
def swap(s): 
    if len(s) < 2: 
        return "Not long enough" 
    return s[-1] + s[1:-1] + s[0]

s = input("Enter the string: ")
print(swap(s))
