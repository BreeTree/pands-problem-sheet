#Calculate BMI from weight and height
#Author: Breeda Herlihy

# input height and weight as integers
weight = int(input("Enter your weight(kg): "))
height = int(input("Enter your height(cm): "))

#convert height from centimetres to metres
heightMetres = height/100

#calculate BMI
answer = weight/(heightMetres*heightMetres)

# format the result to display two decimals
# https://www.w3schools.com/python/python_string_formatting.asp
txt = "The BMI is {:.2f}(kg/m²)"
print(txt.format(answer))