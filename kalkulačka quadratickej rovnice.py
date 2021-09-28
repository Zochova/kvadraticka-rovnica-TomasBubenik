import math
#Kvadratická rovnica = a*x+b*x+c = 0
#D = b2 - 4*a*c
a = int(input("Zadajte premmenú a:"))
b = int(input("Zadajte premmenú b:"))
c = int(input("Zadajte premmenú c:"))

D = b**2-4*a*c 
x1 = (-b + math.sqrt(D))/2
x2 = (-b -math.sqrt(D))/2

print (x1)
print (x2)

