import math

maximum = int(input(" Please Enter the Maximum Value: "))
n = int(input("Enter Vaue of N")
for Number in range(1, maximum,n):
    temp = Number
    Sum = 0
    while(Temp > 0):
        Reminder = temp % n
        Factorial = math.factorial(Reminder)
        Sum = Sum + Factorial
        temp = temp // n
    
    if (Sum == Number):
        print(" %d is a Strong Number" %Number)
