'''The ASCII value of a character is the number the represents that character in yhe computer's memory 
    ord()
    chr()
    in python ,you can use the ord() function to find the ascii value of the character'''

char_a="A"
char_b="B"
ascii_value_a=ord(char_a)
ascii_value_b=ord(char_b)
print("ASCII Value of A is : ",ascii_value_a)
print("ASCII Value of B is : ",ascii_value_b)

ascii_value= 75
character=chr(ascii_value)
print("The character of the given ascii value is : ",character)