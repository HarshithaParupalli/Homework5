import os
import logging
from dotenv import load_dotenv
from app import App


# Load environment variables from .env file
load_dotenv()

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Access environment variable (e.g., to identify the environment the app is running in)
environment = os.getenv('ENVIRONMENT', 'development')  # Default to 'development' if ENVIRONMENT is not set

logging.info(f"Starting application in {environment} environment")

if __name__ == '__main__':
    try:
        # Initialize and start the app
        app = App()
        app.start()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
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