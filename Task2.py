# Simple calculator using Python
print("Select an operation to perform:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")


operation = input()
# Addition
if operation == "1":
    num1 = input("Enter first number:")
    num2 = input("Enter second number:")
    print("The sum is " + str(int(num1) + int(num2)))
# subtraction    
elif operation == "2":
    num1 = input("Enter first number:")
    num2 = input("Enter second number:")
    print("The difference is " + str(int(num1) - int(num2)))
 # Multiplication   
elif operation == "3":
    num1 = input("Enter first number:")
    num2 = input("Enter second number:")
    print("The product is " + str(int(num1) * int(num2)))
  # Division  
elif operation == "4":
    num1 = input("Enter first number:")
    num2 = input("Enter second number:")
    print("The result is " + str(int(num1) / int(num2)))
    
else:
    print("Invalid Entry")
