num1=input("Enter the first number:")
num2=input("Enter the second number:")
operator=input("Choose the operation (+, -, *, /):")

match operator:
    case "+":
        result=(float(num1) + float(num2))   
    case "-":
        result=(float(num1) - float(num2))
    case "*":
        result=(float(num1) * float(num2))
    case "/":
        if num2 == 0:
            print("Error: Division by zero")
            exit()
        result=(float(num1) / float(num2))

    case _:
        print("Invalid operator")

print(f"The result is {result}")
