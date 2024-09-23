age = int(input("How old are you?:"))

if age >= 10 and age < 20:
    print("You are allowed in class. Age limit is between 10 and 20.")
elif age < 10 or age >= 20:
    print("You are not allowed in class.")