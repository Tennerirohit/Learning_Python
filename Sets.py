#Sets in Python
'''A Set in Python is used to store a collection of items with the following properties.

. No duplicate elements. If try to insert the same item again, it overwrites previous one.
. An unordered collection. When we access all items, 
  they are accessed without any specific order and we cannot access items using indexes as we do in lists.
. Internally use hashing that makes set efficient for search, insert and delete operations. 
  It gives a major advantage over a list for problems with these operations.
. Mutable, meaning we can add or remove elements after their creation, 
  the individual elements within the set cannot be changed directly.'''

#Type Casting with Python Set method

'''# typecasting list to set
s = set(["a", "b", "c"])
print(s)

# Adding element to the set
s.add("d")
print(s)'''

#Check unique and  Immutable with Python Set

'''# a set cannot have duplicate values
s = {"Geeks", "for", "Geeks"}
print(s)

# values of a set cannot be changed
s[1] = "Hello"
print(s)'''

#Methods for Sets
#1. Adding elements to Sets

'''# Creating a Set
people = {"Jay", "Idrish", "Archi"}

print("People:", end = " ")
print(people)

# This will add Daxit in the set
people.add("Daxit")

# Adding elements to the set using iterator
for i in range(1, 6):
    people.add(i)

print("\nSet after adding element:", end = " ")
print(people)'''

#2. Union operation on Python Sets

'''people = {"Jay", "Idrish", "Archil"}
vampires = {"Karan", "Arjun"}
dracula = {"Deepanshu", "Raju"}

# Union using union() function
population = people.union(vampires)

print("Union using union() function")
print(population)

# Union using "|" operator
population = people|dracula
print("\nUnion using '|' operator")
print(population)'''

#3. Intersection operation on Python Sets

'''set1 = set()
set2 = set()

for i in range(5):
    set1.add(i)

for i in range(3,9):
    set2.add(i)

# Intersection using intersection() function
set3 = set1.intersection(set2)

print("Intersection using intersection() function")
print(set3)

# Intersection using "&" operator
set3 = set1 & set2
print("\nIntersection using '&' operator")
print(set3)'''

#4. Finding Differences of Sets in Python

'''set1 = set()
set2 = set()

for i in range(5):
    set1.add(i)

for i in range(3,9):
    set2.add(i)

# Difference of two sets using difference() function
set3 = set1.difference(set2)
print(" Difference of two sets using difference() function")
print(set3)

# Difference of two sets using '-' operator
set3 = set1 - set2
print("\nDifference of two sets using '-' operator")
print(set3)'''

#5. Clearing Python Sets

set1 = {1,2,3,4,5,6}
print("Initial set")
print(set1)

# This method will remove all the elements of the set
set1.clear()
print("\nSet after using clear() function")
print(set1)