#Positional Arguments

'''def add_numbers(a,b) :
    return a+b
r=add_numbers(2,3)
print(r)'''

#Keyword Argument 

'''def personal_info(name,age):
    print("Name",name)
    print("Age",age)
personal_info(age=23,name="Rohit")'''

#Default keyword

def greet_user(name,greeting="Hello"):
    return greeting + "," + name + "!"
greeting1=greet_user("Rohit")
greeting2=greet_user("Priya","Hi")
print(greeting1)
print(greeting2)