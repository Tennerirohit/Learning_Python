#1. Finding sum of all elements in a given list of numbers
#Sample Input : [10,20,30,40,50]
#Sample Output : 150
 
'''l=[10,20,30,40,50]
sum=0
for i in l:
    sum=sum+i
    
print(sum)
'''
#2. Finding the maximum and minimum values in the list 
#Sample Input : [15,2,7,25,10]
#Sample Output : 150

'''l=[15,2,7,25,10]
l.sort()
print("Maximum : ",l[-1])
print("Minimum : ",l[0])'''

#3. Remove duplicate elements from a list to create a new list with unique element
#Sample Input : [10,20,30,20,40,10,50]
#Sample Output : [10,20,30,40,50]

'''l=[10,20,30,20,40,10,50]
a=set(l)
b=list(a)
b.sort()
print(b)'''


#4. Count the number of occurrences of a specific element in a list.
#Sample Input : [1,2,3,2,1,4,2,5] 2
#Sample Output : Count of 2 =3

'''inp=input("Enter the list :").split(",")
n=int(input("Enter the number : "))
l=[int(item) for item in inp]
count =0 
for i in l :
    if i==n :
        count=count+1
print(count)
'''
#4. Given two sets,find their intersection(common elements) and union (all unique elements combined).
#Sample Input : set A :{1,2,3,4,5}  set B :{4,5,6,7,8,9}
#Sample Output : Intersection : {4,5}   Union : {1,2,3,4,5,6,7,8,9}

A ={1,2,3,4,5}
B ={4,5,6,7,8,9}
print(A.intersection(B))
print(A.union(B))




