'''Loops :- are used to execute a block of code repeatdedly as long as a certain condition is true 
    or for a specific number of iterations
    Types :- 1. While:- In Python, a while loop is used to execute a block of statements repeatedly until a given condition is satisfied. 
                        When the condition becomes false, the line immediately after the loop in the program is executed.
             
             2. For :- For loops is used to iterate over a sequence such as a list, tuple, string or range. 
                       It allow to execute a block of code repeatedly, once for each item in the sequence.
            
             3. Nested Loops :- Python programming language allows to use one loop inside another loop which is called nested loop. 

             _______Loop Control Statements________
             
             Loop control statements change execution from their normal sequence. When execution leaves a scope, 
             all automatic objects that were created in that scope are destroyed. Python supports the following control statements. 

            1. Continue Statement :- The continue statement in Python returns the control to the beginning of the loop.
            2. Break Statement :- The break statement in Python brings control out of the loop.
            3. Pass Statement :- We use pass statement in Python to write empty loops. Pass is also used for empty control statements, functions and classes.
'''
#For Loop

'''n = 4
for i in range(0, n):
    print(i)'''

#While Loop

'''cnt = 0
while (cnt < 3):
    cnt = cnt + 1
    print("Hello Rohit")'''

#Nested Loops

'''for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()'''


#Loop Control Statements

#Continue Statement

'''for letter in 'Tennerirohit':
    if letter == 'n' or letter == 'i':
        continue
    print('Current Letter :', letter)'''

#Break Statement

for letter in 'geeksforgeeks':
    if letter == 'r' or letter == 's':
        break

print('Current Letter :', letter)