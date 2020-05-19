# cs9 exam 2 question 9
# catdog
def catdog(str):
# input str string 
# return count of occurrences of “cat” “dog” in str
#   
#  example:  catdog(“catcatdogdo”) returns 3
#            catdog(“parrot”) returns 0
#            catdog(“ca”) returns 0
#
  cat=0
  dog=0
  for i in range(0,len(str)):
    if str[i]=='c' and str[i+1]=='a' and str[i+2]=='t':
      cat=cat+1
    elif str[i]=='d' and str[i+1]=='o' and str[i+2]=='g':
      dog=dog+1
  return cat+dog


print('Welcome to cat-dog.  At the prompt enter a string.')
print('To quit the program, just hit the ENTER key')
while True:
   line = input('?')
   if line == '':
      break
   print(catdog(line))
print('thank you for using cat-dog')
