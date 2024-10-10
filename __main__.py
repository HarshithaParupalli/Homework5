from app import App

if __name__ == '__main__':
    app = App()
    app.start()

'''
import sys
from app.calculator import calculate

def main():
    # Check if the script is run with the correct number of command-line arguments
    if len(sys.argv) != 4:
        print("Error: Please provide exactly three inputs: a b operation.")
        sys.exit(1)  # Exit the program with an error status

    # Assign command-line arguments to variables
    a = sys.argv[1]
    b = sys.argv[2]
    operation = sys.argv[3]

    try:
        result = calculate(a, b, operation)
        print(result)  # Print the result of the calculation
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
'''