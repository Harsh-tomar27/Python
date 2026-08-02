# #In Python,conditional statements are used to make decisions based on whether a condition is True or False.

# # 1 if Statement
# #Executes a block of code if the condition is true.

age=int(input("Enter your age: "))
if age>=18:
    print("your You are eligible to vote.")

# # 2 if...else Statement
# #Executes one block if the condition is true, and another if it is false.
num=int(input("enter no: "))
if num % 2==0:
    print("number is Even",num)
else:
    print("number is odd ",num)

#if-elif-else:- when we have multiple conditions to check.
marks=85
if marks>=90:
    print("Grade A")
elif marks>=75:
    print("Grade B")
elif marks>=60:
    print("Grade c")
else:
    print("Fail")    

#Question:
a=int(input("enter first number"))
b=int(input("enter secoand number:"))

if a>b:
    print(a,"is largest")
else:
    print(b,"is largest")    

a=int(input("enter first number:"))
b=int(input("enter secoand number:"))
c=int(input("enter third  number:"))
if  a>=b and a>=c:
    print("A is largest",a)
elif b>=a and b>=c:
    print("B is largest",b)   
else:
    print("c is largest",c)     

#discount based on the bill amount
bill=float(input("enter bill amount:"))
if bill>=5000:
    discount=bill*0.20
elif bill>=3000:
    discount=bill=0.15
elif bill>=1000:
    discount=bill=0.10
else:
    discount=0

final_bill= bill-discount  
print("original bill",bill)            
print("discount: ",discount)            
print("final bill: ",final_bill)            

# leap year 
year = int(input("Enter year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")