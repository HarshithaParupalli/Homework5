'''def calculate(a, b, operation):
    original_a = a
    original_b = b
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        return f"Invalid number input: {original_a} or {original_b} is not a valid number."


    try:
        if operation == 'add':
            result = a + b
        elif operation == 'subtract':
            result = a - b
        elif operation == 'multiply':
            result = a * b
        elif operation == 'divide':
            if b == 0:
                raise ZeroDivisionError
            result = a / b
        else:
            return f"Unknown operation: {operation}"

        return f"The result of {int(a)} {operation} {int(b)} is equal to {int(result)}"

    except ZeroDivisionError:
        return "An error occurred: Cannot divide by zero"

        '''
