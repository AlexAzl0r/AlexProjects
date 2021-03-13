import logging
from functools import wraps

logger = logging.getLogger(__name__)

def generate_logging(orig_func): #pragma: no cover
    logging.basicConfig(format="%(asctime)s:%")