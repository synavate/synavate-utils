import os
import sys
import logging
import ecs_logging
import sys
from ecs_logging import StdlibFormatter
from datetime import datetime
import uuid



def setup_logging(log_file="../logs/f"{__name__}-)
# Get the Logger
_logger = logging.getLogger(__name__)
_logger.setLevel(logging.ERROR)

# Add an ECS formatter to the Handler
handler = logging.StreamHandler()
handler_file = logging.FileHandler(f"../logs/{_logger}-{datetime.now()}.log")
handler.setFormatter(ecs_logging.StdlibFormatter())
handler_file.setFormatter(ecs_logging.StdlibFormatter())
_logger.addHandler(handler)
_logger.addHandler(handler_file)

def get_logger(name=__name__):
    """Get a logger instance."""
    return logging.getLogger(name)

# Emit a log!
_logger.debug("Example message!", extra={"http.request.method": "get"})







    

