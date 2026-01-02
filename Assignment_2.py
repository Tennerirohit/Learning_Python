#Problems on Strings ,Numbers and Decision Making

#1Vowel Counter 
'''Write a program that takes a string input from the user and 
counts the number of vowels(A,E,I,O,U, and their lowercase equivalents) in the string '''
#Sample input :- "Hello,World!"
#Sample Output :- Number of vowels :3

'''s=input("Enter the string : ")
s1=s.lower()
a=s1.count('a')
e=s1.count('e')
i=s1.count('i')
o=s1.count('o')
u=s1.count('u')
print("Number of vowels :",a+e+i+o+u)'''

#2Grade Calculator
'''Create a program that takes the marks of a student in different subjects as input . Calculate the total marks and average
   and display the corresponding grade based on the average'''
#Sample input :- Marks in Math:85, Marks in Science : 90, Marks in English :78
#Sample Output :- Total marks :253 , Average Marks : 84.33,Grade : A

'''m=int(input("Enter the Marks in Math : "))
s=int(input("Enter the Marks in Science : "))
e=int(input("Enter the Marks in English : "))
print("Total marks : ",m+s+e)
print("Average marks : ",(m+s+e)/3)
if (m+s+e)/3>=85 :
    print("Grade : A+")
elif (m+s+e)/3>=80 :
    print("Grade : A")
elif (m+s+e)/3>=75 :
    print("Grade : B+")
elif (m+s+e)/3>=70 :
    print("Grade : B")
elif (m+s+e)/3>=65 :
    print("Grade : C+")
elif (m+s+e)/3>=60 :
    print("Grade : c")
else :
    print("Grade : Fail")

'''
#3 Palindrome checker
'''Write a program that takes a string input from the user and checks if it is a palindrome or not 
   A Palindrome is a word,phrase,number, or sequence of characters that reads the same backward as forward '''
#Sample Input :- radar
#Sample Output :- It is palindrome.


'''a=input("Enter the string : ")
if a==a[::-1] :
    print ("It is a palindrome ")
else :
    print("It is not palindrome ")
'''
#4 Largest of three numbers 
'''Write a program that takes three numbers as input and finds the largest among using decision-making statements. '''

#Sample input :- Enter three numbers : 15,8,21
#Sample output :- Largest number is :21

s=input("Enter the three digits with \", \"in betweeen  : ")
x,y,z=s.split(",")
a=int(x)
b=int(y)
c=int(z)
if a>=b :
    if a>=c :
        print("Largest number is :",a)
    else :
        print("Largest number is :",c)
elif a>=c :
    if a>=b :
        print("Largest number is :",a)
    else :
        print("Largest number is :",b)
elif b>=a :
    if b>=c :
        print("Largest number is :",b)
    else :
        print("Largest number is :",c)
elif b>=c :
    if b>=a :
        print("Largest number is :",b)
    else :
        print("Largest number is :",a)
elif c>=a :
    if c>=b :
        print("Largest number is :",c)
    else :
        print("Largest number is :",b)
elif c>=b :
    if c>=a :
        print("Largest number is :",c)
    else :
        print("Largest number is :",a)
else :
    print("Invalid")