print("welcome to the simple calculator")
num1 = input("Input first number: ")
operand = input("input operand (options are +, -, *, /, %, ^, or sqrt): ")
num2 = input("Input second number: ")

def calculator(arg1, op, arg2):
    ans = 0
    if op == "+":
        ans = float(arg1) + float(arg2)
        return ans
    elif op == "-":
        ans = float(arg1) - float(arg2)
        return ans
    elif op == "*":
        ans = float(arg1) * float(arg2)
        return ans
    elif op == "/":
        ans = float(arg1) / float(arg2)
        return ans
    elif op == "%":
        ans = float(arg1) % float(arg2)
        return ans
    elif op == "^":
        ans = pow(float(arg1),float(arg2))
        return ans
    elif op == "sqrt":
        ans = sqrt(float(arg1),float(arg2))
        return ans
    else:
        print("Operand not recognized")
        return "ERROR"

print(calculator(num1, operand, num2))