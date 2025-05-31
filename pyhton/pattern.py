# write a python program to construct the following pattern
'''
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''
# Number of rows for the pattern
n = 5

# First half of the pattern
for i in range(1, n +1):
    print("* " * i)

# Last half of the pattern
for i in range(n - 1, 0, -1):
    print("* " * i)