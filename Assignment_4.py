#Problems on functions

#1. Finding the sums of two Numbers 
#sample input :- num1=5,num2=10
#sample Output :- sum=15

'''num1=int(input("Enter the number : "))
num2=int(input("Enter the number : "))
def sum(num1,num2):
    r=num1+num2
    return (r)
p= sum(num1,num2)
print(p)'''

#2. Finding the area of a circle
#Sample input :- radius=5
#Sample output :- Area of the circle : 78.5

'''r=int(input("Enter the radius of the circle : "))
def area(r):
    area=3.14*r**2
    return(area)
print(area(r))'''

#3. Solving Quadratic Equations
#Sample input :- a=1,b=-3,c=2
#Sample output :- Roots:(2.0,1.0)

'''a=int(input("Enter the value of a : "))
b=int(input("Enter the value of b : "))
c=int(input("Enter the value of c : "))
def equation(a,b,c):
    d=b**2-4*a*c
    e1=(-b+d**-2)/2*a
    e2=(-b-d**-2)/2*a
    print(f"Roots : ({e1},{e2})")
    return print
roots=equation(a,b,c)'''

#4. Temperature Converter
'''Build a temperature converter program that allows the user to convert temperatures between celsius,kelvin and fahrenheit'''
 #Sample input :- Enter the temperature : 30, Enter the Units(K or F or C) : c
 #Sample output :- Temperature in Fahrenheit : 89.6F, Temperature in Kelvin : 305k

a=int(input("Enter the temperature : "))
u=input("Enter the operator : ")
s=u.lower()
def temp(a,S):
    if s =="c":
        print("Temperature in Fahrenheit : ",(a*9/5)+32)
        print("Temperature in Kelvin : ",a+273.15)
    elif s =="f":
        print("Temperature in Celsius : ",(a - 32) * 5/9)
        print("Temperature in Kelvin : ",(a-32)*5/9+273.15)
    elif s =="k":
        print("Temperature in Celsius : ",a-273.15)
        print("Temperature in Fahrenheit : ",(a-273.15)* 9/5 + 32)
    else :
        print("Invalid operator")
    return print
temperature=temp(a,s)
