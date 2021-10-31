
units = int(input(" Please enter Number of Units you Consumed : "))

if(units <= 100):
    amount = 130 + ((units - 50) * 3.25)
    surcharge = 35
elif(units <= 200):
    amount = 130 + 162.50 + ((units - 100) * 5.26)
    surcharge = 45
elif(units <= 300):
    amount = 130 + 162.50 + 526 + ((units - 200) * 8.45)
    surcharge = 75
elif(units <= 400):
    amount = 150 + 168 + 566 + ((units - 300) * 8.0)
    surcharge = 60
else:
    
    amount = 150 + 168 + 566 + ((units - 400) * 9.0)
    surcharge = 60

total = amount + surcharge
print("\nElectricity Bill = %.2f"  %total)
