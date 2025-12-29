#1. String input and output 
# as Hello,Rohit !

'''a=input("Enter the string value : ")
print (type(a))
print ("Hello",a,end=" !")
'''
#2 Integer input and output 
# Expected input : 5 
# Expected Output : "You Entered : 5"
'''
a=int(input("Enter the integer : "))
print("You Entered : ",a)
'''

#3 Float input and output
# Expected input : 3.14
# Expected Output : "Value of pi : 3.14"

'''a=float(input("Enter the Value : "))
print("Value of pi : ",a)'''

#4 Taking multiple inputs in a single line
# Expected input : 10 20 30
# Expected Output : "Sum of inputs : 60"

'''a=input("Enter the Values : ")
x,y,z=a.split(" ")
d=int(x)+int(y)+int(z)
print(d)'''

#5 Specifying Separator in the output
# Expected input : "John",25
# Expected Output : "Name : John, Age:25"

'''a=input("Enter your name and age : ")
name,age=a.split(",")
print(f"Name : {name}, Age: {age}")'''

#6 Arithematic Operators
# Expected input : 10,5
# Expected Output : Addition: 15,Subtraction:5,Multiplication:50,Division:2.0

'''a=int(input("Enter the integer : "))
b=int(input("Enter the integer : "))
print("Addition : ",a+b)
print("Subtraction : ",a-b)
print("Multiplication : ",a*b)
print("Division : ",a/b)'''

#7 Comparision Operators
# Expected input : 10,5
# Expected Output : 10>5:True,10<5:False,10==5:False,10!=5:True

'''a=int(input("Enter the integer : "))
b=int(input("Enter the integer : "))
print(f"{a}>{b} ",a>b)
print(f"{a}<{b} ",a<b)
print(f"{a}=={b} ",a==b)
print(f"{a}!={b} ",a!=b)'''

#8 Finding Area of a circle
# Expected input : radius =5
# Expected Output : Area of the circle :78.53981633974483

'''r=float(input("Enter the integer : "))
print("Area of the circle : ",3.14*r*r) '''

#9 Swapping of two numbers
# Expected input : a=10 , b=20
# Expected Output : a=20 , b=10

'''a=int(input("Enter the integer : "))
b=int(input("Enter the integer : "))
a,b=b,a
print(a,b)'''

#9 Converting Temperature Units
# Expected input : temperature_celsius = 30
# Expected Output : temperature_Fahrenheit = 86.0 , temperature_Kelvin = 303.15

c=int(input("Enter the temperature : "))
print("Temperature in Fahrenheit : ",(c*9/5)+32)
print("Temperature in Kelvin : ",c+273.15)