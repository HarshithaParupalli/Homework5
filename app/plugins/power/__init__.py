# app/plugins/power/__init__.py

from app.commands import Command
from decimal import Decimal, InvalidOperation

class PowerCommand(Command):
    def execute(self, a: str, b: str):
        try:
            a_decimal, b_decimal = map(Decimal, [a, b])
            return f"The result of {a} raised to {b} is {a_decimal ** b_decimal}"
        except InvalidOperation:
            return f"Invalid number input: {a} or {b} is not a valid number."
