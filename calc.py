import os
inp = input("Enter The Expression")
try:
  print(eval(inp))
  os.system("pause")
except:
  print("Please Enter a Valid Expression")
  os.system("pause")
