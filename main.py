# Write a Python program to get a string maade of the first 2 and the last 2 chars from a given string. If the string length is less than or equal to 3, return the original string 
x=input()
l=len(x)
if(l>3):
  print(x[:2]+x[l-2:l])
else:
  print(x)