units=int(input("What is the number of units consumed"))
if (units<=50):
    amount=units+(units/2)
    surcharge=25
elif (units<=100):
    amount=units+(units/2)
    surcharge=50    
elif (units<=150):
    amount=units+(units/2)
    surcharge=75
elif (units<=200):
    amount=units+(units/2)
    surcharge=100
else:
    amount=units+(units/2)*2
    surcharge=150   
print("You bill is",amount ,"and the surcharge wil be :",surcharge)                     