number = input("Enter Number")
def prime(number):
    count = 0
    i = 2
    while(i <= number//2):
        if(Number % i == 0):
            count = count + 1
            break
        i = i + 1

    if (count == 0 and number != 1):
        print(" %d" %number, end = '  ')
    number = number  + 1
prime(number)
