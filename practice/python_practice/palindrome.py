# Write a program to find if the string is palindrome or not

def is_palindrome(s):
    return s == s[::-1]

s = input("Enter the string: ")
print(is_palindrome(s))