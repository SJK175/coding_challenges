#basic calculator that gives sum of two numbers :
n1 = input("first number : ")
n2 = input("second number : ")
result = float(n1) + float(n2)
print("your result is : " + str(result))

# provide me the radius of a circle & I'll give you the area
rad = input("what is the radius of the circle (in cm) : ")
import math 
pi = math.pi
area = pi * float(rad)**2
print("area of the circle is aprox : " + str(round(area)) + " cm square")
