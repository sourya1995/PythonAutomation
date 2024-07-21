import logging

LOGGER = logging.getLogger(__name__)

LOGGER.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

LOGGER.addHandler(console_handler)

LOGGER.info('This is an info message')
LOGGER.error('This is an error message')

# Function that might raise exceptions
def some_function():
    raise ValueError("This is a value error example")

# Using the logger for exceptions
try:
    result = some_function()
except ZeroDivisionError as e:
    LOGGER.exception("An error occurred: ZeroDivisionError")
except ValueError as e:
    LOGGER.exception("An error occurred: ValueError")
except Exception as e:
    LOGGER.exception("An unexpected error occurred")