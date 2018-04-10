
def print_something(name,age):
    print("my name is" + name + "and my age is" + str(age))
    print("My name is", name, "and my age is", age)
print_something("Sunil",27)



def print_something(name = "python", age = "unknown"):
    print("My name is", name, "and my age is", age)
print_something("Sunil")


def print_something(name = "python", age = "unknown"):
    print("My name is", name, "and my age is", age)
print_something()

#Key word arguements
def print_something(name = "python", age = "unknown"):
    print("My name is", name, "and my age is", age)
print_something(age = 27, name = "sunil")
print_something(age = 27)

#Infinite arguements
def print_people(*people):
    for person in people:
        print("This person is", person)
print_people("King","Queen","Minister","Soldier")


#Return values from function
def do_math(num1,num2):
    return num1 + num2

math1 = do_math(10,20)
math2 = do_math(30,40)

print("First sum is",math1, "second sum is", math2)