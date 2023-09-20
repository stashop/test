num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator (+ - * /): ")

match op:
 case "+":
    print(num1 + num2)
 case "-":
    print(num1 - num2)
 case "*":
    print(num1 * num2)
 case "/":
    print(num1 / num2)
 case default:
    print("Invalid operator")