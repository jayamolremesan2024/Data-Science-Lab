import math
print("*************************************************")
print("JAYAMOL REMESAN")
print("--SJC22MCA-2031--")
print("--20MCA241--DATA SCIENCE LAB--")
print("**************************************************")
a = float(input("Enter coefficient 'a': "))
b = float(input("Enter coefficient 'b': "))
c = float(input("Enter coefficient 'c': "))

discriminant = b**2 - 4*a*c

if discriminant >= 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Root 1: {root1:.2f}")
    print(f"Root 2: {root2:.2f}")
else:
    print("No real roots")
