# tax calculator
# Wade Costa

print("Welcome to Wade's tax calculator")
print("Warning: do not use for real tax purposes")

income = float(input("What is your income? "))
dependents = int(input("How many dependents including yourself? "))
status = input("Are you married or single? ")

if status == 'single' :
    exemption = 5950
else :
    exemption = 11900

taxableIncome = income - (3800*dependents) - exemption

print(income, dependents, status, exemption, taxableIncome)

# use tax table to get taxRate

if status == 'single':
    # single tax table lookup
    if taxableIncome <= 8700 :
        taxrate = 0.10
    elif taxableIncome <= 35350 :
        taxrate = 0.15
    elif taxableIncome <= 85650 :
        taxrate = 0.25
    elif taxableIncome <= 178650 :
        taxrate = 0.28
    elif taxableIncome <= 388350 :
        taxrate = 0.33
    else :
        taxrate = 0.35

else :

    if taxableIncome <= 17400 :
        taxrate = 0.10
    elif taxableIncome <= 70700 :
        taxrate = 0.15
    elif taxableIncome <= 142700 :
        taxrate = 0.25
    elif taxableIncome <= 217450 :
        taxrate = 0.28
    elif taxableIncome <= 388350 :
        taxrate = 0.33
    else :
        taxrate = 0.35
    # married tax table lookup


tax = taxableIncome * taxrate
print("Your tax bill is $" , '%.2f'%tax)
