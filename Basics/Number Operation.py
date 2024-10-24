def num_operation(num1,num2,operation):
    if operation == "+":
          return num1 + num2
    elif operation == "-":
          return num1 - num2
    elif operation == "*":
          return num1 * num2
    elif operation == "/":
          return num1 / num2
    else:
          return "Invalid operation"

num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
operation = input("Enter the operation to be Execution:")
print("result:",num_operation(num1,num2,operation))