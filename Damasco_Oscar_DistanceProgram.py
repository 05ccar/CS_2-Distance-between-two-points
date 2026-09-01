import math  
    
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

    
distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

    
print(f"\nThe distance between the two points is: {distance:.2f}")


#Reflection
# A library is more practical than doing it from scratch because its faster
# while from scratch can take up time. Also, if you do it from scratch
# you may make mistakes while a library can do little to no mistakes. 