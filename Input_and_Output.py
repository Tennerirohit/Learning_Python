''' Input:- The input() function is used to take input from the user via keyboard during the program's execution
    Output:- The print statement is used to display output to the console or the terminal. It allows you to show information'''

'''a=input("Enter the input : ") #Taking the input value
print(a) #Printing the input that we have given '''

'''1.Output Should be 
    Enter your name : Rohit
    Enter your age : 23 
    Hello , Rohit ! You are 23 years old .'''

''' solution :-
name=input("Enter your name : ")
age=int(input("Enter your age : "))
print(f"Hello , {name} ! You are {age} years old .")'''

'''2. Using sep between output '''

'''a=int(input("Enter your number : "))
b=int(input("Enter your number : "))
print(a,b,sep="Hello world")'''

'''3. Using end in the output'''

a=int(input("Enter your number : "))
b=int(input("Enter your number : "))
print(a,b,sep=",",end=" Hello sentence is ended")