'''The conditional statements are used in decision making 
The most common conditional statements used for decision making are :- 
 1. if :- If statement is the simplest form of a conditional statement. It executes a block of code if the given condition is true.
 2. if-else :- If Else allows us to specify a block of code that will execute if the condition(s) associated with an if or elif statement evaluates to False. Else block provides a way to handle all other cases that don't meet the specified conditions.
 3. if-elif-else :- elif statement in Python stands for "else if." It allows us to check multiple conditions, providing a way to execute different blocks of code based on which condition is true. Using elif statements makes our code more readable and efficient by eliminating the need for multiple nested if statements.
 4. Nested if..else :- Nested if..else means an if-else statement inside another if statement. We can use nested if statements to check conditions within conditions.
 5. Match-Case Statement :- match-case statement is Python's version of a switch-case found in other languages. It allows us to match a variable's value against a set of patterns.
 '''

#If Conditional Statement

'''age = 20
if age >= 18:
    print("Eligible to vote.")'''



#If else Conditional Statement
'''age = 10
if age <= 12:
    print("Travel for free.")
else:
    print("Pay for ticket.")'''

#elif Statement

'''age = int(input("Enter the age : "))

if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.")
else:
    print("Adult.")'''

#Nested if..else Conditional Statement

'''age = 70
is_member = True

if age >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")'''

#Match-Case Statement

number = int(input("Enter the number : "))

match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case _:
        print("Other number")