# tests/test_logging.py

import logging

def test_logging(caplog):
    with caplog.at_level(logging.INFO):
        logging.info("Test log message")
    
    assert "Test log message" in caplog.text
