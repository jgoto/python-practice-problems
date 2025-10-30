# F = (C * (9 / 5)) + 32
# C = (5 / 9)(F-32)

def celsius_fahrenheit(temp):
	return (temp * ( 9 / 5 )) + 32

def fahrenheit_celsius(temp):
	return ( 5 / 9 )*(temp - 32)

print('100 C is ' + str(round(celsius_fahrenheit(100),1)) + ' fahrenheit') 
print('26 C is ' + str(round(celsius_fahrenheit(26),1)) + ' fahrenheit') 
print('32 F is ' + str(round(fahrenheit_celsius(32),1)) + ' celsius') 
print('75 F is ' + str(round(fahrenheit_celsius(75),1)) + ' celsius') 

