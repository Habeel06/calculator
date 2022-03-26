# Author:Habeel
print("Made my habeel")

x=int(input('Enter your 1st number:\n '))
y=int(input('Enter your 2nd number:'))
print("Write 1 to perform addition")
print("Write 2 to perform subtraction")
print("Write 3 to perform multiplication")
print("Write 4 to perform integer division")
print("Write 5 to perform division")
print("Write 6 to find remainder")
z=int(input("Write your number:"))
if z==1:
  print("The Sum of these two numbers is:",x+y)
elif z==2:
  print("The Difference  of these two numbers is:",x-y)
elif z==3:
  print("The Product of these two numbers is:",x*y)
elif z==4:
  print("The(quotient) integer division of these two numbers is:",x//y)
elif z==5:
  print("The quotient of these two numbers is:",x/y)
elif z==6:
  print("The remainder on dividing these two numbers is:",x%y)
else:
  print("NA")
  
