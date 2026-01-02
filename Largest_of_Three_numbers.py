#Largest of three numbers 
'''Write a program that takes three numbers as input and finds the largest among using decision-making statements. '''

#Sample input :- Enter three numbers : 15,8,21
#Sample output :- Largest number is :21
 
a=int(input("Enter the digit : "))
b=int(input("Enter the digit : "))
c=int(input("Enter the digit : "))
if a>=b :
    if a>=c :
        print("Largest number is :",a)
    else :
        print("Largest number is :",c)
elif a>=c :
    if a>=b :
        print("Largest number is :",a)
    else :
        print("Largest number is :",b)
elif b>=a :
    if b>=c :
        print("Largest number is :",b)
    else :
        print("Largest number is :",c)
elif b>=c :
    if b>=a :
        print("Largest number is :",b)
    else :
        print("Largest number is :",a)
elif c>=a :
    if c>=b :
        print("Largest number is :",c)
    else :
        print("Largest number is :",b)
elif c>=b :
    if c>=a :
        print("Largest number is :",c)
    else :
        print("Largest number is :",a)
else :
    print("Invalid")