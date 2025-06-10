def isPalindrome(s):
    my_string = s.lower()
    new_arr = []
    Palindrome_is = False
    for char in my_string:
        if char.isalpha() or char.isdigit():
            new_arr.append(char)
    if new_arr == new_arr[::-1]:
        Palindrome_is = True
    return Palindrome_is
# s = "sajbf ksj df32 4edsf3468   7;liur@#$$ egzty"
# s = "0p"
s = "race a car"
# s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))

