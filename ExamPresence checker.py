midicalcause= str(input("did you have a medical condition yes or no:"))
attend=int(input("What is your attendence input:"))

if (midicalcause=="yes"):
    print("You are allowed")
else:
    if (attend>=75):
        print("you are allowed")
    else:
        print("you aren't allowed")        