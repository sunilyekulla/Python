#If-Else statement
a=9
if(a>10):
    print("Value of a is greater than 10")
if(a<10):
    print("Value of a is lesser than 10")
else :
    print("Value of a is 10")

#If-Elif-Else statement
variable = {2.5:4}
if(type(variable)== int):
    print("Type of variable is integer")
elif(type(variable)== float):
    print("Type of variable is float")
elif(type(variable)== bool):
    print("Type of variable is bool")
elif(type(variable)== str):
    print("Type of variable is string")
elif(type(variable)== dict):
    print("Type of variable is dictionaries")
elif(type(variable)== list):
    print("Type of variable is list")
else:
    print("Type of variable is sunil")




age = 10
if (age >= 11):
    print("You are eligible to see the IPL.")
    if (age <= 20 or age >= 60):
            print("Ticket price is $12")
    else:
            print("Tickit price is $20")
else:
        print("You're not eligible to buy a ticket.")
