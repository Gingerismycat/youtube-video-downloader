import logging

import yaml

from .constants import APP_ROOT

LOGGING_LEVELS = {
    "DEBUG": logging.DEBUG,  # 10
    "INFO": logging.INFO,  # 20
    "WARNING": logging.WARNING,  # 30
    "ERROR": logging.ERROR,  # 40
    "CRITICAL": logging.CRITICAL,  # 50
}


def read_app_config() -> dict:
    """Read the app level config file as a dictionary."""
    with open(APP_ROOT / "config.yaml", "r") as fh:
        config = yaml.safe_load(fh.read())
    return config


def get_logging_level() -> str:
    """Get the logging config settings."""
    config = read_app_config()
    logging_setting = config["logging"]["level"]
    logging_level = LOGGING_LEVELS[logging_setting]
    return logging_level


def setup_logger():
    """Configure the loggers."""
    logging_level = get_logging_level()
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging_level)
    logging.basicConfig(
        level=logging_level,
        format="[%(asctime)s] %(levelname)s %(name)s %(module)s : %(message)s",
        datefmt="%d/%b/%Y %H:%M:%S",
        handlers=[stream_handler],
        force=True,
    )
    logging.captureWarnings(True)