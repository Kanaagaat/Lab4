#regular polygon.
import math
ns = int(input("Input number of sides: "))
ln = int(input("Input the length of a side: "))
pi = math.pi

tg = math.tan(pi/ns)
ans = round((ln**2 * ns)/(4*tg))

print(f"The area of the polygon is: {ans}")