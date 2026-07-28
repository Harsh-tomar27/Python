# Variables:-Its a containers that stored dataType storage location
# Name of variable is called Identifiers
name="Harsh"
age=21
pi=3.14
print(name,age,pi)
print(type(name)) # type function is use to known the datatype of variable

#Type conversion :- is the process of changing a value from one data type to another

# Implicit Type Conversion (Automatic)
# Performed automatically by the programming language.
# Usually happens when converting from a smaller or compatible type to a larger type.

# Explicit Type Conversion (Type Casting)
# Performed manually by the programmer.
# Used when automatic conversion is not possible or when you want to force a conversion.

#print(f"Hello {name},you are {age} years old!")

# Take two numbers as input from the user and print their product, and quotient sum, difference
Num1=int(input("enter first Number"))
Num2=int(input("enter Second Number"))
sum=Num1+Num2
product=Num1*Num2
difference=Num1-Num2
quotient=Num1%Num2
print(sum , product ,difference , quotient)

#Ask the user to enter two integers and one float. Convert them all to floats and print their average
num1= int(input("enter num1: "))
num2= int(input("enter num2: "))
num3= float(input("enter num3: "))
# Convert them all to floats
num1=float(num1)
num2=float(num2)
avg=(num1+num2+num3)/3
print(avg)

# '''Python follows the order of operations (operator precedence):
# ** (Exponent)
# *, /, //, % (Multiplication, Division, etc.)
# +, - (Addition, Subtraction)'''

#swap two no                    # using third variables temp=x,x=y,y=temp
x=6
y=9
print(x,y)
x,y=y,x
print("x:",x,"y:",y)

# Take the radius ( ) as user input and print the area
r=int(input("enter radius"))
area_OF_circle= 3.14*r*r
print("area of circle is: ",area_OF_circle)