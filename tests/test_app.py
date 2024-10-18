# tests/test_app.py

import os
import pytest
from app import App

# Mock app class for testing
class MockApp(App):
    def start(self):
        return "App started"

def test_environment_variable(monkeypatch):
    # Use monkeypatch to temporarily set the environment variable
    monkeypatch.setenv('ENVIRONMENT', 'testing')

    environment = os.getenv('ENVIRONMENT')
    assert environment == 'testing'

def test_app_start():
    # Test if the start method of the App works correctly
    mock_app = MockApp()
    result = mock_app.start()
    assert result == "App started"
