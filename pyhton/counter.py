text = input("Enter a string: ")
lll=0
letter_count = 0
digit_count = 0

for char in text:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1





    
print("No. of letters: ", letter_count)
print("No. of digits: ", digit_count)