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

m=int(input("Enter the Marks in Math : "))
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

