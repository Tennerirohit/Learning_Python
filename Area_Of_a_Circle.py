#Finding the area of a circle
#Sample input :- radius=5
#Sample output :- Area of the circle : 78.5

r=int(input("Enter the radius of the circle : "))
def area(r):
    area=3.14*r**2
    return(area)
print(area(r))