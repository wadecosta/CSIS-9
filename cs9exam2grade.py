# cs9 exam 2  question 8
#  grades
grades=[]
while True:
   line = input('Enter a grade or end? ')
   if line=='':
      line = line + [grades]
      
   elif line == 'end':
      break
   grades = grades + [ int(line) ]
#  write code to sum and average the grades
summ = sum(grades)
avg = float(summ / len(grades))

#  print sum and average
print('The sum is: ' , summ)
print('The average is: ' , avg)

#  determine and print the letter grade  
print("The letter grade is: ")
if int(avg) >= 90:
   print('A')
elif int(avg) >= 80:
   print('B')
elif int(avg) >= 70:
   print('C')
elif int(avg) >= 60:
   print('D')
else:
   print('F')

#  extra credit:  print the highest and lowest grade

print('The higest grade is: ' , max(grades))
print('The lowest grade is: ' , min(grades))
