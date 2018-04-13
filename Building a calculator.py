#1
def add(x,y):
    "This function adds two numbers"
    return x+y
def subtract(x,y):
    "This function subtract two numbers"
    return x-y
def multiply(x,y):
    "This function multiply two numbers"
    return x*y
def divide(x,y):
    "This function divides two numbers"
    return x/y
#Take input from the user
print("select option:")
print("1.Addition")
print("2.subtract")
print("3.multiply")
print("4.divide")

choice=input("Enter choice 1/2/3/4:")

num1=int(input("First number:"))
num2=int(input("Second number:"))

if choice=='1':
    print(num1,"+",num2,"=",add(num1,num2))

elif choice=='2':
    print(num1,"-",num2,"=",subtract(num1,num2))

elif choice=='3':
    print(num1,"*",num2,"=",multiply(num1,num2))

elif choice=='4':
    print(num1,"/",num2,"=",divide(num1,num2))

else:
    print("print unknown")




