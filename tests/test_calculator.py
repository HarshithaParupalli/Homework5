import pytest
from app import App

# Initialize the App instance
app = App()

def test_add():
    output = app.command_handler.execute_command("5", "3", "add")
    assert output == "The result of 5 add 3 is equal to 8"

def test_subtract():
    output = app.command_handler.execute_command("10", "2", "subtract")
    assert output == "The result of 10 subtract 2 is equal to 8"

def test_multiply():
    output = app.command_handler.execute_command("4", "5", "multiply")
    assert output == "The result of 4 multiply 5 is equal to 20"

def test_divide():
    output = app.command_handler.execute_command("20", "4", "divide")
    assert output == "The result of 20 divide 4 is equal to 5"

def test_divide_by_zero():
    output = app.command_handler.execute_command("1", "0", "divide")
    assert output == "An error occurred: Cannot divide by zero"

def test_unknown_operation():
    output = app.command_handler.execute_command("9", "3", "unknown")
    assert output == "Unknown operation: unknown"

def test_invalid_input_a():
    # Since the execute_command method doesn't handle invalid input directly,
    # you may want to capture the output and assert it here.
    output = app.command_handler.execute_command("a", "3", "add")
    assert output == "Invalid number input: a or 3 is not a valid number."

def test_invalid_input_b():
    output = app.command_handler.execute_command("5", "b", "subtract")
    assert output == "Invalid number input: 5 or b is not a valid number."

# Direct use of fake_records fixture
def test_generated_operations(fake_records):
    for a, b, operation in fake_records:
        expected_result = None
        if operation == 'add':
            expected_result = f"The result of {a} add {b} is equal to {a + b}"
        elif operation == 'subtract':
            expected_result = f"The result of {a} subtract {b} is equal to {a - b}"
        elif operation == 'multiply':
            expected_result = f"The result of {a} multiply {b} is equal to {a * b}"
        elif operation == 'divide':
            if b == 0:
                expected_result = "An error occurred: Cannot divide by zero"
            else:
                expected_result = f"The result of {a} divide {b} is equal to {int(a / b)}"

        output = app.command_handler.execute_command(str(a), str(b), operation)
        assert output == expected_result
