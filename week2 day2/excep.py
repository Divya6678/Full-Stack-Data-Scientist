try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    result = num1 / num2
    print("Result:", result)

except :
    print("Error: Division by zero is not allowed!")


finally:
    print("Division")
