# lab 3
# Wade Costa
import math
#part 1
# code for part 1 goes here
number1 = float(input('Enter The First Number '))
number2 = float(input('Enter The Second Number '))
average = (number1 + number2) / 2
print('average ','%.3f' % average)

#part 2
f = int(input('Enter the temperature in Fahrenheit ')) 
c = int(5/9 * (f - 32))
print ('Fahrenheit = ' , f, ' Centigrade = ' , c)

#part 3
import math
diameter = float(input('Enter the diameter of the sphere '))
radius = diameter / 2
volume = 4/3 * math.pi * radius**3
print ('Diameter =', '%.2f' % diameter, ' volume = ' , '%.2f' % volume) 

#part 4
firstName = str(input('What is your first name? '))
lastName = str(input('What is your last name? '))
fullName = str(firstName + ' ' + lastName)
print (fullName)
firstInital = firstName[0]
lastInital = lastName[0]
print(firstInital + lastInital)
print(lastName + ',' + ' '+ firstName)
CAP = str.upper(firstName + ' ' + lastName)
print(CAP)
# print full name 
# print initials
# print full name, last name first
# print capitalized name
