def calculator():
    print("🧮 Simple Calculator")
    
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("❌ Error: Division by zero is not allowed.")
                return
        else:
            print("❗ Invalid operator.")
            return

        print(f"✅ Result: {result}")

    except ValueError:
        print("❗ Please enter valid numbers.")

if __name__ == "__main__":
    calculator()

