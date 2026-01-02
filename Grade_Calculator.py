#Grade Calculator
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