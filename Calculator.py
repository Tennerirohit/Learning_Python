a= float(input("Enter the digit : "))
b= float(input("Enter the digit : "))
operator= input("Enter the Operator : ")
if operator == "+" :
    print("The addition value : ",a+b)
elif operator =="-":
    print("The subtracted value : ",a-b)
elif operator =="/":
    print("The Divided value : ",a/b)
elif operator =="-":
    print("The Multiplied value : ",a*b)
elif operator =="-":
    print("The Modular division value : ",a%b)
else :
    print("Invalid operator ,Enter the operator again")