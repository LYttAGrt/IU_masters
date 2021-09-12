from datetime import datetime
import inspect


class Decorator:
    def __init__(self, filename: str):
        self.cnt = {}
        self.scorer = {}
        self.dump = open(filename, 'w+')
        pass

    def __call__(self, function: callable):
        def wrap(*args, **kwargs):
            name = function.__name__
            self.cnt[name] = 1 if self.cnt.get(name) is None else self.cnt[name] + 1
            st_dt = datetime.now()
            res = function(*args, **kwargs)
            exec_time = datetime.now() - st_dt
            self.dump.write(f'''\n\nFunction {name} call #{self.cnt.get(name)} exec time {exec_time}\n''')
            self.scorer[name] = exec_time
            self.dump.write('\n'.join([
                "Docs: " + str(inspect.getdoc(function)),
                'Comments: ' + str(inspect.getcomments(function)),
                'Source: \n' + str(inspect.getsource(function))
            ]))
            return res
        return wrap

    def rank_and_close(self):
        if not self.dump.closed:
            data = [(k,v) for k,v in self.scorer.items()]
            data.sort(key=lambda x: str(x[1]))
            self.dump.write('\n\n\nWho\t|\tTime\n')
            for score in data:
                self.dump.write('\t|\t'.join([score[0], str(score[1])]) + '\n')
            self.dump.flush()
            self.dump.close()
        return 0
