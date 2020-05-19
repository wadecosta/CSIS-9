yourSpeed = int(input("Enter your speed: "))
limit = int(input("Enter the speed limit: "))
isBirthday = input("Is is your birthday? yes or no : ")

if(isBirthday == 'yes'):
    isBirthday = True
else :
    isBirthday = False

if isBirthday == True :
    fineAmount = 0
elif yourSpeed <= limit+10:
    # get off with warning
    fineAmount = 0
elif yourSpeed <= limit+30:
    fineAmount = 100
else:
    fineAmount = 200
if fineAmount == 0:
    print("You get a warning.")
else:
    print("Your fine is $"+str(fineAmount))
