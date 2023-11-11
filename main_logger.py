import os
import logging
from utils import make_directory


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


# get the current working directory
BASE_DIR = os.path.dirname(__file__)
LOG_DIRS = os.path.join(BASE_DIR, "log")

# Define log levels and corresponding log file names
LOG_LEVEL = {
    "debug": logging.DEBUG,
    "info": logging.INFO,
    "warning": logging.WARNING,
    "error": logging.ERROR,
    "critical": logging.CRITICAL,
}
# define the log Formatter
FORMATTER = logging.Formatter(
    "%(asctime)s - [%(levelname)s] - %(pathname)s - %(filename)s \
     - %(module)s - %(lineno)s - %(message)s"
)


# * Define log for DEBUG mode
debug_dir_name = make_directory(LOG_DIRS, "debug")
debug_log_handler = logging.FileHandler(
    filename=f"{debug_dir_name}/debug.log", mode="a", encoding="utf-8"
)
debug_log_handler.setLevel(logging.DEBUG)
debug_log_handler.setFormatter(FORMATTER)


def logger_filter(record) -> bool:
    return record.levelno == logging.DEBUG


"""
Each handler will handle only one specific type of logging,
so each handler is set to a specific type of filter.
"""
# debug_log_handler.addFilter(logger_filter)
# debug_log_handler.filter = logger_filter
"""
debug_log_handler.addFilter(logger_filter), debug_log_handler.filter = logger_filter
or lambda function these all are same work.
"""
debug_log_handler.filter = lambda record: record.levelno == logging.DEBUG
# ** add a filter to the logger,
# logger.addFilter(logger_filter)
logger.addHandler(debug_log_handler)


# * Define log for INFO mode
info_dir_name = make_directory(LOG_DIRS, "info")
info_log_handler = logging.FileHandler(
    f"{info_dir_name}/info.log", mode="a", encoding="utf-8"
)
info_log_handler.setLevel(logging.INFO)
info_log_handler.setFormatter(FORMATTER)
info_log_handler.filter = lambda record: record.levelno == logging.INFO
logger.addHandler(info_log_handler)


# * Define log for WARNING mode
warning_dir_name = make_directory(LOG_DIRS, "warning")
warning_log_handler = logging.FileHandler(
    filename=f"{warning_dir_name}/warning.log", mode="a", encoding="utf-8"
)
warning_log_handler.setLevel(logging.WARNING)
warning_log_handler.setFormatter(FORMATTER)
warning_log_handler.filter = lambda record: record.levelno == logging.WARNING
logger.addHandler(warning_log_handler)


# * Define log for ERROR mode
error_dir_name = make_directory(LOG_DIRS, "error")
error_log_handler = logging.FileHandler(
    filename=f"{error_dir_name}/error.log", mode="a", encoding="utf-8"
)
error_log_handler.setLevel(logging.ERROR)
error_log_handler.setFormatter(FORMATTER)
error_log_handler.filter = lambda record: record.levelno == logging.ERROR
logger.addHandler(error_log_handler)


# * Define log for CRITICAL mode
critical_dir_name = make_directory(LOG_DIRS, "critical")
critical_log_handler = logging.FileHandler(
    filename=f"{critical_dir_name}/critical.log", mode="a", encoding="utf-8"
)
critical_log_handler.setLevel(logging.CRITICAL)
critical_log_handler.setFormatter(FORMATTER)
critical_log_handler.filter = lambda record: record.levelno == logging.CRITICAL
logger.addHandler(critical_log_handler)


# Create a console (stream) handler for displaying logs on the console
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)


# Create a custom formatter with color for log levels
class ColoredFormatter(logging.Formatter):
    COLORS = {
        logging.DEBUG: "\x1b[34m",  # Blue for DEBUG
        logging.INFO: "\x1b[32m",  # Green for INFO
        logging.WARNING: "\x1b[33m",  # Yellow for WARNING
        logging.ERROR: "\x1b[31m",  # Red for ERROR
        logging.CRITICAL: "\x1b[41m",  # Background Red for CRITICAL
    }
    RESET = "\x1b[0m"

    def format(self, record):
        log_message = super(ColoredFormatter, self).format(record)
        return f"{self.COLORS.get(record.levelno, '')}{log_message}{self.RESET}"


stream_formatter = ColoredFormatter(
    "[%(levelname)s] - %(name)s - %(message)s - %(filename)s - %(lineno)s"
)
stream_handler.setFormatter(stream_formatter)
logger.addHandler(stream_handler)
