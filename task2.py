from datetime import datetime
import inspect

cnt = {}


def decorate(function: callable):
    """
    Updated simplest decorator.

    :param function: callable object.
    :return: its generated call.
    """
    def wrap(*args, **kwargs):
        """
        Wrapper. Prints metadata for given callable object.

        :param args: Direct arguments for callable.
        :param kwargs: Named arguments for callable.
        :return: call for callable.
        """
        st_dt = datetime.now()
        name = function.__name__
        global cnt
        cnt[name] = 1 if cnt.get(name) is None else cnt[name] + 1
        print(f'''\n\nFunction {name} call #{cnt.get(name)}, output:''', end='\n')
        res = function(*args, **kwargs)
        print(f'''exec time {datetime.now() - st_dt}\n''', end='\n')
        print('\n'.join([
            "Docs: " + str(inspect.getdoc(function)),
            'Comments: ' + str(inspect.getcomments(function)),
            'Source: \n' + str(inspect.getsource(function))
        ]))
        return res
    return wrap
