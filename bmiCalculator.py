#Write a Python program to calculate one body mass index(BMI).
#Find the formula online

print("BMI Calculator for python using function, simple one.")

#Calculation for BMI
def bmi(height,weight):
  total = weight / ( height * height )
  return total

#This function for choosing our BMI description
def choose(a):
  if ( a < 16):
   print("Severely Underweight")
  elif ( a >= 16 and a < 18.5):
    print("Underweight")
  elif ( a >= 18.5 and a < 25):
    print("Healthy")
  elif ( a >= 25 and a < 30):
    print("Overweight")
  elif ( a >= 30):
    print("Severely Overweight")
    
#Prompt a user to enter their height
def h():
  height=float(input("Enter your height(m): "))
  return height

#Prompt a user to enter their weight
def w():
  weight=float(input("Enter your weight(kg): "))
  return weight

result = bmi(h(),w())
print "Your BMI is : ",round(result,2)
choose(result)
