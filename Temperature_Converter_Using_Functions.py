#Temperature Converter
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