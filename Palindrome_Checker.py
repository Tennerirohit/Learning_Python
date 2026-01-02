#Palindrome checker
'''Write a program that takes a string input from the user and checks if it is a palindrome or not 
   A Palindrome is a word,phrase,number, or sequence of characters that reads the same backward as forward '''
#Sample Input :- radar
#Sample Output :- It is palindrome.


a=input("Enter the string : ")
if a==a[::-1] :
    print ("It is a palindrome ")
else :
    print("It is not palindrome ")