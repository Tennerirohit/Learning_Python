#Python Functions

'''Python Functions are a block of statements that does a specific task. 
The idea is to put some commonly or repeatedly done task together and make a function so that instead of writing the same code again 
and again for different inputs, we can do the function calls to reuse code contained in it over and over again.'''

#Defining a Function

'''We can define a function in Python, using the def keyword. A function might take input in the form of parameters.
   def fun():'''

#Calling a Function

'''After creating a function in Python we can call it by using the name of the functions followed by parenthesis 
   containing parameters of that particular function.'''

#Function Arguments

'''Arguments are the values passed inside the parenthesis of the function. 
   A function can have any number of arguments separated by a comma.

Syntax:

def function_name(parameters):
    """Docstring"""
    # body of the function
    return expression
    '''

#Types of Function Arguments

'''Python supports various types of arguments that can be passed at the time of the function call. 
   In Python, we have the following function argument types in Python, Let's explore them one by one.
   
   1. Default Arguments : A default argument is a parameter that assumes a default value if a value 
                          is not provided in the function call for that argument.
   2. Keyword Arguments : In keyword arguments, values are passed by explicitly specifying the parameter names, 
                          so the order doesnot matter.
   3. Positional Arguments : In positional arguments, values are assigned to parameters based on their order in the function call.
'''
#Function within Functions

'''A function defined inside another function is called an inner function (or nested function). 
   It can access variables from the enclosing functions scope and is often used to keep logic protected and organized.'''
#Return Statement in Function

'''The return statement ends a function and sends a value back to the caller. 
   It can return any data type, multiple values (packed into a tuple), or None if no value is given.

Syntax:

return [expression]'''

#Recursive Functions

'''A recursive function is a function that calls itself to solve a problem. 
   It is commonly used in mathematical and divide-and-conquer problems. Always include a base case to avoid infinite recursion.'''

#Defining a Function

'''def fun():
    print("Welcome to GFG")'''

#Calling a Function

'''def fun():
    print("Welcome to GFG")
    
fun() # Driver code to call a function'''

#Function Arguments

'''def evenOdd(x):
    if (x % 2 == 0):
        return "Even"
    else:
        return "Odd"

print(evenOdd(16))
print(evenOdd(7))'''

#Types of Function Arguments

#1. Default Arguments
'''def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)

myFun(10)'''

#2. Keyword Arguments
'''def student(fname, lname):
    print(fname, lname)

student(fname='Geeks', lname='Practice')
student(lname='Practice', fname='Geeks')
'''
#3. Positional Arguments
'''def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)

print("Case-1:")
nameAge("Suraj", 27)

print("\nCase-2:")
nameAge(27, "Suraj")
'''
#Function within Functions

'''def f1():
    s = 'I love GeeksforGeeks'
    def f2():
        print(s)
        
    f2()
f1()
'''
#Return Statement in Function
'''def square_value(num):
    """This function returns the square
    value of the entered number"""
    return num**2

print(square_value(2))
print(square_value(-4))
'''
#Recursive Functions

def factorial(n):
    if n == 0:  
        return 1
    else:
        return n * factorial(n - 1) 
      
print(factorial(4))