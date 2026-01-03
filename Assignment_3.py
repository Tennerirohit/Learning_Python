#Problems on Loops,strings,numbers,decision making

'''1 Print natural numbers from 1 to n '''

#sample Input : N=5
#Sample output : 1 ,2,3,4,5

'''n=int(input("Enter the digit : "))
for i in range (1,n+1):
    print(i)'''

'''n=int(input("Enter the digit : "))
i=1
while (i<=n) :
    print(i)
    i+=1'''

'''2 Sum of N natural numbers'''

'''n=int(input("Enter the digit : "))
i=1
sum=0
while (i<=n) :
    sum=i + sum
    i+=1
print(sum)    '''

'''3. Print even numbers from 1 to n'''

'''n=int(input("Enter the digit : "))
for i in range (2,n+1,2) :
    print(i)'''

'''4. Print odd numbers from 1 to n'''

'''n=int(input("Enter the digit : "))
for i in range (1,n+1,2) :
    print(i)'''

'''5. Calculate the factorial of the number '''

n=int(input("Enter the digit : "))
fact=1
while n>0:
    fact=fact*n
    n-=1
print(fact)
