Name = "Conrad Salazar"
Age = 19
Height = 6
FavColor = "black"
#print (Name)
#print (Age)
#print (Height)
#print (FavColor)
print (Name, Age, Height, FavColor)
print (f"Hello, I am {Name} and I am {Age} years old.")

print (f"""
Name: {Name}
Age: {Age}
Height: {Height}
Favorite Color: {FavColor}
""")

import math
circle_area = math.pi*5**2  # alt w/o math module: circle_area = 3.142*5**2
print (round(circle_area, 1))
print (round(math.sqrt(Age), 2))
print (f"""
SIN(Age): {round(math.sin(Age), 2)}
COS(Age): {round(math.cos(Age), 2)}
""")

print (f"""
{Age+5}
{Height-4}
{Age*Height}
{Height/2}
{Age%3}
{Age**2}
""")

#def celsius_to_fahrenheit():
#    print(f"{INP_F}\u00b0 Celsius is equal to {int((int(INP_F) * 9 / 5) + 32)}\u00b0 Fahrenheit.")
#def fahrenheit_to_celsius():
#    print(f"{INP_C}\u00b0 Fahrenheit is equal to {int((int(INP_C) - 32) * 5 / 9)}\u00b0 Celsius.")
#print ("This code will convert Fahrenheit to Celsius")
#print ("Enter a temperature value in Fahrenheit. Type C to convert from Celsius to Fahrenheit instead.")
#INP_C = input()
#while INP_C == "C" or "c":
#    print ("This code will convert Celsius to Fahrenheit.")
#    print ("Enter a temperature value in Celsius. Type F to convert from Celsius to Fahrenheit instead.")
#    INP_F = input()
#    if INP_F == "F" or "f":
#        fahrenheit_to_celsius()
#    else:
#        celsius_to_fahrenheit()
#    if INP_C != "F" or "f":
#        fahrenheit_to_celsius()
#
#print ("beep boop the code worked")


def celsius_to_fahrenheit(cel_temp):
    output_f = int(cel_temp * (9 / 5) + 32)
    print(f"{cel_temp}\u00b0C is equal to {str(output_f)}\u00b0F")

def fahrenheit_to_celsius(far_temp):
    output_c = int((far_temp - 32) * (5 / 9))
    print(f"{far_temp}\u00b0F is equal to {str(output_c)}\u00b0C")

print("This code will convert between Fahrenheit and Celsius or vice versa.")
print("Type C to convert from Celsius to Fahrenheit, type F to convert from Fahrenheit to Celsius.")
inp1 = input().strip().upper()
while inp1 == "C":
    print("This code will convert from Celsius to Fahrenheit. Type a value in Celsius.")
    temp_val_c = int(input())
    celsius_to_fahrenheit(temp_val_c)
    break
while inp1 == "F":
    print("This code will convert from Fahrenheit to Celsius. Type a value in Fahrenheit.")
    temp_val_f = int(input())
    fahrenheit_to_celsius(temp_val_f)
    break
if inp1 != "C" and inp1 != "F":
    print("Invalid input. Please restart the program and enter 'C' or 'F'.")