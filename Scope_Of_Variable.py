#Scope of variable
'''The location where we can find a variable and also access it if required is called the scope of a variable.'''

#Python Local scope
'''Local variables are those that are initialized within a function and are unique to that function. 
   It cannot be accessed outside of the function. Let's look at how to make a local variable.'''

'''def f():
    
    # local variable
    s = "I love coding"
    print("Inside Function:", s)

# Driver code
f()
print(s) #It cannot be accessed because it is defined inside the function so it is a local scope variable'''

#Python Global variables
'''Global variables are the ones that are defined and declared outside any function 
   and are not specified to any function. They can be used by any part of the program.'''

# This function uses global variable s
'''def f():
    print(s)


# Global scope
s = "I love My life"
f()'''

#Global and Local Variables with the Same Name
'''Now suppose a variable with the same name is defined inside the scope of the function as well then 
   it will print the value given inside the function only and not the global value.'''
# This function has a variable with
# name same as s.
def f():
    s = "Me too."
    print(s)

# Global scope
s = "I love Coding"
f()
print(s)