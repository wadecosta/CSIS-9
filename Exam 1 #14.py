number = int(input("Please enter a number: "))
inout = input("Enter: inside or outside ")

if(inout == 'inside' and number>=1 and number<=10):
    print("Yes")
elif(inout == 'outside' and (number<1 or number>10)):
    print("Yes")
else:
    print ("No")
