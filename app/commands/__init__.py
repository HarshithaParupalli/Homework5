# app/commands/__init__.py

from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self, a: str, b: str):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, name, command):
        self.commands[name] = command

    def execute_command(self, a: str, b: str, operation: str):
        command = self.commands.get(operation)
        if command:
            return command.execute(a, b)
        else:
            return f"Unknown operation: {operation}"

