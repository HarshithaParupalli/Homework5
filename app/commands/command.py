# app/commands/command.py

class Command:
    def execute(self, num1, num2):
        raise NotImplementedError("Subclasses must implement this method.")
