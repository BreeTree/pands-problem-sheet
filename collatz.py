# Program that reads an integer and performs a calculation
# known as the Collatz Conjecture
# Author: Breeda Herlihy

# solution adapted from 
# https://www.w3resource.com/python-exercises/challenges/1/python-challenges-1-exercise-23.php

# create a list
values = []

# input a positive value
value = int(input("Please enter a positive integer: "))
# add this value to the start of the list
values.insert(0, value)

# Have the program end if the current value is one.
while value > 1: 
# perform the Collatz conjecture
    if value % 2 == 0:
        value = value // 2
    else:
        value = 3 * value + 1
    # add the values to a list
    values.append(int(value))

#print the list
print(values)