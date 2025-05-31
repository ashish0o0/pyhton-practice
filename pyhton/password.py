# write a Python program to check the validity of passwords Input by users. 
'''

Password validity Rules: 
A valid password must: 

Be at least 8 characters long. 
Contain at least one lowercase letter. 
Contain at least one uppercase letter. 
Contain at least one digit (8-9). 
Contain at least one special character (@, #, &, $, %, etc.). 

'''
def is_valid_password(password): 

    #Check length (at least 8 characters) 
    if len(password) < 8: 
        return "Password must be at least 8 characters long."
    
    #Initialize flags for different character types 

    has_lower = False 
    has_upper = False 
    has_digit = False
    has_special = False 
    special_characters = "@#$%^&*!"

    #Check each character in the password 
    for char in password: 
        if char.islower(): 
            has_lower = True 
        elif char.isupper(): 
            has_upper = True 
        elif char.isdigit(): 
            has_digit = True 
        elif char in special_characters: 
            has_special = True

    #validate all conditions
    if not has_lower: 
        return "Password must contain at least one lowercase letter." 
    if not has_upper: 
        return "Password must contain at least one uppercase letter." 
    if not has_digit: 
        return "Password must contain at least one digit." 
    if not has_special: 
        return "Password must contain at least one special character (@, #, I, etc.)."

    return "Password is valid!" 

# Get user input
password = input("Enter a password: ")

# Validate and print the result 
print(is_valid_password(password)) 