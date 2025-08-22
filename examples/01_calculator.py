# ===============================
# 🧮 SIMPLE CALCULATOR - PRACTICAL EXAMPLE
# ===============================

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide a by b"""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def power(a, b):
    """Calculate a raised to power b"""
    return a ** b

def calculator():
    """Main calculator function"""
    print("🧮 Simple Calculator")
    print("=" * 30)
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Exit")
    
    while True:
        try:
            choice = input("\nEnter your choice (1-6): ")
            
            if choice == '6':
                print("👋 Goodbye!")
                break
            
            if choice not in ['1', '2', '3', '4', '5']:
                print("❌ Invalid choice! Please enter 1-6.")
                continue
            
            # Get numbers from user
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            # Perform calculation based on choice
            if choice == '1':
                result = add(num1, num2)
                operation = "+"
            elif choice == '2':
                result = subtract(num1, num2)
                operation = "-"
            elif choice == '3':
                result = multiply(num1, num2)
                operation = "*"
            elif choice == '4':
                result = divide(num1, num2)
                operation = "/"
            elif choice == '5':
                result = power(num1, num2)
                operation = "**"
            
            print(f"✅ {num1} {operation} {num2} = {result}")
            
        except ValueError as e:
            print(f"❌ Error: {e}")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")

# Run the calculator
if __name__ == "__main__":
    calculator()
