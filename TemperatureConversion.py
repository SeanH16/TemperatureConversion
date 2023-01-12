#Sean Holbrook
#CIS261
#TemperatureConversion

def celsius_to_fahrenheit(celsius):
    temperature = (9.0/5.0) * celsius
    fahrenheit = temperature + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    temperature = fahrenheit- 32
    celsius = temperature * (5.0/9.0)
    return celsius

#Write a for..in loop for calculating and displaying the Fahrenheit to Celsius conversion:


for fahrenheit in range(0, 212, 40):
    print(fahrenheit, "Fahrenheit = ", round(fahrenheit_to_celsius(fahrenheit), 2), "Celsius")
    
    

#Write a for..in loop for calculating and displaying the Celsius to Fahrenheit conversion:

for celsius in range(0, 100, 20):
    print(celsius, "Celsius = ", round(celsius_to_fahrenheit(celsius), 2), "Fahrenheit")

