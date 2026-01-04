#Solving Quadratic Equations
#Sample input :- a=1,b=-3,c=2
#Sample output :- Roots:(2.0,1.0)

a=int(input("Enter the value of a : "))
b=int(input("Enter the value of b : "))
c=int(input("Enter the value of c : "))
def equation(a,b,c):
    d=b**2-4*a*c
    e1=(-b+d**-2)/2*a
    e2=(-b-d**-2)/2*a
    print(f"Roots : ({e1},{e2})")
    return print
roots=equation(a,b,c)
