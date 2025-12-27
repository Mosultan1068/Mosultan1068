'''
Temp Conversion for Python
this is part of the training
input the temp in celsius
output the temp in fahrenheit
'''

celcius = float(input('what is the temp in celsius?'))
print(celcius)
fahrenheit = (celcius * 9 / 5) + 32
print(f"The value in faranheit is {fahrenheit} ")

print("The value in faranheit is := " , fahrenheit ,"F")

fahrenheit = float(input('\nwhat is the temp in fahrenheit?'))
celcius = (fahrenheit - 32) * 5/9
print(f"The value in celcius is {celcius} c")
