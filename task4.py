from contextlib import redirect_stderr
from datetime import datetime


def decorate(function: callable):
    """
    Final version of decorator. This time, we will stop on more simple implementation - only function.
    Log filename is hardcoded.

    :param function: object to be called
    :return: wrapped result of calling.
    """
    def wrap(*args, **kwargs):
        try:
            res = function(*args, **kwargs)
            return res
        except (Exception, RuntimeError):
            with open('t4_log.txt', 'w+') as f:
                with redirect_stderr(f):
                    f.write('Error caught at: ' + str(datetime.now()))

    return wrap