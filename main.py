import inspect
import numpy as np

from task1 import decorate as t1_decorate
from task2 import decorate as t2_decorate
from task3 import Decorator as t3_Decorator
from task4 import decorate as t4_decorate


class Methods:
    """
        Simple class to store all testing methods.
    """
    def __init__(self):
        pass

    @classmethod
    def print_pascal(cls, layer: int):
        """
        Prints Pascal triangle. Costly, but ok so far.

        :param layer: the index of row to be printed.
        :return: Pascal's triangle line #{layer}
        """
        layer = abs(layer)
        arr = [[_ for _ in range(layer)] for _ in range(layer)]
        for i in range(layer):
            arr[i][0], arr[0][i] = 1, 1

        for i in range(1, layer):
            for j in range(1, layer):
                arr[i][j] = arr[i - 1][j] + arr[i][j - 1]

        for i in range(layer):
            for j in range(layer):
                if i + j == layer - 1:
                    print(arr[i][j], end=' ')
        return 0

    @classmethod
    def lambda_test(cls, **kwargs):
        """
        Simple processor of keyword arguments via lambda expression.

        :param kwargs: all given params
        :return: empty tuple.
        """
        L = lambda arg1, arg2: print(f'{str(arg1)}: {str(arg2)}')
        for k, v in kwargs.items():
            L(k, v)

    @classmethod
    def solve_eq(cls, a: float, b: float, c: float) -> (complex or float, complex or float):
        """
        Solves quadratic equation using NumPy.

        :param a: 2nd power coef.
        :param b: 1st power coef.
        :param c: Free coef.
        :return: tuple of 2, even if equal, solutions to given coefficients.
        """

        d = b * b - 4 * a * c
        d = complex(0, np.sqrt(abs(d)), ) if d < 0 else np.sqrt(d)
        return .5 * (-b + d) / a, .5 * (-b - d) / a

    @classmethod
    def print_self(cls):
        print(inspect.getsource(cls))

    @classmethod
    def lambda_dumb(cls):
        L = lambda everything: tuple()
        L()


class Task1(Methods):
    def __init__(self):
        """
            Task1 class.

            Each method, given below, calls an object from parent class.
            For docs, please check the #Methods class.
        """
        self.parent = super()
        self.parent.__init__()

    @t1_decorate
    def print_pascal(self, layer: int):
        return self.parent.print_pascal(layer)

    @t1_decorate
    def lambda_test(self, **kwargs):
        return self.parent.lambda_test(**kwargs)

    @t1_decorate
    def solve_eq(self, a: float, b: float, c: float):
        return print(self.parent.solve_eq(a, b, c))


class Task2(Methods):
    def __init__(self):
        """
            Task2 class.

            Each method, given below, calls an object from parent class.
            For docs, please check the #Methods class.
        """
        self.parent = super()
        self.parent.__init__()

    @t2_decorate
    def lambda_test(self, **kwargs):
        return self.parent.lambda_test(**kwargs)

    @t2_decorate
    def print_self(self):
        return self.parent.print_self()

    def __call__(self):
        self.parent.lambda_test(a=10, b=20, c=-40)


class Task3(Methods):
    decorator = t3_Decorator('test3.txt')

    def __init__(self):
        """
            Task3 class.

            Each method, given below, calls an object from parent class.
            For docs, please check the #Methods class.
        """
        self.parent = super()
        self.parent.__init__()

    @decorator
    def lambda_test(self, **kwargs):
        return self.parent.lambda_test(**kwargs)

    @decorator
    def print_self(self):
        return self.parent.print_self()

    @decorator
    def print_pascal(self, layer: int):
        return self.parent.print_pascal(layer)

    @decorator
    def solve_eq(self, a: float, b: float, c: float):
        return print(self.parent.solve_eq(a, b, c))

    def __call__(self):
        self.decorator.rank_and_close()


class Task4(Methods):
    def __init__(self):
        """
            Task4 class.

            Each method, given below, calls an object from parent class.
            For docs, please check the #Methods class.
        """
        self.parent = super()
        self.parent.__init__()

        print(self.parent.solve_eq)

    @t4_decorate
    def solve_eq(self, a: float, b: float, c: float):
        return self.parent.solve_eq(a, b, c)


# Probably, use inner method in testing classes, not main()
if __name__ == '__main__':
    # Test group 1
    t1 = Task1()
    t1.print_pascal(4)
    t1.print_pascal(3)
    t1.solve_eq(1, -2, 1)

    # Test group 2
    t2 = Task2()
    t2.lambda_test(a=20)
    t2.print_self()

    # Test group 3
    t3 = Task3()
    t3.lambda_test()
    t3.print_self()
    t3.print_pascal(10)
    t3.solve_eq(1, -2, 1)
    t3()

    # Test group 4
    t4 = Task4()
    # -- should be ok
    t4.solve_eq(1, -2, 1)
    # -- should fail successfully
    t4.solve_eq(1, -2, '1')

    exit(0)
