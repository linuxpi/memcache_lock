class TimeoutException(Exception):
    """
    Raised when max timeout reached while waiting for a lock to be acquired
    """
