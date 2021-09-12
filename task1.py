from datetime import datetime

cnt = {}


def decorate(function: callable):
    """
    Sinmplest decorator.

    :param function: object to be called.
    :return: generated wrapper
    """
    def wrap(*args):
        '''
        Wrapper for decorator. Callbacks, you are welcome!

        :param args: Arguments for callable object.
        :return: called function, given in higher-order method.
        '''
        global cnt
        st_dt = datetime.now()
        if cnt.get(function.__name__) is None:
            cnt[function.__name__] = 1
        else:
            cnt[function.__name__] += 1
        print(f'\n\nFunction {function.__name__} call #{cnt.get(function.__name__)} exec time {datetime.now() - st_dt}')
        res = function(*args)
        return res
    return wrap
