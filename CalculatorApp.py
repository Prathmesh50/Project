HISTORY_FILE = "history.txt"

def show_history():
    try:
        # Fixed 'readLines' to 'readlines'
        file = open(HISTORY_FILE, 'r')
        lines = file.readlines()
        
        if len(lines) == 0:
            print("No history found!")
        else:
            # Removed '.string()' as lists don't have that attribute
            for line in reversed(lines):
                print(line.strip())
        file.close()
    except FileNotFoundError:
        print("No history file exists yet.")

def clear_history():
    file = open(HISTORY_FILE, 'w')
    file.close()
    print('History cleared.')

# Fixed parameter name from 'equaLion' to 'equation' to match line 20
def save_to_history(equation, result):
    file = open(HISTORY_FILE, 'a')
    file.write(equation + " = " + str(result) + "\n")
    file.close()

def calculator(user_input):
    parts = user_input.split()
    
    # Added check to prevent IndexError if input is too short
    if len(parts) < 3:
        print("Invalid input. Use format: number operator number (e.g., 8 + 8)")
        return

    try:
        num1 = float(parts[0])
        op = parts[1]
        num2 = float(parts[2])
    except ValueError:
        print("Invalid input. Please enter numbers.")
        return

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("Cannot divide by zero")
            return
        result = num1 / num2
    else:
        print("Invalid operator. Use ONLY +, -, *, /")
        return

    # Check if result is a whole number to print as integer
    if result == int(result):
        result = int(result)
        
    print(f"Result: {result}")
    save_to_history(user_input, result)

def main():
    print("--- SIMPLE CALCULATOR (type history, clear or exit) ---")
    while True:
        user_input = input("Enter calculation (+ - * /) or command (history, clear or exit): ").lower().strip()
        
        if user_input == "exit":
            print("Goodbye!")
            break
        elif user_input == "history":
            show_history()
        elif user_input == "clear":
            clear_history()
        else:
            calculator(user_input)

if __name__ == "__main__":
    main()