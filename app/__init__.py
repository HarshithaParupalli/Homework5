import pkgutil
import importlib
from app.commands import CommandHandler

class App:
    def __init__(self):
        self.command_handler = CommandHandler()
        self.load_plugins()

    def load_plugins(self):
        # Iterate over all submodules in the plugins directory
        for loader, plugin_name, is_pkg in pkgutil.iter_modules(['app/plugins']):
            if is_pkg:
                # Dynamically import the plugin's __init__.py
                module = importlib.import_module(f'app.plugins.{plugin_name}')
                # Retrieve the command class from the module
                command_class = getattr(module, f"{plugin_name.capitalize()}Command", None)
                if command_class:
                    self.command_handler.register_command(plugin_name, command_class())


    def start(self):
        print("Type 'exit' to exit.")
        while True:  # REPL (Read, Evaluate, Process, Loop)
            user_input = input(">>> ").strip()
            if user_input.lower() == 'exit':
                break
            parts = user_input.split()
            if len(parts) == 3:
                a, b, operation = parts
                output = self.command_handler.execute_command(a, b, operation.lower())  # Make sure to convert to lowercase
                print(output)
            else:
                print("Invalid input format. Please provide: <number1> <number2> <operation>")

