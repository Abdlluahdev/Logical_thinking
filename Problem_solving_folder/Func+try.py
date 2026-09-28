'''
try:

  def show_nums():
   
    
    x ="hello"
    print(x)
   
  show_nums()
  print(x)
   
except NameError:
 print("name error")

try:
  num = 20
  def change_num():
    num = 50

    print(num)
  change_num()
  print(num)
except:
  print("something went wrong")

try :
  def get_num():
    x =int(input("enter a number "))
    
    print(x)
  get_num()
except ValueError:
  print("Enter a whole number")
try:
      
 def calculate():
   result = 100
   return result

 print(calculate())
 print(result)
except:
  print("name error")
'''
'''
try:
  def divide():
    
    while True :
      
      num1 = int(input("Enter a number1"))

  
        print("goodbye")
        break
      num2 = int(input("Enter a number2"))
      result = num1 / num2

      return result
      
   
  print(divide()) 
except ValueError:
  print("Please enter a number ")

except ZeroDivisionError:
  print("cannot divide by zero")
'''
try:
 def check_num():
   num= float(input("Enter float number:"))
   result = int(num)
   if result >0:
     return True
   else:
     return False
 print(check_num())
except ValueError:
  print("Please valid number")

try:
  def divide():
    n1 = int(input("Enter num1:"))
    n2 = int(input("Enter num2:"))
    while True:
      
    