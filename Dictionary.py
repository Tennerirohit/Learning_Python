#Python Dictionary

'''Python dictionary is a data structure that stores the value in key: value pairs. Values in a dictionary can be of any data type and can be duplicated, whereas keys can't be repeated and must be immutable.

.Keys are case sensitive which means same name but different cases of Key will be treated distinctly.
.Keys must be immutable which means keys can be strings, numbers or tuples but not lists.
.Duplicate keys are not allowed and any duplicate key will overwrite the previous value.
.Internally uses hashing. Hence, operations like search, insert, delete can be performed in Constant Time.
.From Python 3.7 Version onward, Python dictionary are Ordered.
'''
#How to Create a Dictionary
'''Dictionary can be created by placing a sequence of elements within curly {} braces, separated by a 'comma'.'''
'''d1 = {1: 'Tenneri', 2: 'Rohit', 3: 'Naidu'}
print(d1)

# create dictionary using dict() constructor
d2 = dict(a = "Tenneri", b = "Rohit", c = "Naidu")
print(d2)'''

#Accessing Dictionary Items
'''We can access a value from a dictionary by using the key within square brackets or get() method.'''

'''d = { "name": "Prajjwal", 1: "Python", (1, 2): [1,2,4] }

# Access using key
print(d["name"])

# Access using get()
print(d.get("name"))'''

#Adding and Updating Dictionary Items

'''
d = {1: 'Tenneri', 2: 'Rohit', 3: 'Naidu'}

# Adding a new key-value pair
d["age"] = 22

# Updating an existing value
d[1] = "Python dict"

print(d)
'''
#Removing Dictionary Items
'''
We can remove items from dictionary using the following methods:

. del: Removes an item by key.
. pop(): Removes an item by key and returns its value.
. clear(): Empties the dictionary.
. popitem(): Removes and returns the last key-value pair.
'''
'''d = {1: 'Tenneri', 2: 'Rohit', 3: 'Naidu', 'age':22}

# Using del to remove an item
del d["age"]
print(d)

# Using pop() to remove an item and return the value
val = d.pop(1)
print(val)

# Using popitem to removes and returns
# the last key-value pair.
key, val = d.popitem()
print(f"Key: {key}, Value: {val}")

# Clear all items from the dictionary
d.clear()
print(d)'''

#Iterating Through a Dictionary
'''We can iterate over keys [using keys() method] , 
   values [using values() method] or both [using item() method] with a for loop.'''

d = {1: 'Tenneri', 2: 'Rohit', 'age':22}

# Iterate over keys
for key in d:
    print(key)

# Iterate over values
for value in d.values():
    print(value)

# Iterate over key-value pairs
for key, value in d.items():
    print(f"{key}: {value}")
