import logging
import sys



# Create handlers for stdout and stderr
stdout_handler = logging.StreamHandler(sys.stdout)
stderr_handler = logging.StreamHandler(sys.stderr)

# Set logging levels for each handler
stdout_handler.setLevel(logging.DEBUG)  # Log DEBUG and above to stdout
stderr_handler.setLevel(logging.WARNING) # Log WARNING and above to stderr

# Create a formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
stdout_handler.setFormatter(formatter)
stderr_handler.setFormatter(formatter)


def get_logger(name:str, log_level=logging.DEBUG):
  # Configure logging

  logger = logging.getLogger(name)
  logger.setLevel(log_level)  # Set overall level to include DEBUG
  # Add the handlers to the logger
  logger.addHandler(stdout_handler)
  logger.addHandler(stderr_handler)
  return logger