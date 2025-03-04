def calculator():
    num1 = float(input("Enter The First Number:"))
    num2 = float(input("Enter The Second Number:"))
    operator = input("Enter an operator(+,-,*,/,%):")
    if operator == "+":
       Answer = num1 + num2
    elif operator == "-":
        Answer = num1 - num2
    elif operator == "*":
        Answer = num1 * num2
    elif operator == "/":
        Answer = num1 / num2
    elif operator == "%":
        Answer = num1 % num2
    else:
        return "InValid Operator "
    return f"The Answer Of Operation Is:{Answer}"
print(calculator())
