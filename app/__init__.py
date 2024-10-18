import pkgutil
import importlib
from app.commands import CommandHandler

class App:
    def __init__(self):
        # Initialize the CommandHandler to manage commands
        self.command_handler = CommandHandler()
        self.load_plugins()

    def load_plugins(self):
        # Dynamically load plugins from the 'app/plugins' directory
        for loader, plugin_name, is_pkg in pkgutil.iter_modules(['app/plugins']):
            if is_pkg:
                # Dynamically import the plugin's __init__.py
                module = importlib.import_module(f'app.plugins.{plugin_name}')
                # Retrieve the command class from the module (e.g., AddCommand)
                command_class = getattr(module, f"{plugin_name.capitalize()}Command", None)
                if command_class:
                    # Register the command with the CommandHandler
                    self.command_handler.register_command(plugin_name.lower(), command_class())

    def start(self):
        # Start the REPL loop
        print("Welcome to the REPL Calculator. Type 'exit' to quit.")
        while True:
            # Accept user input
            user_input = input(">>> ").strip()
            if user_input.lower() == 'exit':
                break

            # Split input into components: <number1> <number2> <operation>
            parts = user_input.split()
            if len(parts) != 3:
                print("Invalid input format. Please provide: <number1> <number2> <operation>")
                continue

            # Unpack input
            a, b, operation = parts

            try:
                # Execute the command via CommandHandler
                result = self.command_handler.execute_command(a, b, operation.lower())
                print(result)  # Print the result from the command execution
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

