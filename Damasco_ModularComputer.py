
def add_numbers(num1, num2):
   return num1 + num2


def subtract_numbers(num1, num2):
    return num1 - num2


def multiply_numbers(num1, num2):
    return num1 * num2


def divide_numbers(num1, num2):
    return num1 / num2



num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


print("\nChoose operation:")
print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")

choice = input("\nEnter choice: ")


if choice == "1":
    result = add_numbers(num1, num2)
    print("Result:", result)

elif choice == "2":
    result = subtract_numbers(num1, num2)
    print("Result:", result)

elif choice == "3":
    result = multiply_numbers(num1, num2)
    print("Result:", result)

elif choice == "4":
    if num2 == 0:
        print("Cannot divide by zero.")
    else:
        result = divide_numbers(num1, num2)
        print("Result:", result)

else:
    print("Invalid choice.")
# Reflection
# I created four functions: add_numbers(), subtract_numbers(), multiply_numbers(), and divide_numbers().
# Each function uses two parameters: num1 and num2.
# The arguments passed were the two numbers entered by the user, stored in the variables num1 and num2.
# The returned value was stored in the result variable and then displayed to the user.
# Using functions makes the program easier to read, understand, test, and maintain. Each function has one specific use and the functions 
#can be reused if needed
