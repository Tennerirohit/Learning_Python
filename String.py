'''Strings is the data type that is used to represent texted data . 
    String Indexing :- Strings are ordered sequence and you can access individual characters using indexing .Python uses zero based indexing ,where the first character has an index of zero 
    String Slicing :- Slicing is a way to extract a portion of a string by specifying the start and end indexes. The syntax for slicing is string[start:end], where start starting index and end is stopping index (excluded).
    String Iteration :- Strings are iterable; you can loop through characters one by one.
    String Immutability :- Strings are immutable, which means that they cannot be changed after they are created. If we need to manipulate strings then we can use methods like concatenation, slicing or formatting to create new strings based on original.
    Deleting a String :- In Python, it is not possible to delete individual characters from a string since strings are immutable. However, we can delete an entire string variable using the del keyword.
    Updating a String :- As strings are immutable, “updates” create new strings using slicing or methods such as replace().
    '''

#Creating a String
'''s1 = 'GfG'  # single quote
s2 = "GfG"  # double quote
print(s1)
print(s2)'''

#Accessing characters in String

'''s = "Tenneri rohit"
print(s[0])   # first character
print(s[4])   # 5th character'''

'''s = "Tenneri rohit"
print(s[-10])   # 3rd character
print(s[-5])    # 5th character from end'''

#String Slicing

'''s = "Tennerirohit"
print(s[1:4])    # characters from index 1 to 3
print(s[:3])     # from start to index 2
print(s[3:])     # from index 3 to end
print(s[::-1])   # reverse string'''

#String Iteration

'''n = "Tennerirohit"
for l in n:
    print(l)'''

#String Immutability
'''s = "tennerirohit"
s = "T" + s[1:]   # create new string #using both string concatination and string slicing
print(s)'''

#Deleting a String

'''s = "GfG"
del s'''

#Updating a String

'''s = "hello geeks"
s1 = "H" + s[1:]                   # update first character
s2 = s.replace("geeks", "GeeksforGeeks")  # replace word
print(s1)
print(s2)'''

#Common String Methods

'''1. len(): The len() function returns the total number of characters in a string (including spaces and punctuation).'''

'''s = "Tennerirohit"
print(len(s))'''

'''2. upper() and lower(): upper() method converts all characters to uppercase whereas, lower() method converts all characters to lowercase.'''

'''s = "Hello World"
print(s.upper())
print(s.lower())'''

'''3. strip() and replace(): strip() removes leading and trailing whitespace from the string and replace() replaces all occurrences of a specified substring with another.'''

'''s = "   Gfg   "
print(s.strip())    

r = "Python is fun"
print(r.replace("fun", "awesome"))'''

#Concatenating and Repeating Strings
'''We can concatenate strings using + operator and repeat them using * operator.'''

'''s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)

s = "Hello "
print(s * 30)
'''

#Formatting Strings
'''Python provides several ways to include variables inside strings.'''

#1. Using f-strings

'''name = "Alice"
age = 22
print(f"Name: {name}, Age: {age}")'''

#2. Using format()
'''s = "My name is {} and I am {} years old.".format("Alice", 22)
print(s)'''

#String Membership Testing
'''in keyword checks if a particular substring is present in a string.'''

s = "Tennerirohit"
print("rohit" in s)
print("GfG" in s)
