# Write a pyhton to count the number of characters in a string

def char_frequency (s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

text = input("Enter a string: ")
frequency = char_frequency(text)

for char, count in frequency.items():
    print(char, " : ", count)

