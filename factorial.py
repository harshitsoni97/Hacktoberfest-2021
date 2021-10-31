num = int(input("Enter a number: "))    
factorial = 1
def fact(num):
   if num < 0:    
      print(" Factorial does not exist for negative numbers")    
   elif num == 0:    
      print("The factorial of 0 is 1")    
   else:    
      for i in range(1,num + 1):    
          factorial = factorial*i
   return factorial
def print_fact(fact):
   print(fact)
 
print_fact(fact(num))
