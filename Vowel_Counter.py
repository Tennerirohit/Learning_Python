#Vowel Counter 
'''Write a program that takes a string input from the user and 
counts the number of vowels(A,E,I,O,U, and their lowercase equivalents) in the string '''
#Sample input :- "Hello,World!"
#Sample Output :- Number of vowels :3

s=input("Enter the string : ")
s1=s.lower()
a=s1.count('a')
e=s1.count('e')
i=s1.count('i')
o=s1.count('o')
u=s1.count('u')
print("Number of vowels :",a+e+i+o+u)