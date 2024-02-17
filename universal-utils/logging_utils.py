import logging
import ecs_logging
import sys
from ecs_logging import StdlibFormatter
from datetime import datetime

# Get the Logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

# Add an ECS formatter to the Handler
handler = logging.StreamHandler()
handler_file = logging.FileHandler(f"../logs/{logger}-{datetime.now()}.log")
handler.setFormatter(ecs_logging.StdlibFormatter())
handler_file.setFormatter(ecs_logging.StdlibFormatter())
logger.addHandler(handler)
logger.addHandler(handler_file)

# Emit a log!
logger.debug("Example message!", extra={"http.request.method": "get"})







    

