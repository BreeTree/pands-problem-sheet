# Program that takes an inputted string and outputs it in reverse order skipping characters
# Author: Breeda Herlihy

string = input ("Please enter a sentence: ") 
#The quick brown fox jumps over the lazy dog.

# Step 1: Reverse the string, use a slice to step backwards
# https://www.w3schools.com/python/python_howto_reverse_string.asp
txtReverse = string[::-1]

# Step 2: Output every second character using the slice function, [start:stop:step]
# https://www.hashbangcode.com/article/slicing-arrays-and-strings-using-colon-operator-python
txtDrop = txtReverse[::2]
print(txtDrop)
