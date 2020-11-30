# i). List down all the error types - using python program 

#Syntax error

a=3
b=2
print a+b

#Division by zero error

try:
  print(8/0)
except ZeroDivisionError:
  print("Division by zero error")

#Key error

try:
  a={'cat':'white','dog':'brown'}
  a['fish']
except KeyError:
  print("Key not found error")

#Module not found error
try:
  import module1
except ModuleNotFoundError:
  print("Module not found")


# ii). calculator
def calcii():
      try:
         a=int(input("enter number 1 : "))
         b=int(input("enter number 2 : "))
         c=input("Operation: +,-,*,/")
         if c=='+':
           print(" Addition :",a+b)
         elif c=='-':
           print(" Subtraction :",a-b)
         elif c=='*':
           print(" Multiplication :",a*b)
         elif c=='/':
           try:
             print(" Division :",a/b)
           except ZeroDivisionError:
             print("division by zero error")
      except ValueError:
         print("enter valid input")
calcii()


#Print one message if the try block raises a NameError and another for other errors
try:
  print(name)
except NameError:
  print("Name is not defined")
except:
  print("Other error has occured")


#Input inside the try catch block
try:
  series=int(input(" name a series : "))
  print(series)
except:
  print("An exception occurs")
