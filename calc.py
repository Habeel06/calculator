import os
inp = input("Enter The Expression")
try:
  eval(inp)
except:
  print("Please Enter a Valid Expression")
  os.system("pause")
