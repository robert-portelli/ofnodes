import logging
import pytest
from ofnodes.logging_config import configure_logging, logger
from ofnodes.structures.randomaccessarray import RandomAccessArray


def test_configure_logging(caplog):
    configure_logging(level=caplog.set_level(logging.DEBUG))

    logger.debug("This is a debug message")

    # Assert that the log message is captured
    assert "This is a debug message" in caplog.text

    # Verify the log level
    assert caplog.records[0].levelname == "DEBUG"

    # Check the log format (time, logger name, level, and message)
    log_message = caplog.records[0].message
    assert "This is a debug message" in log_message

    # Check the number of log records to ensure no unexpected logs are present
    assert len(caplog.records) == 1