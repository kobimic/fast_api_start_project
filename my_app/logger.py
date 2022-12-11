import logging
import os

app_name = os.getenv('APP_NAME', 'This is my fastapi project template')

logger = logging.getLogger(app_name)
console_handler = logging.StreamHandler()
logger.setLevel(logging.DEBUG)
console_format = logging.Formatter("%(name)s | %(levelname)s | %(module)s | %(message)s")
console_handler.setFormatter(console_format)
logger.addHandler(console_handler)

logger.info("Logger init done")