"""
Custom log output
"""

import sys
import logging

TEXT_NORMAL = 0
TEXT_BOLD = 1
TEXT_RED = 31
TEXT_GREEN = 32
TEXT_YELLOW = 33
TEXT_BLUE = 34
TEXT_MAGENTA = 35
TEXT_CYAN = 36


def get_logger():
    return logging.getLogger('exifreader')


def setup_logger(debug):
    """Configure the logger."""
    if debug:
        log_level = logging.DEBUG
    else:
        log_level = logging.INFO

    logger = logging.getLogger('exifreader')
    stream = Handler(log_level, debug)
    logger.addHandler(stream)
    logger.setLevel(log_level)


class Formatter(logging.Formatter):

    def __init__(self, debug=False):
        self.debug = debug
        if self.debug:
            log_format = '%(levelname)-6s %(message)s'
        else:
            log_format = '%(message)s'
        logging.Formatter.__init__(self, log_format)


class Handler(logging.StreamHandler):

    def __init__(self, log_level, debug=False):
        self.debug = debug
        logging.StreamHandler.__init__(self, sys.stdout)
        self.setFormatter(Formatter(debug))
        self.setLevel(log_level)
